import codecs

# Easy way
_hex = "10000000000002ae"
b64 = codecs.encode(codecs.decode(_hex, "hex"), "base64")
print(b64.decode())

# Hard way