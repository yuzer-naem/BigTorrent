from urllib.parse import urlencode
import aiohttp


class Tracker:
    def __init__(self, metainfo):
        self.metainfo = metainfo

    async def get_request(self, params, session):
        params["info_hash"] = self.metainfo.info_hash

        for tracker in self.metainfo.trackers:
            if isinstance(tracker, list):
                tracker = tracker[0]

            url = tracker.decode("ascii") + "?" + urlencode(params)
            # url = "https://www.google.com"
            print(tracker)
            print(urlencode(params))

            try:
                async with session.get(url) as response:
                    if not response.status == 200:
                        raise ConnectionError('Unable to connect to tracker, {}'.format(response.status))
                    return await response.read()
            except aiohttp.ClientError as e:
                print("tracker", tracker.decode("ascii"), "failed because \"", e, "\"trying other trackers")

        raise Exception("Couldn't get one single tracker to work >:(")


