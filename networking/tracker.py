from fileio import bencode, bdecode
import hashlib
import random


class Torrent:
    def __init__(self, metainfo):
        self.metainfo = metainfo

        # params
        self.info_string = bencode.Encoder(metainfo.object[b"info"]).encode()
        hasher = hashlib.sha1()
        hasher.update(self.info_string)
        self.info_hash = hasher.digest()
        self.peer_id = "-BG0001-" + str(random.randint(0, 10 ** 12 - 1)).zfill(12)
        self.port = 0
        self.uploaded = 0
        self.downloaded = 0
        self.left = 0
        self.event = "started"

    def get_request(self, port, uploaded, downloaded, left, event):
        pass
