from struct import *

p = lambda x:pack("<L", x)		#pack
up = lambda x:unpack("<L", x)[0]	#unpack

a = p(0xaabbccdd)
b = p(0x11223344)

print a
print repr(a)

print b
print repr(b)

a = up(a)
b = up(b)

print hex(a)
print hex(b)

