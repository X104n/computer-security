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
    iv = [1] * 32
    hash = hakunaMatata(p, iv)
    print("Hashing gold_plaintext.in we get:", hash, "as the result")
    print("Or see the 'hash.txt' in the output folder")
    f2b.writeMain("output/hash.txt", hash)
    print("For the questions on problem 2, the size of the hash is 32 bits. And it will always be 32 bits because "
          "hashes have a fixed length.")
    print("Using the birthday attack, we can find that the probability of finding a pair of inputs with the same hash "
          "(aka a collision) is 2^(n/2). And in our case that is 2^(32/2) = 2^16 = 65536. So in theory the attacker "
          "would on the 65537th attempt find a collision.")
