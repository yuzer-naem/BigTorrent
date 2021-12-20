import asyncio
import aiohttp

from fileio.metainfo import MetaInfo
from fileio.bencode import Encoder
from fileio.bdecode import Decoder
from networking.torrent import Torrent
from networking.tracker import Tracker


async def main():
    session = aiohttp.ClientSession()
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
    print(torrent.raw)

if __name__ == '__main__':
    asyncio.run(main())
