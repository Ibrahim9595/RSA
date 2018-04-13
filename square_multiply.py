def squareAndMultiply(b, p):
    n_bits = len(str(bin(p))) - 2
    res = b
    # print(n_bits)
    for i in range(n_bits - 2, -1, -1):
        print(i)
        res = res ** 2
        if p & (1 << i):
            res = res * b

    return res


def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    # Assert :: (modulus - 1) * (modulus - 1) does not overflow base
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result
