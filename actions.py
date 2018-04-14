from get_prime import get_rand_prime
from random import randrange
from inverse import inverse
from square_multiply import modular_pow
from CRT import CRT

# Handle RSA Initialization
# @params nbits: int
# @return RSAParams: {p: int, q: int, phi: int, e: int, d: int}
def setup(nbits=512):
    p = get_rand_prime(nbits)
    q = get_rand_prime(nbits)
    while p == q:
        q = get_rand_prime(nbits)
    n = p * q
    phi = (p-1) * (q-1)
    e = randrange(2**16, 2**17)
    d = inverse(phi, e)
    while d == -1:
        e = randrange(2**16, 2**17)
        d = inverse(phi, e)

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d
    }

# Handle encryption Action
# @params msg: int, e: int, n: int
# @return encrypted_msg: int
def do_encryption(msg, e, n):
    return modular_pow(msg, e, n)

# Handle decryption Action
# @params msg: int, e: int, n: int
# @return decrypted_msg: int
def do_decryption(msg, d, p, q):
    return CRT(msg, d, p, q)