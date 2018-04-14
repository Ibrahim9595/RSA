from inverse import inverse
from square_multiply import modular_pow

# Handle CRT Algorithm (get the modular exponent)
# @params y: int, d: int, p: int, q: int
# @return x: int
def CRT(y, d, p, q):
    n = p*q

    # 1- Convert to CRT domain 
    yp = y % p
    yq = y % q
    # print("(yp, yq) = ", str((yp, yq)))

    # 2- Do the computations
    dp = d % (p-1)
    dq = d % (q-1)
    # print("(dp, dq) = ", str((dp, dq)))

    xp = pow(yp, dp, p)
    xq = pow(yq, dq, q)
    # print("(xp, xq) = ", str((xp, xq)))

    # 3- Inverse transform
    inv = inverse(p, q)
    print(inv)
    cp = pow(q, p-2, p)
    cq = pow(p, q-2, q)
    # print(cq == pow(p, q-2, q))
    # print("(cp, cq) = ", str((p, q)))

    x = ((q*cp*xp) + (p*cq*xq)) % n
    # print("x = ", x, "mod " + str(n))
    return x