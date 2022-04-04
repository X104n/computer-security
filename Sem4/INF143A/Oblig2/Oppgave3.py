import Oppgave2


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


if __name__ == '__main__':
    n = 15151

    e = 17

    c = 832

    primeList = findPrimes(n)

    p = primeList[0]
    q = primeList[1]

    phi = (p-1)*(q-1)

    d = 0

    for i in range(2, n):
        if (i * e) % phi == 1:
            d = i
            break
    print(d)
    print(phi)

    print(decrypt(d, c, n))
