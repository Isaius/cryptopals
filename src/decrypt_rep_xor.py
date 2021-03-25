import math

from src.hamming_distance import hamming_distance


def break_repeation_xor(cyphertext):
    keysize = find_keysize(cyphertext)
    blocks = split_in_blocks(cyphertext, keysize)
    tranposed_blocks = transpose_blocks(blocks)


def find_keysize(cyphertext, MAX_KEY_SIZE=40):
    KEYSIZE_OF_SMALLEST_DISTANCE = MAX_KEY_SIZE
    SMALLEST_NORMALIZED_DISTANCE = KEYSIZE_OF_SMALLEST_DISTANCE * 2

    for KEYSIZE in range(2, MAX_KEY_SIZE):
        section_1 = get_section_bytes(cyphertext, 0, KEYSIZE)
        section_2 = get_section_bytes(cyphertext, 1, KEYSIZE)

        distance = hamming_distance(section_1.decode(), section_2.decode())
        normal = distance / KEYSIZE

        if normal < SMALLEST_NORMALIZED_DISTANCE:
            SMALLEST_NORMALIZED_DISTANCE = normal
            KEYSIZE_OF_SMALLEST_DISTANCE = KEYSIZE

    return KEYSIZE_OF_SMALLEST_DISTANCE


# breaks the given input into blocks of the given blocksize
def split_in_blocks(cyphertext, blocksize):
    blocks_quantity = math.ceil(len(cyphertext) / blocksize)
    blocks = []

    for i in range(blocks_quantity):
        blocks.append(get_section_bytes(cyphertext, i, blocksize))

    return blocks


# buffer is the source, section is which part and size is what size each part should have
def get_section_bytes(buffer, section, size=1):
    start = section * size
    end = start + size

    return buffer[start:end]


def transpose_blocks(blocks):
    tranposed_blocks = []

    for i in range(len(blocks[0])):
        transp_block = []
        try:
            # Each i-th byte of all blocks make the transposed block
            for block in blocks:
                transp_block.append(block[i])
            tranposed_blocks.append(transp_block)
        except (IndexError, KeyError):
            tranposed_blocks.append("0".encode())
    return tranposed_blocks
