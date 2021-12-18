from fileio import bencode, bdecode
import hashlib


class MetaInfo:
    def __init__(self, filepath):
        self.file = filepath

        with open(filepath, 'rb') as file:
            self.binary = file.read()

        decoder = bdecode.Decoder(self.binary)

        self.dict = decoder.decode()
        self.info_dict = self.dict[b"info"]

        self.info_string = bencode.Encoder(self.info_dict).encode()
        hasher = hashlib.sha1()
        hasher.update(self.info_string)
        self.info_hash = hasher.digest()

        self.size = self.info_dict[b"piece length"] * len(self.info_dict[b"pieces"]) / 20
        self.trackers = self.dict[b"url-list"]
