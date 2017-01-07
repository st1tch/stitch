from z3 import *
A = BitVec('A', 32)
B = BitVec('B', 32)
C = BitVec('C', 32)
D = BitVec('D', 32)

eax = BitVec('eax', 32)
ecx = BitVec('ecx', 32)
edx = BitVec('edx', 32)
edi = BitVec('edi', 32)
esi = BitVec('esi', 32)
r8d = BitVec('r8d', 32)
r9d = BitVec('r9d', 32)
r10d = BitVec('r10d', 32)
r11d = BitVec('r11d', 32)
r14d = BitVec('r14d', 32)

# Basically the initial block of the code translated to Python & Z3.
eax = A
edx = C
esi = eax
r9d = B
r11d = edx
r10d = D
r8d = r10d
r14d = edx & BitVecVal(0xffff, 32)
edx = r9d
edi = eax & BitVecVal(0xffff, 32)
eax = r14d
esi = esi >> 0x10
eax = eax ^ esi
r11d = r11d >> 0x10
edx = edx >> 0x10
r8d = r8d >> 0x10
ecx = r9d & BitVecVal(0xffff, 32)
r9d = r10d & BitVecVal(0xffff, 32)

lower_limit = 0x20
upper_limit = 0x7e

s = Solver()
s.add(
    # The rest of the blocks translated as conditions.
    eax == 0x2633,
    r14d+esi == 0xa6cb,
    r11d^edi == 0x535c,
    r11d+edi == 0x939C,
    r9d^edx == 0x0103,
    r9d+edx == 0xC993,
    r8d^ecx == 0x066f,
    r8d+ecx == 0xE68F,
    (r9d * BitVecVal(4, 32) + ecx + BitVecVal(0x13, 32)) ^
    (edx + BitVecVal(0x37, 32) + r8d) == 0x2D231,

    # And some limits to get ASCII flag.
    (A & 0xff) >= lower_limit, (A & 0xff) <= upper_limit,
    (B & 0xff) >= lower_limit, (B & 0xff) <= upper_limit,
    (C & 0xff) >= lower_limit, (C & 0xff) <= upper_limit,
    (D & 0xff) >= lower_limit, (D & 0xff) <= upper_limit,

    ((A >> 8) & 0xff) >= lower_limit, ((A >> 8) & 0xff) <= upper_limit,
    ((B >> 8) & 0xff) >= lower_limit, ((B >> 8) & 0xff) <= upper_limit,
    ((C >> 8) & 0xff) >= lower_limit, ((C >> 8) & 0xff) <= upper_limit,
    ((D >> 8) & 0xff) >= lower_limit, ((D >> 8) & 0xff) <= upper_limit,

    ((A >> 16) & 0xff) >= lower_limit, ((A >> 16) & 0xff) <= upper_limit,
    ((B >> 16) & 0xff) >= lower_limit, ((B >> 16) & 0xff) <= upper_limit,
    ((C >> 16) & 0xff) >= lower_limit, ((C >> 16) & 0xff) <= upper_limit,
    ((D >> 16) & 0xff) >= lower_limit, ((D >> 16) & 0xff) <= upper_limit,

    ((A >> 24) & 0xff) >= lower_limit, ((A >> 24) & 0xff) <= upper_limit,
    ((B >> 24) & 0xff) >= lower_limit, ((B >> 24) & 0xff) <= upper_limit,
    ((C >> 24) & 0xff) >= lower_limit, ((C >> 24) & 0xff) <= upper_limit,
    ((D >> 24) & 0xff) >= lower_limit, ((D >> 24) & 0xff) <= upper_limit,    
)

print s.check()
m = s.model()

res = [
    int(str(m.evaluate(A))),
    int(str(m.evaluate(B))),
    int(str(m.evaluate(C))),
    int(str(m.evaluate(D)))
]

oo = ""
for x in res:
  o = hex(x)[2:].decode("hex")[::-1]
  print hex(x), o
  oo += o

print oo

