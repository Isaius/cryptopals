import codecs

def fixed_XOR(a_buffer: bytes, b_buffer: bytes):
  # Inputs must have the same size
  if len(a_buffer) != len(b_buffer):
    raise 'No matching size of inputs'

  # bitwise operator over tuples (a_buffer[i], b_buffer[i]) returned by zip()
  xor_buffer = bytes(a ^ b for (a, b) in zip(a_buffer, b_buffer))

  return codecs.encode(xor_buffer, "hex")
