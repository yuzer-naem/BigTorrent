import unittest
from fileio.bdecode import Decoder
from fileio.bencode import Encoder


class TestBencoder(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = {
            b"number": 5,
            b"list": [b"we are gaming", 12, b"nice to meet you"]
        }

        self.text = b"d6:numberi5e4:listl13:we are gamingi12e16:nice to meet youee"

    def test_decode(self):
        decoder = Decoder(self.text)
        self.assertEqual(decoder.decode(), self.obj)

    def test_encode(self):
        encoder = Encoder(self.obj)
        self.assertEqual(encoder.encode(), self.text)


