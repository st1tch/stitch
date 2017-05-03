import re


def grep(s,pattern):
    return '\n'.join(re.findall(r'^.*%s.*?$'%pattern,s,flags=re.M))

def grep(s,pattern):
    return re.findall(r'^.*%s.*?$'%pattern,s,flags=re.M)


a = ' 80484f7:\t68 bf 92 04 08       \tpush   0x80492bf\n'
re.findall('0x[\w]{6,8}', a)[0]
re.search('0x[\w]{6,8}', a).group(0)
