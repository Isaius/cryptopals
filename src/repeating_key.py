from src.fixed_XOR import fixed_XOR


def repeating_key(plaintext, key):
    index = -1
    result = b""

    for char in plaintext:
        index = next_key(key, index)
        result += fixed_XOR(char.encode(), key[index].encode())
    return result


def next_key(key, actual_index):
    return 0 if actual_index == len(key) - 1 else actual_index + 1
