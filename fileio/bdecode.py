
class Decoder:
    def __init__(self, binary: bytes):
        self.text = binary
        self.ind = 0

    def _pop(self):
        self.ind += 1
        return self.text[self.ind - 1]

    def _skip(self):
        self.ind += 1

    def _chunk(self, size):
        self.ind += size
        return self.text[self.ind - size:self.ind]

    def _cur(self):
        try:
            return self.text[self.ind]
        except:
            print(self.ind)
            print(len(self.text))
            raise

    def decode(self):
        char = chr(self._cur())

        try:
            if char == "d":
                self._skip()
                return self.decode_dict()
            elif char == "l":
                self._skip()
                return self.decode_list()
            elif char == "i":
                self._skip()
                return self.decode_int(ord("e"))
            elif char.isnumeric():
                return self.decode_str()
            else:
                raise
        except:
            print(self.text.decode("ascii")[self.ind-2:self.ind+2])
            raise Exception("Weird bencoding at ", self.ind)

    def decode_dict(self):
        obj = {}

        while chr(self._cur()) != "e":
            key = self.decode()
            value = self.decode()
            obj[key] = value

        self._skip()
        return obj

    def decode_list(self):
        obj = []

        while chr(self._cur()) != "e":
            obj.append(self.decode())

        self._skip()
        return obj

    def decode_int(self, ending):
        obj = 0

        while self._cur() != ending:
            obj *= 10

            try:
                obj += self._pop() - 48
            except ValueError:
                raise Exception("weird number at ", self.ind)

        self._skip()
        return obj

    def decode_str(self):
        return self._chunk(self.decode_int(ord(":")))
