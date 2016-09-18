import os
import sys

c = 'file * | grep -i ' + sys.argv[1] + ' > list'
os.system(c)
s = open('list', 'rb').read()
cnt = len(s.split('\n')[:-1])

for i in range(cnt) :
	c = 'mv \'' + s.split('\n')[i].split(' ')[0][:-1] + '\' ' + str(i) + '.' + sys.argv[1]
	os.system(c)

os.system('rm list')

