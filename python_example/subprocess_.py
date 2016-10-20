import subprocess

password = 'sHow_Me_The_Your_Passw0rd'
ttmp = ['./crackme']

for i in range(9000, 10030) :
    argv = ttmp + ['a'] * i
    s = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    s.stdin.write(password+'\n')
    sleep(0.01)
    s.stdin.write(password+'\n')
    tmp = s.stdout.read()
    if 'Invalid' in tmp :
        s.kill()
    else :
        print tmp
        s.communicate()
        break


subprocess.check_output(args, *, input=None, output=None, stderr=None, shell=False, timeout=None)


