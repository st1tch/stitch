import os
import sys

def user_add(user, debug=''):
    os.system('useradd {} -m -s /bin/bash {}'.format(user, debug))
    os.system('chown root:{} /home/{} {}'.format(user, user, debug))
    os.system('chmod 750 /home/{} {}'.format(user, debug))
    print '[+] {} user add successful!'.format(user)

def set_passwd(user, debug=''):
    os.system('passwd {} < set_passwd {}'.format(user, debug))
    print '[*] {} passwd set successful!'.format(user)

def user_del(user, debug=''):
    os.system('userdel -r {} {}'.format(user, debug))
    os.system('rm -rf /home/{} {}'.format(user, debug))
    print '[-] {} user delete successful!'.format(user)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'select option -add, -del'
        sys.exit(0)
    try:
        user_list = open('user_list', 'rb').read()
    except:
        print 'make user_list first!'
        sys.exit(0)
    open('set_passwd', 'wb').write('abcde\nabcde\n')
    for user in [i for i in user_list.split('\n') if i != '']:
        if sys.argv[1] == '-add':
            user_add(user, '2>/dev/null')
            set_passwd(user, '2>/dev/null')
        elif sys.argv[1] == '-del':
            user_del(user, '2>/dev/null')
        else:
            print 'incorrect option'
            sys.exit(0)
    os.system('rm -rf ./set_passwd')
