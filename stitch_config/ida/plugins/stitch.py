import idaapi
import idautils
import idc

class MyHandler(idaapi.action_handler_t):
    def __init__(self):
        idaapi.action_handler_t.__init__(self)

    def activate(self, ctx):
        COLOR = 0x39D38A
      	for ea in idautils.Heads():
            if idaapi.isCode(idaapi.getFlags(ea)) and idaapi.is_call_insn(ea):
                current_color = idaapi.get_item_color(ea)
                if current_color != idc.DEFCOLOR:
                    idaapi.set_item_color(ea, idc.DEFCOLOR)
                elif current_color == idc.DEFCOLOR:
                    idaapi.set_item_color(ea, COLOR) 
        print "Success Highlight!"
        return 1

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

action_desc = idaapi.action_desc_t(
    'stitch',   # The action name. This acts like an ID and must be unique
    'Highlighting!',  # The action text.
    MyHandler(),   # The action handler.
    'Ctrl+`',      # Optional: the action shortcut
    'Stitch\'s call highlighting',  # Optional: the action tooltip (available in menus/toolbar)
    199)           # Optional: the action icon (shows when in menus/toolbars)

idaapi.register_action(action_desc)
idaapi.attach_action_to_toolbar(
    "StitchHighlight",  # The toolbar name
    'stitch')        # The action ID
