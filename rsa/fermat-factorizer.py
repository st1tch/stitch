import gmpy2
import sys

n = int(sys.argv[1], 16)

a = gmpy2.isqrt(n) + 1
b2 = a * a - n

while not gmpy2.is_square(b2):
    a = a + 1
    b2 = a * a - n

b = gmpy2.isqrt(b2)

p = a + b
q = a - b

print("p =", p)
print("q =", q)
