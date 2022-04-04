
def isEven(n):
    if n % 2 == 0:
        return True
    return False


def powerCal(b, p, m):
    b %= m
    extra = []
    while p > 20:
        if isEven(p):
            p = p // 2
            b = b ** 2 % m
        else:
            p = p // 2
            extra.append(b)
            b = b ** 2 % m

    b = b ** p % m

    for i in range(len(extra)):
        b = b * extra[i] % m

    return b


if __name__ == '__main__':
    base = 987654321
    power = 12345678987654321
    print("The base is: ", base)
    print("The power is:", power)
    print("The last two integers of this exponent is:", powerCal(base, power, 100))

