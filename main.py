## To test functions
from codecrypto import *
import codecs
import base64

## MAIN PROGRAM
_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


# Easy way #1
b64 = codecs.encode(codecs.decode(_hex, "hex"), "base64")
print(f"Easy way #1: {b64}")

# Easy way #2
print(f"Easy way #2: {base64.b64encode(codecs.decode(_hex, 'hex'))}")

print(f"Hard way #1: {b64_encode(_hex)}\n\n")

input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'

a_buffer = bytes.fromhex(input1)
b_buffer = bytes.fromhex(input2)

result = fixed_XOR(a_buffer, b_buffer)
print(f"fixed xor: {result}\n\n")

stanza = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
output = repeating_key(stanza, 'ICE')
print(f"repeating key: {output}\n\n")