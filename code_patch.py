from pwn import *

def first(pay):
    dat = open('leo', 'rb').read()
    dat = list(dat)

    start = 0x1c9e
    end = 0x1f31

    for i in range(start, end):
        dat[i] = '\x90'

    for idx, d in enumerate(pay):
        dat[start+idx] = d
    
    return dat

def second(dat):
    start = 0x13cf
    end = 0x185e

    for i in range(start, end):
        dat[i] = '\x90'

    pay = '\x55\x48\x89\xe5\x48\x89\x7d\xd8\x89\x75\xd4\x8b\x45\xd4\x89\xc2\xc1\xea\x1f\x01\xd0\xd1\xf8\x83\xc0\x01\x89\x45\xf8\xc7\x45\xfc\x11\x00\x00\x00\xc7\x45\xfc\x00\x00\x00\x00\xeb\x35\x8b\x45\xd4\x89\xc2\xc1\xea\x1f\x01\xd0\xd1\xf8\x83\xc0\x01\x3b\x45\xf8\x74\x02\xeb\x28\x8b\x45\xfc\x48\x63\xd0\x48\x8b\x45\xd8\x48\x01\xd0\x0f\xb6\x00\x89\xc2\x8b\x45\xfc\x48\x98\x88\x54\x05\xe0\x83\x45\xfc\x01\x8b\x45\xfc\x3b\x45\xd4\x7c\xc3\x90\x5d\xc3'.encode('hex').decode('hex')

    for idx, d in enumerate(pay):
        dat[start+idx] = d

    dat = ''.join(dat)
    open('test.edit','wb').write(dat)

def make_opcode():
    tmp = '''

    '''
    pay = asm(tmp, arch='amd64', os='linux')
    return pay

if __name__ == '__main__':
    pay = make_opcode()
    dat = first(pay)
    fourd(dat)
