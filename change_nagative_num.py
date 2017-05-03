
def dec2hex(n):
    r = hex(n & 0xffffffff)
    return r

#only input nagative hex
def hex2dec(n):
    r = 0xffffffff-n
    r += 1
    r *= -1
    return r

hex2dec = lambda a : -(a^0xffffffff)-1 if a&(1<<31) else a
hex2dec = lambda a : (0x100-(0xff&a))*-1
