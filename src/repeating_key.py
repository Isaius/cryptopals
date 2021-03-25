from src.fixed_XOR import fixed_XOR


def repeating_key(plaintext: str, key: str):
    index = -1
    result = "".encode()

    for b in plaintext:
        index = next_key(key, index)
        result += fixed_XOR(b.encode(), key[index].encode())

    return result


def next_key(key, actual_index):
    return 0 if actual_index == len(key) - 1 else actual_index + 1
