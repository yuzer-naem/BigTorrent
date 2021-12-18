from networking.response import TrackerResponse


class Tracker:
    def __init__(self, metainfo):
        self.metainfo = metainfo

    def get_request(self, peer_id, port, uploaded, downloaded, left, event) -> TrackerResponse:
        params = {
            "info_hash": self.metainfo.info_hash,
            "peer_id": peer_id,
            "port": port,
            "uploaded": uploaded,
            "downloaded": downloaded,
            "left": left,
            "compact": 0,
            "event": event,
        }

        return TrackerResponse(b"fuck")
