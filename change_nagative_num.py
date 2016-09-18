
def dec2hex(n):
    r = hex(n & 0xffffffff)
    return r

#only input nagative hex
def hex2dec(n):
    r = 0xffffffff-n
    r += 1
    r *= -1
    return r


