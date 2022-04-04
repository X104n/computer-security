import Isiy_koum_omh_hrobtvv_tk_Heigv_Mlvcqyzrj
import random
import Oppgave1 as op1


def isPrime(a, p):
    calc = op1.powerCal(a, p, p) - a
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
    # Should lower this here to test the code
    for j in range(1000000):
        r = random.randint(2, p - 1)
        if not isPrime(r, p):
            return False
    return True


def findPrime(d):
    # Finding the lower and higher bound of all the integers with d bits
    lower_bound = int(generate(d), 2)
    higher_bound = int(generate(d + 1), 2)

    # Setting our first prime to test at the lower bound, and we go up until we reach the higher bound
    prime = lower_bound
    for i in range(lower_bound, higher_bound):
        if testIfPrime(prime):
            return prime
        prime += 1
    return None


if __name__ == '__main__':
    # Go to testIfPrime function and lower the for loop to 100 or 1000 to test the code. Kept it high to show that it
    # needs to run a couple of times to make sure it is a prime number
    print("A prime of 500 bits:", findPrime(500))
    print("A prime of 671 bits:", findPrime(671))
    print("A prime of 1024 bits:", findPrime(1024))
