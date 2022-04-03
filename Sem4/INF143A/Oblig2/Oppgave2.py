from random import random, randint


def isPrime(a, p):
    calc = (pow(a, p, p)-a)
    if calc % p == 0:
        return True
    else:
        return False


def generate(n):
    result = ""
    for k in range(n):
        if k == 0:
            result += "1"
        else:
            result += "0"
    return result


def testIfPrime(p):
    for j in range(1000):
        if not isPrime(j, p):
            return False
    return True


if __name__ == '__main__':
    d = 500
    myPrime = False
    lower = int(generate(d), 2)
    prime = lower
    higher = int(generate(d+1), 2)
    for i in range(lower, higher):
        if testIfPrime(prime):
            myPrime = True
            break
        prime += 1
    print(prime)
    print(myPrime)
