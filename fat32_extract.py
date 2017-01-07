import os

os.system('mkdir output')

#vhd file read
vhd = open('./1.vhd', 'rb').read()

ss = open('input.txt', 'r').read().split()
s = [ [] for i in range(len(ss) / 32)]

for i in range(len(ss)):
    s[i/32].append(ss[i])

idx = 1
for i in s:
    if i[0xb] == '20':
        offset = ''.join(i[0x14:0x16][::-1]) + ''.join(i[0x1a:0x1c][::-1])
        size = ''.join(i[0x1c:][::-1])
        type_ = ''.join(i[0x08:0xb]).decode('hex')

        offset = int(offset, 16)
        size = int(size, 16)

        if (offset == 0 or size == 0):
            continue
        if type_ == 'CRD':
            continue

        start_point = (((offset-2) * 8 ) + 16512) * 512
        tmp = vhd[start_point:start_point+size]
        file_name = str(idx) + '.' + type_
        open(file_name, 'wb').write(tmp)
        os.system('mv {0} output'.format(file_name))
        print 'offset = {0}, size = {1}, output = {2}'.format(offset, size, file_name)
        print 'clear!!'
        idx += 1


