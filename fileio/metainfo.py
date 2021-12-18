import fileio.bdecode
from fileio import bdecode


class MetaInfo:
    def __init__(self, filepath):
        self.file = filepath

        with open(filepath, 'rb') as file:
            self.binary = file.read()

        decoder = bdecode.Decoder(self.binary)
        self.object = decoder.decode()
