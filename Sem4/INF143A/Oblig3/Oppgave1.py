import f2b
import gold as enc

testK = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#k = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
k = [1] * 32
iv = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
poly = []


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


def ecb(p, k):
    plainBlock = plain_to_block(p)
    cryptBlock = []

    for i in range(len(plainBlock)):
        cryptBlock.extend(enc.encrypt(plainBlock[i], k))

    return cryptBlock


def cbc(p, k, iv):
    plainBlock = plain_to_block(p)
    cryptBlock = []
    result = []

    for i in range(len(plainBlock)):

        if i == 0:
            currentBlock = enc.xor(plainBlock[i], iv)
        else:
            currentBlock = enc.xor(plainBlock[i], cryptBlock[i - 1])

        cryptBlock.append(enc.encrypt(currentBlock, k))

    for i in range(len(cryptBlock)):
        result.extend(cryptBlock[i])

    return result

def ofb(p, k, iv):
    plainBlock = plain_to_block(p)
    stream = []
    result = []

    for i in range(len(plainBlock)):

        if i == 0:
            stream = enc.encrypt(iv, k)
        else:
            stream = enc.encrypt(stream, k)

        result.extend(enc.xor(plainBlock[i], stream))

    return result


p = f2b.readMain("gold_plaintext.in")

f2b.writeMain("cbcEncryption.txt", cbc(p, k, iv))

#print(cbc(p, k, iv))
