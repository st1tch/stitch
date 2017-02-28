import angr # angr-5.6.8.22
import simuvex

p = angr.Project("./FUck_binary")
state = p.factory.entry_state()

key_length = 300
key = state.se.BVS(name="key", size=key_length*8)
for i in range(key_length):
    c = key[i*8+7 : i*8]
    state.se.add(0x20 <= c)
    state.se.add(c != 0x7e)
state.se.simplify()

class read(simuvex.SimProcedure):
    def run(self, fd, buf, count):
        self.state.memory.store(buf, key)
p.hook_symbol('read', read)

get_flag = 0x403a23
goodbye = 0x4051f1
pathgroup = p.factory.path_group(state)
pathgroup.explore(find=get_flag, avoid=goodbye)

for path in pathgroup.found:
    print repr(path.state.se.any_str(key))
