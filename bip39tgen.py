#! /usr/bin/python
import binascii, hashlib, struct, os, zlib
s = (lambda x: str(x, "ascii"), str)[type(struct.pack('B', 0)) is str]
y = (lambda x: bytes(x, "ascii"), str)[type(struct.pack('B', 0)) is str]
words = s(zlib.decompress(binascii.a2b_base64(y(
"""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
""".replace("\n", ""))), -15)).split()
if getattr(os, 'urandom', None):
  a, b = struct.unpack(">QQ", os.urandom(16))
else:
  import random; a, b = random.getrandbits(64), random.getrandbits(64)
c = hashlib.sha256(struct.pack(">QQ", a, b)).digest()[:1]
c = a << 68 | b << 4 | struct.unpack("B", c)[0] >> 4
print(" ".join(words[c >> i & 2047] for i in range(121, -8, -11)))
