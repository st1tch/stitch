import angr

p = angr.Project("./test")

s = p.factory.blank_state(addr = 0x400616 ) #check function start addr
serial = s.se.BVS("serial", 32*8)
s.memory.store(0x601050, serial) # store some symbolic memory in the bss
s.regs.rdi = 0x601050 # let the first arguemnt(rdi) point to it

pg = p.factory.path_group(s)
pg.explore(find = 0x4006CB) # mov correct string

# Find out what to give as input to reach this state. (Solve it like a TI-89, please?)
print "Serial is: %r" % pg.found[0].state.se.any_str(serial).strip("\x00")
