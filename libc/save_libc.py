#save_libc.py
import os
import sys

path = '/home/stitch/stitch/libc/'
data = ''
try :
	if open(sys.argv[1], 'rb').read()[4] == '\x01' :
		bit = 0	#32bit
	else :
		bit = 1	#64bit
except :
	print 'format error => python this.py path_libc'
	sys.exit(0)

def add(name, addr) :
	global data
	if name == '' or addr == '' :
		return
	else :
		data += name
		data += '#'
		data += str(addr)
		data += '\n'

def remove_null(s) :
	s = s.split(': ')[1].split(' ')
	return [i for i in s if i != '']

#binsh addr save
def binsh() :
	tmp = os.popen('strings -a -t x %s | grep /bin/sh'%sys.argv[1]).read()
	binsh = tmp.strip().split(' ')[0]
	add('binsh', binsh)

#main_ret addr save
def main_ret() :
	tmp = open(sys.argv[1], 'rb').read()
	#64bit
	if bit :
		main_ret = tmp.find('\xff\xd0\x89\xc7') + 2
		poprdi_ret = hex(tmp.find('\x5f\xc3')).lstrip('0x')
		add('poprdi_ret', poprdi_ret)
	#32bit
	else :
		main_ret = tmp.find('\xff\x54\x24\x70') + 4
	main_ret = hex(main_ret).lstrip('0x')
	add('main_ret', main_ret)

#libc addr save
def libc_addr() :
	tmp = os.popen('readelf -s %s'%sys.argv[1]).read().split('\n')[3:-1]
	for i in tmp :
		data = remove_null(i)
		if (data[2] == 'FUNC') or (data[2] == 'IFUNC') :
			add(data[6].split('@')[0], data[0].lstrip('0'))

if __name__ == '__main__' :
	filename = sys.argv[1].split('/')[-1]
	if bit :
		filename = '64_' + filename + '.list'	#64bit
	else :
		filename = '32_' + filename + '.list'	#32bit
	f = open(path + filename, 'wb')
	libc_addr()
	binsh()
	main_ret()
	f.write(data)
	f.close()
	print '[Success] Create %s '%(path+filename)


