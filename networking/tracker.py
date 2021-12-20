from urllib.parse import urlencode
import asyncio
import aiohttp
import requests


class Tracker:
    def __init__(self, metainfo):
        self.metainfo = metainfo

    async def get_request(self, params, session):
        params["info_hash"] = self.metainfo.info_hash

        for tracker in self.metainfo.trackers:
            if isinstance(tracker, list):
                tracker = tracker[0]

            url = tracker.decode("ascii") + "?" + urlencode(params)
            print(tracker)
            print(urlencode(params))

            try:
                with await session.get(url) as response:
                    if response.code != 200:
                        print("unable to connect to ", tracker, ", trying other trackers")
                    else:
                        return response.content
            except aiohttp.ClientError as e:
                print("tracker", tracker, "failed because \"", e, "\"trying other trackers")

        raise Exception("Couldn't get one single tracker to work >:(")


