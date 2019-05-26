import os
from pwn import *

while True:
    try:
        log.info("wait 9989")
        s = process(['nc', '-lvp', '9989'])
        try:
            while True:
                print s.recvline()
        except Exception as e:
            print e
        finally:
            log.failure("close 9989")
            s.close()
    except:
        s.close()
        break

