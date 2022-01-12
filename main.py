import asyncio
import aiohttp

from fileio.metainfo import MetaInfo
from fileio.bencode import Encoder
from fileio.bdecode import Decoder
from networking.torrent import Torrent
from networking.tracker import Tracker
import certifi
import ssl


async def main():
    sslcontext = ssl.create_default_context(cafile=certifi.where())
    connection = aiohttp.TCPConnector(ssl=sslcontext)

    async with aiohttp.ClientSession(connector=connection) as session:
        file = input("enter torrent file to open: ")
        metainfo = MetaInfo(file)
        info = metainfo.dict[b"info"]

        # should both be true
        print(metainfo.binary == Encoder(metainfo.dict).encode())
        print(metainfo.dict == Decoder(metainfo.binary).decode())

        torrent = Torrent(Tracker(metainfo))
        await torrent.start(session)

        print(torrent.peer_id)
        print(torrent.response)


if __name__ == '__main__':
    # event loop policy stops a weird error message
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
