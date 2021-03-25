import codecs


def fixed_XOR(a_buffer, b_buffer):
    # Inputs must have the same size
    if len(a_buffer) != len(b_buffer):
        raise Exception("Input doesn't have matching sizes")

    # bitwise operator over tuples (a_buffer[i], b_buffer[i]) returned by zip()
    xor_buffer = bytes(a ^ b for (a, b) in zip(a_buffer, b_buffer))

    return codecs.encode(xor_buffer, "hex")
