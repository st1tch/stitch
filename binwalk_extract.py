import sys
import os

def main() :
    del_empty = lambda x : x != ''
    dict_ = {}
    try :
        binwalk = open(sys.argv[2], 'r').read().split('\n')[3:-1]
    except :
        assert 0, 'first binwalk execute!'
    for i in range(len(binwalk)-1):
        if (i != len(binwalk)-1) :
            cur_ = list(filter(del_empty, binwalk[i].split(' ')))
            next_ = list(filter(del_empty, binwalk[i+1].split(' ')))
            if cur_[2] in dict_ :
                dict_[cur_[2]] += 1
            else :
                dict_[cur_[2]] = 1
                os.system('mkdir %s'%(cur_[2].lower()))
            of = 'out' + str(dict_[cur_[2]]) + '_' + cur_[0] + '.' + cur_[2].lower()
            skip = cur_[0]
            try :
                count = str(int(next_[0])-int(cur_[0]))
                extract(sys.argv[1], of, skip, count)
            except :
                os.system('dd if=%s of=%s bs=1 skip=%s'%(sys.argv[1], of, skip))
            finally :
                os.system('mv %s %s'%(of, cur_[2].lower()))
    output = ''
    output += '--------------------------FINISH--------------------------\n'
    for i in dict_.keys() :
        output += '%s file -> %d\n'%(i, dict_[i])
    print output
    open('output.txt', 'w').write(output)

def extract(*args) :
    default = 'dd if=%s of=%s bs=1 skip=%s count=%s'%(args[0], args[1], args[2], args[3])
    print default
    os.system(default)

if __name__ == '__main__':
    main()
