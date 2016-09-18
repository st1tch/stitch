import simuvex
import angr

p = angr.Project('abc')

key_str = angr.StringSpec(sym_length=20)
initial_state = p.factory.entry_state(args=['abc', key_str])
pg = p.factory.path_group(initial_state, immutable=False)

# find_addr should be adjusted to the basic block that prints 'win.'
find_addr = 0x40291F
pg.explore(find=find_addr)
if hasattr(pg, 'found'):
    print 'yay'
    fs = pg.found[0].state
    # flag should be 'this_is_a_test'
    print fs.se.any_str(fs.memory.load(fs.regs.rdi,20))
else:
    print 'nope.'
