import zlib
s = b'witch which has which witches wrist watch'
print(len(s), s)

t = zlib.compress(s)
print(len(t), t)

print(zlib.decompress(t))
print(zlib.crc32(s))
