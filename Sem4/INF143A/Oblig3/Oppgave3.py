import hashlib
import gold as enc
import Oppgave1 as o1
import f2b


def listToBytes(list):
    return b''.join(f2b.bits_to_bytes(list))


def stringToList(string):
    res = []
    for i in string:
        res.append(int(i))
    return res


def enrycpting(p, k, iv):
    plainBlock = o1.plain_to_block(p, 256)
    result = []

    for i in range(len(plainBlock)):

        if i == 0:
            M = iv
        else:
            M = plainBlock[i - 1]

        concat = k + M
        cipher = hashlib.sha256(b''.join(f2b.bits_to_bytes(concat))).digest()
        cryptedBlock = enc.xor(f2b.bytes_to_bits(cipher)[:len(plainBlock[i])], plainBlock[i])
        result.extend(cryptedBlock)

    return result


if __name__ == "__main__":
    p = f2b.readMain("gold_plaintext.in")
    iv = [1] * 256
    k = [0, 1] * 128
    blocks = enrycpting(p, k, iv)
    f2b.writeMain("output/sha256.txt", blocks)
