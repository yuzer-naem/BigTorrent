from networking.response import TrackerResponse
import requests
from urllib.parse import urlencode


class Tracker:
    def __init__(self, metainfo):
        self.metainfo = metainfo

    def get_request(self, peer_id, port, uploaded, downloaded,
                          left, event) -> TrackerResponse:
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

        for tracker in self.metainfo.trackers:
            if isinstance(tracker, list):
                print("length is", len(tracker))
                tracker = tracker[0]

            url = tracker.decode("ascii") + "?" + urlencode(params)
            print(tracker)
            print(urlencode(params))

            try:
                with requests.get(url) as response:
                    if response.status_code != 200:
                        print("unable to connect to ", tracker, ", trying other trackers")
                    else:
                        return response.content
            except ConnectionError as e:
                print("tracker", tracker, "failed because \"", e, "\"trying other trackers")

            raise Exception("Couldn't get one single tracker to work >:(")
