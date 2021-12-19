import random
from fileio.bdecode import Decoder
from networking.tracker import Tracker


class Torrent:
    def __init__(self, tracker: Tracker):
        self.tracker = tracker

        self.peer_id = "-BG0001-" + str(random.randint(0, 10 ** 12 - 1)).zfill(12)
        self.port = 6884
        self.uploaded = 0
        self.downloaded = 0
        self.left = tracker.metainfo.size
        self.event = "started"

        self.raw = self.tracker.get_request(self.peer_id, self.port,
                                                       self.uploaded, self.downloaded,
                                                       self.left, self.event)

        self.response = Decoder(self.raw).decode()
        self.peers = self.response[b"peers"]
        self.interval = self.response[b"interval"]

    def getresponse(self):
        pass
