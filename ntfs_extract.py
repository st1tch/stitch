import os

#vhd file read
vhd = open('./NTFS_Recovery.vhd', 'rb').read()
#boot code
offset = 2099200 * 512
#mft number
l = [37, 41, 42, 43, 44, 45, 46, 47]

f_idx = 1
for idx in l:
    s_idx = offset + ((idx*2) * 512)
    dat = vhd[s_idx:s_idx+1024]
    dat = [i for i in dat]
    ss_idx = ''.join(dat).index('\x80\x00\x00\x00\x48\x00\x00\x00')
    size_ = int(''.join(dat[ss_idx+56:ss_idx+64][::-1]).encode('hex'), 16)
    print 'size =', size_
    tmp = dat[ss_idx+64].encode('hex')
    range_ = int(tmp[0]) + int(tmp[1])
    tmp = dat[ss_idx+64 : ss_idx+64+range_+1]
    tmp2 = ''.join(tmp).encode('hex')
    file_offset = int((''.join(tmp[-int(tmp2[0]):][::-1])).encode('hex'), 16)
    print 'offset =', file_offset
    start_ = ((file_offset*8) + 2048) * 512
    end_ = start_ + size_
    output = vhd[start_:start_+end_]
    filename = 'output_{0}'.format(str(f_idx))
    open(filename, 'wb').write(output)
    print '%d clear!'%(f_idx)
    f_idx += 1


