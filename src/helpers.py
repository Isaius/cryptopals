import binascii


def b64_to_bytes(encoded):
    return binascii.a2b_base64(encoded)
