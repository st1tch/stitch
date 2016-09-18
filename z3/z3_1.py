from z3 import *

n = 43

b = [ i for i in range(n**2) ]

for i in range(len(b)) :
	b[i] = Int('b[%d]'%i)

result = [0] * n**2

s = Solver()

arr_b = [147, 154, 140, 171, 179, 165, 150, 145, 152, 140, 131, 134, 159, 172, 171, 151, 169, 164, 148, 134, 160, 159, 161, 156, 154, 133, 140, 140, 140, 154, 156, 148, 142, 156, 149, 136, 138, 121, 153, 154, 124, 146, 139]
arr_a = [164, 165, 132, 172, 159, 145, 144, 163, 139, 144, 155, 145, 168, 139, 165, 150, 147, 145, 159, 135, 155, 150, 168, 152, 152, 139, 145, 155, 139, 158, 149, 116, 155, 132, 161, 155, 155, 152, 144, 133, 171, 142, 122]


for i in range(n) :
	j = i*n
	s.add(sum(b[j:j+n])==arr_a[i])
	s.add(sum(b[i:i+n*(n-1)+1:n])==arr_b[i])

for i in range(n**2) :
	s.add(b[i] >= 1)
	s.add(b[i] <= 9)

print s.check()
m = s.model()
#m.decls()[0].name()
#m[s.model().decls()[0]]

#1 (rand sequence)
for d in m.decls() :
	print d.name(), m[d]

#2 (in regular sequence)
for i in range(n**2) :
	print i, m[b[i]]

#3 (perfect regular sequence and save)
for d in m.decls() :
	_i, _v = int(d.name().strip('b[]')), str(m[d])
	result[_i] = _v

print result


