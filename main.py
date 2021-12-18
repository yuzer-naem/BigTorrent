from fileio.metainfo import MetaInfo
from fileio.bencode import Encoder
from fileio.bdecode import Decoder

file = input("enter torrent file to open: ")

metainfo = MetaInfo(file)

info = metainfo.object[b"info"]

print(metainfo.binary == Encoder(metainfo.object).encode())
print(metainfo.object == Decoder(metainfo.binary).decode())
