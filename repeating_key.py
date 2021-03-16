from fixed_XOR import fixed_XOR
import codecs

def repeating_key(plaintext: str, key: str):
  index = -1
  result = "".encode()

  for b in plaintext:
    result += fixed_XOR(b.encode(), key[next_key(key, index)].encode())

  return result


def next_key(key, actual_index):
  return 0 if actual_index == len(key)-1 else actual_index+1