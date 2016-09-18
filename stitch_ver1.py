import string
import os

p = lambda x : struct.pack('<I', x)
up = lambda x : struct.unpack('>I', x)[0]

printable = string.printable[:-6]


def dump_str(_input) :
	def padding(s) :
		if len(s) % 16 :
			s += "\x00" * (16 - ( len(s) % 16) )
		return s

	s = padding(_input)

	#print addr
	for addr in range(0x0, len(s), 0x10) :
		print '0x' + '0'*(10-len(str(hex(addr)))) + str(hex(addr))[2:] + '    ',
		#print hex value
		for s_hex in range(addr, addr+16) :
			tmp = str(hex(ord(s[s_hex])))[2:]
			if(len(tmp) == 1):
				print '0' + tmp + ' ',
			else :
				print tmp + ' ',
		#print ascii value
		print '  ',
		l = []
		for s_ascii in range(addr, addr+16) :
			if s[s_ascii] in printable :
				l.append(s[s_ascii])
			else :
				l.append('.')
		print ''.join(l)

msg = ''
def find_libc_sub(func1, func2, sub) :
	global msg
	def find(data, func1, func2, sub) :
		global msg
		data = data.split('\n')
		for _str in data :
			if len(_str) == 0 : continue
			func, addr = _str.split(' ')
			if func == 'system' :
				system = int(addr, 16)
			if func == 'execl' :
				execl = int(addr, 16)
			if func == 'str_bin_sh' :
				binsh = int(addr, 16)
			if func == func1 :
				addr1 = int(addr, 16)
			elif func == func2 :
				addr2 = int(addr, 16)
		if sub == str(abs(addr1 - addr2)) :
			msg += '-'*30 + '\n'
			msg += func1 + '=' + hex(addr1) + '\n'
			msg += func2 + '=' + hex(addr2) + '\n'
			msg += 'system=' + hex(system) + '\n'
			msg += 'binsh=' + hex(binsh) + '\n'
			msg += 'execl=' + hex(execl) + '\n'
			return 1
		else :
			return 0

	if type(sub) == int :
		sub = str(abs(sub))
	for root, dirs, files in os.walk('/home/stitch/tool/libc-database/db'):
		for file in files:
			if '.symbols' == file[-8:] :
				data = open( '/home/stitch/tool/libc-database/db/' + file, 'rb').read()
				if find(data, func1, func2, sub) :
					msg += 'libc=' + file[:-8] + '\n'
	tmp = msg
	msg = ''
	return tmp

def find_libc(input_func, three_byte) :
	global msg
	def find(input_func, data, three_byte) :
		global msg
		data = data.split('\n')
		for _str in data :
			if len(_str) == 0 : continue
			func, addr = _str.split(' ')
			if func == 'system' :
				system = int(addr, 16)
			if func == 'execl' :
				execl = int(addr, 16)
			if func == 'str_bin_sh' :
				binsh = int(addr, 16)
			if func == input_func :
				tmp = int(addr, 16)

		if three_byte == hex(tmp)[-3:] :
			msg += '-'*30 + '\n'
			msg += input_func + '=' + hex(tmp) + '\n'
			msg += 'system=' + hex(system) + '\n'
			msg += 'binsh=' + hex(binsh) + '\n'
			msg += 'execl=' + hex(execl) + '\n'
			return 1
		else :
			return 0

	for root, dirs, files in os.walk('/home/stitch/tool/libc-database/db'):
		for file in files:
			if '.symbols' == file[-8:] :
				data = open('/home/stitch/tool/libc-database/db/' + file, 'rb').read()
				if find(input_func, data, three_byte) :
					msg += 'libc=' + file[:-8] + '\n'

	tmp = msg
	msg = ''
	return tmp

def fsb(offset, addr_list, written) :
	payload = ''
	tmp = written
	default = '%NUMc%OFFSET$hn'
	for i in range(len(addr_list)) :
		addr = addr_list[i]
		addr_high = addr >> 16
		addr_low = addr & 0x0000ffff
		while (addr_low < tmp) :
			addr_low += 0x10000
		num1 = addr_low - tmp
		tmp += num1
		while (addr_high < tmp) :
			addr_high += 0x10000
		num2 = addr_high - tmp
		tmp += num2
		payload += default.replace('NUM',str(num1)).replace('OFFSET', str(offset))
		offset += 1
		payload += default.replace('NUM',str(num2)).replace('OFFSET', str(offset))
		offset += 1

	return payload, tmp     # tmp = written


if __name__ == '__main__' :
	print 'stitch'
