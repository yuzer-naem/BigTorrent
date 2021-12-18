from fileio.metainfo import MetaInfo
from fileio.bencode import Encoder
from fileio.bdecode import Decoder
from networking.client import Client
from networking.tracker import Tracker

file = input("enter torrent file to open: ")

metainfo = MetaInfo(file)

info = metainfo.dict[b"info"]

# should both be true
print(metainfo.binary == Encoder(metainfo.dict).encode())
print(metainfo.dict == Decoder(metainfo.binary).decode())

torrent = Client(Tracker(metainfo))

print(torrent.peer_id)
print(torrent.response)
