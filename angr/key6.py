import angr

START_ADDR = 0x00000000004028d9
AVOID_ADDR = 0x0000000000402941
FIND_ADDR = 0x000000000040293f
BASE_ADDR = 0x7fffffffe5c0
STACK_ADDR = 0x7fffffffe560
INPUT_ADDR = 0x7fffffffe560
INPUT_LENGTH = 13

p = angr.Project('baby-re')
state = p.factory.blank_state(addr=START_ADDR)
state.regs.rbp = BASE_ADDR
state.regs.rsp = STACK_ADDR

for i in range(INPUT_LENGTH):    
      s = state.se.BVS('Var[{}]'.format(i), 32, explicit_name=True)      
     state.memory.store(INPUT_ADDR + i * 4, s)   

path = p.factory.path(state)
ex = p.surveyors.Explorer(start=path, find=(FIND_ADDR,), avoid=(AVOID_ADDR,0x00000000004025e0))
ex.run()

print "The Flag: " + ex.found[0].state.posix.dumps(1)
