from random import randrange
from square_multiply import modular_pow

# Handle analysing a prime to 2^u * r
# @params num: int(prime)
# @return (u, r)
def get_u_r(num):
    u = 0
    num -= 1
    
    while True:
        u += 1
        num //= 2
        if u != 0 and num % 2 != 0:
            break
    
    return (u, num)



# Handle testing the primality of a number
# @params p: int, s: int
# @return isPrime: bool
def miller_rabin(p, s):
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    u, r = get_u_r(p)
    for i in range(s):
        a = randrange(2, p - 1)
        z = modular_pow(a, r, p)

        if z != 1 and z != (p - 1):
            for j in range(u):
                z = modular_pow(z, 2, p)
                if z == p - 1:
                    break
            else:
                return False
                
    return True


# Handle generating a prime_number of nbits long
# @params nbits: int
# @return p: int(prime)
def get_rand_prime(nbits=16):
    while True:
        p = randrange(2**nbits, 2*2**nbits)
        # print(p)
        if miller_rabin(p, 100):
            return p