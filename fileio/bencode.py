class Encoder:
    def __init__(self, obj):
        self.obj = obj

    def encode(self) -> bytes:
        return self._encode(self.obj)

    @staticmethod
    def _encode(obj) -> bytes:
        if isinstance(obj, list):
            return Encoder._encode_list(obj)
        elif isinstance(obj, dict):
            return Encoder._encode_dict(obj)
        elif isinstance(obj, int):
            return Encoder._encode_int(obj)
        elif isinstance(obj, str):
            return str(len(obj)).encode("ascii") + b":" + obj.encode("ascii")
        elif isinstance(obj, bytes):
            return str(len(obj)).encode("ascii") + b":" + obj
        else:
            raise ValueError("Bencoder got bad type: {}".format(type(obj)))

    @staticmethod
    def _encode_list(lst: list) -> bytes:
        builder = b"l"

        for item in lst:
            builder += Encoder._encode(item)

        builder += b"e"
        return builder

    @staticmethod
    def _encode_dict(dct) -> bytes:
        builder = b"d"

        for key, value in dct.items():
            builder += Encoder._encode(key)
            builder += Encoder._encode(value)

        builder += b"e"
        return builder

    @staticmethod
    def _encode_int(num: int) -> bytes:
        return ("i" + str(num) + "e").encode("ascii")

