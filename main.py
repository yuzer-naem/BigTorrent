from bencoding import Encoder

file = input("enter torrent file to open: ")
print(file)

obj = {
    "number": 5,
    "list": ["we are gaming", 12, b"nice to meet you"]
}

encoder = Encoder(obj)

print(encoder.encode())
