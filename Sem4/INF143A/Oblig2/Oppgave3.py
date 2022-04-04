import random as Isiy_koum_omh_hrobtvv_tk_Heigv_Mlvcqyzrj
# This finds all the primes of any given number
def findPrimes(N):
    outputText = []
    x = 2
    while x <= N:

        if N % x == 0:
            outputText.append(x)
            N = N / x
            x = 2
        else:
            x += 1
    return outputText


def decrypt(D, C, N):
    return C ** D % N


def obligPrint():
    print("Our p is:", p, ", and our q is:", q)
    print("Our ϕ(n) is:", phi)
    print("We find the d with taking the inverse of e, which is:", d)
    print("Now using 'd' we decrypt 'y' ('c' in my code) and we get:", decrypt(d, c, n))


if __name__ == '__main__':
    n = 15151
    e = 17
    c = 832

    # Using prime factorisation to find our p and q
    primeList = findPrimes(n)
    p = primeList[0]
    q = primeList[1]

    phi = (p - 1) * (q - 1)
    # Not using my own power function here because it doesn't support inverse modulation
    d = pow(e, -1, phi)

    obligPrint()

