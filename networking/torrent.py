import random
from fileio.bdecode import Decoder
from networking.tracker import Tracker
import asyncio


class Torrent:
    def __init__(self, tracker: Tracker):
        self.tracker = tracker

        self.peer_id = "-BG0001-" + str(random.randint(0, 10 ** 12 - 1)).zfill(12)
        self.port = 221
        self.uploaded = 0
        self.downloaded = 0
        self.left = tracker.metainfo.size

        self.raw = None
        self.response = None
        self.peers = None
        self.interval = None
        self.is_alive = True

        self.params = {
            "peer_id": self.peer_id,
            "port": self.port,
            "uploaded": self.uploaded,
            "downloaded": self.downloaded,
            "left": self.left,
            "compact": 0,
            "event": "started",
        }

    async def start(self, session):
        self.raw = await self.tracker.get_request(self.params, session)
        self.response = Decoder(self.raw).decode()

        self.peers = self.response[b"peers"]
        self.interval = self.response[b"interval"]

    async def communicate(self, session, interval):
        while self.is_alive:
            cor = self.tracker.get_request(self.params, session)
            await asyncio.sleep(interval)
            await cor

