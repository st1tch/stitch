#!/usr/bin/env python

import angr

p = angr.Project('test')

key_str = angr.StringSpec(sym_length=20)
initial_state = p.factory.entry_state(args=['./test', key_str])
pg = p.factory.path_group(initial_state)

# find_addr should be adjusted to the basic block that prints 'win.'
find_addr = 0x4005f6
pg.explore(find=find_addr)
if hasattr(pg, 'found'):
    print 'yay'
    fs = pg.found[0].state
    key = fs.se.any_str(key_str)
    print key
    #-------------
    #print fs.se.any_str(fs.memory.load(fs.regs.rdi,20))
    #-------------
    #argv_loc = fs.mem[fs.regs.rbp-0x10].qword.resolved
    #argv1_loc = fs.mem[argv_loc+0x8].qword.resolved
    #print fs.se.any_str(fs.memory.load(argv1_loc, 20))
else:
    print 'nope.'
