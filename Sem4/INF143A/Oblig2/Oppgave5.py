from itertools import product

import sys

def xor(v1,v2):
    result = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        result.append(b)
    return result


def multiplication(A, B, irr):
    result = []
    for i in range(len(A)):
        result.append(0)

    for i in range(len(A)):
        if B[i] == 1:
            shift = A
            for s in range(i):
                do_we_have_overflow = (shift[-1] == 1)
                shift = [0] + shift[:-1]
                if do_we_have_overflow:
                    shift = xor(shift, irr)
            result = xor(result, shift)
    return result


def function(x, poly):
    temp = multiplication(x, x, poly)
    return multiplication(temp, x, poly)


def generateTT(poly):
    dict = {

    }
    myList = list(product([0, 1], repeat = len(poly)))
    for j in range(len(myList)):
        myList[j] = list(myList[j])

    for i in range(len(myList)):
        print(i)
        dict[str(myList[i])] = function(myList[i], poly)

    return dict


if __name__ == '__main__':
    poly4 = [1, 1, 0, 0]
    poly5 = [1,0,1,0,0]
    poly6 = []
    print(generateTT(poly4))
    print(generateTT(poly5))
    print(generateTT(poly6))