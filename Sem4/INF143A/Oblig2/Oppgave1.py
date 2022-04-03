
def isEven(n):
    if n % 2 == 0:
        return True
    return False


def calculation(b, p):
    b %= 100
    extra = []
    while p > 20:
        if isEven(p):
            p = p // 2
            b = b ** 2 % 100
        else:
            p = p // 2
            extra.append(b)
            b = b ** 2 % 100

    b = b ** p % 100

    for i in range(len(extra)):
        b = b * extra[i] % 100

    print("The last two integers of this exponent is:", b)


if __name__ == '__main__':
    base = 987654321
    power = 12345678987654321
    print("The base is: ", base)
    print("The power is:", power)
    calculation(base, power)

