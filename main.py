from bencode import Encoder
from bdecode import Decoder

file = input("enter torrent file to open: ")
print(file)

obj = {
    "number": 5,
    "list": ["we are gaming", 12, b"nice to meet you"]
}

encoder = Encoder(obj)
text = encoder.encode()
print(text)
print(text.decode("ascii"))
print(obj)
decoder = Decoder(text)
print(decoder.decode())
