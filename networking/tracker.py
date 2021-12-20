from urllib.parse import urlencode
import asyncio
import aiohttp


class Tracker:
    def __init__(self, metainfo):
        self.metainfo = metainfo

    async def get_request(self, peer_id, port, uploaded, downloaded,
                          left, event, session: aiohttp.ClientSession):
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
                response = await session.get(url)

                if response.status != 200:
                    print("unable to connect to ", tracker, ", trying other trackers")
                else:
                    return response.content

                response.close()
            except aiohttp.ClientError as e:
                print("tracker", tracker, "failed because \"", e, "\"trying other trackers")

            raise Exception("Couldn't get one single tracker to work >:(")
