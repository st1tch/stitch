import angr

b = angr.Project('./test')
e = b.surveyors.Explorer(find=0x4006CB)
e.run()

if len(e.found) > 0:
    print "%r" % e.found[0].state.posix.dumps(4)
