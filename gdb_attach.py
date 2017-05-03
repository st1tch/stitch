#!/usr/bin/env python

from pwn import *

context.log_level = 'debug'

IS_LOCAL = True
RAND_IMG_BASE = False

BIN = './binary'
b = ELF(BIN)

if IS_LOCAL:
	LIBC = ''
	l = ELF(LIBC)
	#/lib/x86_64-linux-gnu/libc-2.23.so'
	#'/lib/i386-linux-gnu/libc-2.23.so'
else :
	HOST = ''
	PORT = 44444
	LIBC = ''
	l = ELF(LIBC)

def get_image_base(s):
		pid = proc.pidof(s)[0]
		proc_path = '/proc/%s/maps' % pid

		with open(proc_path, 'r') as f:
				image_base = f.read().split('\n')[0].split('-')[0]

		image_base = int(image_base, 16)
		return image_base

def get_bp_str(s, bp_l):
	bp_str = ''

	if RAND_IMG_BASE:
		image_base = get_image_base(s)
		for i in range(len(bp_l)):
			bp_l[i] += image_base
	
	for bp in bp_l:
		bp_str += 'b *' + hex(bp) + '\n'
	return bp_str

def end_menu():
	print 'end_menu func'

if __name__ == '__main__':
	if IS_LOCAL:
		s = process(BIN)
		#image_base = get_image_base(s)
		bp_l = []
		bp_str = get_bp_str(s,bp_l)

		gdb.attach(s,'''
		%s
		c''' % (bp_str))
		#display /4xg addr
	else:
		s = remote(HOST,PORT)

	end_menu()
	
	s.interactive()
