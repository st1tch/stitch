import angr
p = angr.Project('FUck_binary')
ex = p.surveyors.Explorer(find=0x403a23)
ex.run()
print ex.found[0].state.posix.dumps(0)
print ex.found[0].state.posix.dumps(1)
