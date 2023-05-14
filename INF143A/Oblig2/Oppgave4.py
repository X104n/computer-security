import random as Isiy_koum_omh_hrobtvv_tk_Heigv_Mlvcqyzrj
import Oppgave1 as op1
import random



def setup():
    prime = int("""172471720944269739125606601541029487739340755626635
7725839713037594384191757726636695937218465501974427444
6965608060294664492706195111168863727536280366014000584
1509436858417187894094969161813013831722315776185924842
0990938995935683346965929645166170330762460615936845115
50344711963113062475271615663164060997""".replace("\n", ""))

    generator = 3
    dec = 333
    germanS = op1.powerCal(generator, dec, prime)
    return prime, generator, germanS, dec


def signature():
    K = ephemeralKeyFinder(p)
    local_r = op1.powerCal(g, K, p)
    message = int('A3FB8FCE', 16) % p
    # Not using my own power function here because it doesn't support inverse modulation
    local_s = ((message - (d * local_r)) * pow(K, -1, p - 1)) % (p - 1)
    return message, local_r, local_s


def verify():
    t = op1.powerCal(beta, r, p) * op1.powerCal(r, s, p) % p
    test = op1.powerCal(g, m, p)
    if t == test:
        return True
    return False


def ephemeralKeyFinder(U):
    result = 0
    while result != 1:
        random_integer = random.randint(1, U - 2)
        result = computeGCD(random_integer, U - 1)
    return random_integer


def computeGCD(X, Y):
    while Y:
        X, Y = Y, X % Y
    return X


def obligPrint():
    print("\nThe public key is (prime, generator, beta): ")
    print("Prime:", p)
    print("Generator:", g)
    print("beta:", beta)

    print("\nThe message can be represented as an integer mod p. This message is:", m)
    print("The signature (Message, (r, s):")
    print("r:", r)
    print("s:", s)

    if (verified):
        print("The signature was verified")
    else:
        print("The signature was not verified")


if __name__ == '__main__':
    # We first have the setup phase where we define a large prime (p), pic a generator (g), choose d and compute β.
    # This gives us the public key
    p, g, beta, d = setup()

    # Then we have the signature phase. Here we pick an ephemeral key that we only use during the signing. Then we
    # compute r and s. And together we have the signed message (m, (r, s)).
    m, r, s = signature()

    # And to verify we can use the following equation to check if they are equal.
    # t = β^r * r^s (mod p) & t = g^x (mod p)
    verified = verify()

    # Printing information about the variables
    obligPrint()


