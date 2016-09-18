import angr

b = angr.Project('./test')
s = b.factory.blank_state(addr=0x400616)    #check function start addr
v = s.se.BVS('key', 15*8)
s.memory.store( 0x601050, v ) #temp memory
s.regs.rdi=0x0000000000601050
initpath = b.factory.path(state=s)
ex = b.surveyors.Explorer( start=initpath, find=(0x4006CB)) #mov Correct string
ex.run()

print ex.found[0].state.se.any_str( ex.found[0].state.memory.load(0x601050, 13))
