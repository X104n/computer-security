import f2b
import gold as enc


def plain_to_block(plaintext, blockSize):
    blocks = []
    while len(plaintext) >= blockSize:
        block = []
        for i in range(blockSize):
            block.append(plaintext[0])
            plaintext.pop(0)
        blocks.append(block)

    if len(plaintext) != 0:
        for i in range(blockSize - len(plaintext)):
            plaintext.append(0)
        blocks.append(plaintext)

    return blocks


def ecb(p, k):
    plainBlock = plain_to_block(p, 32)
    cryptBlock = []

    for i in range(len(plainBlock)):
        cryptBlock.extend(enc.encrypt(plainBlock[i], k))

    return cryptBlock


def cbc(p, k, iv):
    plainBlock = plain_to_block(p, 32)
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
    plainBlock = plain_to_block(p, 32)
    stream = []
    result = []

    for i in range(len(plainBlock)):

        if i == 0:
            stream = enc.encrypt(iv, k)
        else:
            stream = enc.encrypt(stream, k)

        result.extend(enc.xor(plainBlock[i], stream))

    return result


if __name__ == '__main__':
    k = [0, 1] * 16
    iv = [1] * 32

    p = f2b.readMain("gold_plaintext.in")
    f2b.writeMain("output/ecbEncryption.txt", ecb(p, k))

    p = f2b.readMain("gold_plaintext.in")
    f2b.writeMain("output/cbcEncryption.txt", cbc(p, k, iv))

    p = f2b.readMain("gold_plaintext.in")
    f2b.writeMain("output/ofbEncryption.txt", ofb(p, k, iv))
