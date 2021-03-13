import codecs
import base64

_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Easy way #1
b64 = codecs.encode(codecs.decode(_hex, "hex"), "base64")
print(f"Easy way #1: {b64}")

# Easy way #2
print(f"Easy way #2: {base64.b64encode(codecs.decode(_hex, 'hex'))}")

# Hard way #1
def b64_encode(_hex: str):
    _hex = codecs.decode(_hex, "hex").decode()

    i = 0
    base64 = ending = ""
    base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Add padding if string is not dividable by 3
    pad = 3 - (len(_hex) % 3)
    if pad != 3:
        _hex += "A" * pad
        ending += "=" * pad

    # Iterate though the whole input string
    while i < len(_hex):
        b = 0

        # Take 3 characters at a time, convert them to 4 base64 chars
        for j in range(0, 3, 1):

            # get ASCII code of the next character in line
            n = ord(_hex[i])
            i += 1

            # Concatenate the three characters together
            b += n << 8 * (2 - j)

        # Convert the 3 chars to four Base64 chars
        base64 += base64chars[(b >> 18) & 63]
        base64 += base64chars[(b >> 12) & 63]
        base64 += base64chars[(b >> 6) & 63]
        base64 += base64chars[b & 63]

    # Add the actual padding to the end
    if pad != 3:
        base64 = base64[:-pad]
        base64 += ending
    return base64.encode()


print(f"Hard way #1: {b64_encode(_hex)}")
