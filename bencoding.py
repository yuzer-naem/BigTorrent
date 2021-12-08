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


class Decoder:
    def __init__(self, binary: bytes):
        self.text = binary.decode("ascii")
        self.ind = 0

    def _pop(self) -> str:
        self.ind += 1
        return self.text[self.ind - 1]

    def _skip(self):
        self.ind += 1

    def _chunk(self, size):
        self.ind += size
        return self.text[self.ind - size:self.ind]

    def _cur(self):
        return self.text[self.ind]

    def decode(self) -> object:
        char: str = self._cur()

        if char == "d":
            self._skip()
            return self.decode_dict()
        elif char == "l":
            self._skip()
            return self.decode_list()
        elif char == "i":
            self._skip()
            return self.decode_int("e")
        elif char.isnumeric():
            return self.decode_str()
        else:
            print(char)
            raise Exception("Weird bencoding at ", self.ind)

    def decode_dict(self):
        obj = {}

        while self._cur() != "e":
            key = self.decode()
            value = self.decode()
            obj[key] = value

        self._skip()
        return obj

    def decode_list(self):
        obj = []

        while self._cur() != "e":
            obj.append(self.decode())

        self._skip()
        return obj

    def decode_int(self, ending):
        obj = 0

        while self._cur() != ending:
            obj *= 10
            try:
                obj += int(self._pop())
            except ValueError:
                raise Exception("weird number at ", self.ind)

        self._skip()
        return obj

    def decode_str(self):
        return self._chunk(self.decode_int(":")).encode("ascii")

