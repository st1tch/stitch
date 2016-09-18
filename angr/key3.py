import angr

proj = angr.Project('test', load_options={'auto_load_libs' : False})

path_group = proj.factory.path_group(threads=4)

path_group.explore(find=0x4006CB, avoid=0x4006D7)

print path_group.found[0]
print path_group.found[0].state.posix.dumps(1)
