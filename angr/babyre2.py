import angr
import subprocess

i = '1'

cmd = "file prob{}".format(i)
dat = subprocess.check_output(cmd, shell=True)

if '32-bit' in dat:
    bit = 32
else:
    bit = 64

if bit==32:
    cmd = "objdump -S -M intel prob{} | grep jne".format(i)
    dat = subprocess.check_output(cmd, shell=True)
    target = int(dat.split('\n')[2].split()[0].strip(':'), 16) + 2

    proj = angr.Project('./prob{}'.format(i), load_options={"auto_load_libs": False})
    initial_state = proj.factory.entry_state()
    path_group = proj.factory.path_group(initial_state)
    path_group.explore(find=0x4025cc)

if bit==64:
    cmd = "objdump -S -M intel prob{} | grep jne".format(i)
    dat = subprocess.check_output(cmd, shell=True)
    target = int(dat.split('\n')[5].split()[0].strip(':'), 16) + 2

    proj = angr.Project('./prob{}'.format(i), load_options={"auto_load_libs": False})
    initial_state = proj.factory.entry_state()
    path_group = proj.factory.path_group(initial_state)
    path_group.explore(find=target)

found = path_group.found[0]
print found.state.se.any_str(found.state.memory.load(found.state.regs.rbp, 200))
