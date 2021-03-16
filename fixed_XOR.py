import codecs

def fixed_XOR(str1: str, str2: str):
  a_buffer = bytes.fromhex(str1)
  b_buffer = bytes.fromhex(str2)

  # Inputs must have the same size
  if len(a_buffer) != len(b_buffer):
    raise 'No matching size of inputs'

  # bitwise operator over tuples (a_buffer[i], b_buffer[i]) returned by zip()
  xor_buffer = bytes(a ^ b for (a, b) in zip(a_buffer, b_buffer))

  return codecs.encode(xor_buffer, "hex")
