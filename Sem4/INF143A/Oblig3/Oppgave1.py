import f2b

k = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

p = f2b.main("gold_plaintext.in")


def plain_to_block(plaintext):
    blocks = []
    while len(plaintext) >= 32:
        block = []
        for i in range(32):
            block.append(plaintext[0])
            plaintext.pop(0)
        blocks.append(block)

    if len(plaintext) != 0:
        for i in range(32 - len(plaintext)):
            plaintext.append(0)
        blocks.append(plaintext)

    return blocks


def ecb(p, k, iv):
    return None
