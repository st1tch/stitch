from z3 import *
from pwn import *

global conn

def solver() :
	conn.recvuntil('PROB', drop=False)
	print "start!"
	conn.recvline()
	n = int(conn.recvline().split(' : ')[1].split('\n')[0])
	arr_b = map(int, (conn.recvline().split(' : ')[1].split('\n')[0]).strip('[]').split(', '))
	arr_a = map(int, (conn.recvline().split(' : ')[1].split('\n')[0]).strip('[]').split(', '))
	#-------------------------------------------------------------------------------

	b = [0] * (n**2)
	result = [0] * (n**2)

	for i in range(len(b)) :
		b[i] = Int('b[%d]'%i)

	s = Solver()

	for i in range(n) :
		j = i*n
		s.add(sum(b[j:j+n])==arr_a[i])
		s.add(sum(b[i:i+n*(n-1)+1:n])==arr_b[i])

	for i in range(n**2) :
		s.add(b[i] >= 1)
		s.add(b[i] <= 9)

	s.check()
	m = s.model()
	for d in m.decls() :
		_i, _v = int(d.name().strip('b[]')), str(m[d])
		result[_i] = _v

	submit = ''
	for i in range(len(result)) :
		if (i % n == 0) and (i != 0) :
			submit += "|"
		submit += result[i]
	submit += '\n'

	conn.send(submit)
	print "send!!"

#-----main
conn = remote('grr.nadeko.moe', 10002)
cnt = 0
while True:
	try :
		solver()
		cnt+=1
		print "#",cnt,"_Clear!!!!\n"
		if cnt == 20 :
			break
	except :
		print conn.recv()
		conn.close()
		conn = remote('grr.nadeko.moe', 10002)
		cnt = 0
		continue

flag = conn.recvuntil('\n', drop=False)
print flag
print conn.recv()
conn.close()




