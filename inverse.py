# Handle extended eculidian algorithm
# @params ra: int, rb: int
# @return rb^-1: int or -1 (in case of no inverse)
def inverse(ra, rb):
    if rb > ra:
        ra, rb = rb, ra

    modulos = ra
    mult = [(1, 0), (0, 1)]
    i = 2
    while True:
        # print(str(ra) + " = " + str(rb) + "*", end='')
        mod = ra % rb
        q = (ra - mod) // rb
        # print(str(q)+" + " + str(mod))
        ra = rb
        rb = mod
        mult = [
            (mult[1][0], mult[1][1]),
            ((-q * mult[1][0]) + mult[0][0],  (-q * mult[1][1]) + mult[0][1])
        ]
        if mod == 0:
            # print("GCD = " + str(ra))
            if ra == 1:
                return mult[0][1] % modulos
            else:
                return -1
            break
        # else:
            # print("R" + str(i) + " = " + str(mult[1][0]) + " * R" + str(i-2) + " + " + str(mult[1][1]) + " * R" + str(i-1))
