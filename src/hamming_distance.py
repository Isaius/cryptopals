def hamming_distance(str1: str, str2: str):
    a_bytes = bytearray(str1, "ascii")
    b_bytes = bytearray(str2, "ascii")

    a_bits = ascii_to_bin(a_bytes)
    b_bits = ascii_to_bin(b_bytes)

    diff_counter = 0

    for (a, b) in zip(a_bits, b_bits):
        if a != b:
            diff_counter += 1

    return diff_counter


def ascii_to_bin(item):
    result = ""

    for i in item:
        result += format(i, "08b")

    return result
