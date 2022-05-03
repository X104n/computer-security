import gold as enc
import Oppgave1 as o1
import f2b


def hakunaMatata(p, iv):
    plainBlock = o1.plain_to_block(p, 32)
    result = []

    for i in range(len(plainBlock)):

        if i == 0:
            key = iv
        else:
            key = result

        encrypted = enc.encrypt(plainBlock[i], key)
        result = (enc.xor(encrypted, plainBlock[i]))
    return result


if __name__ == "__main__":
    p = f2b.readMain("gold_plaintext.in")
    iv = [1, 0, 0, 1] * 8
    print(hakunaMatata(p, iv))
