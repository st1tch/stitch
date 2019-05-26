from os import *
import sys

try:
    PORT = sys.argv[1]
    EXEC = sys.argv[2]

    op = 'while true; do socat TCP-LISTEN:%s,reuseaddr EXEC:%s ; sleep 1; done'%(sys.argv[1], sys.argv[2])

    system(op)
except:
    print 'usage : mysocat PORT EXEC'
