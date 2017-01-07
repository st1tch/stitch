s = open('pay.bin','rb').read()
l = []
for i in s:
    l.append(i)

def convt(x):
    tmp = hex(ord(x))[2:]
    if len(tmp) == 1:
        return '\\x0'+tmp
    else:
        return '\\x'+tmp
print ''.join(map(convt, l))
