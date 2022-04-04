import Isiy_koum_omh_hrobtvv_tk_Heigv_Mlvcqyzrj
from itertools import product


def xor(v1, v2):
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
    dict = {}
    myList = list(product([0, 1], repeat=len(poly)))
    for j in range(len(myList)):
        myList[j] = list(myList[j])

    for i in range(len(myList)):
        dict[str(myList[i])] = function(myList[i], poly)

    return dict


def printDictionary(d):
    for key, value in d.items():
        print(key, " | ", value)


if __name__ == '__main__':
    # Test poly
    poly3 = [1, 1, 0]

    # Here are the polynomials that I'm using. They were found using magma (See screenshot in image folder)
    poly4 = [1, 1, 0, 0]
    poly5 = [1, 0, 1, 0, 0]
    poly6 = [1, 1, 0, 1, 1, 0]

    print("\nTest truth table for n = 3")
    printDictionary(generateTT(poly3))

    print("\nTruth table for n = 4")
    printDictionary(generateTT(poly4))

    print("\nTruth table for n = 5")
    printDictionary(generateTT(poly5))

    print("\nTruth table for n = 6")
    printDictionary(generateTT(poly6))
