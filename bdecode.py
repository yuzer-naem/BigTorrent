

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