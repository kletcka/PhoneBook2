from tkinter import * 
from tkinter.ttk import * 
import commands
def create_object(name="", pos=[0,0], ob_type=None, size=1, id=None, g_id=0):
        if ob_type == "Entry":
            t=Entry(width=size*15)
            commands.fulling(id, t)
            return    (t, pos, id),         (Label(text=name), [pos[0], pos[1]+21], id)
        elif ob_type == "Button":
            o = ((Button(text=name, width = size*15, command=lambda g_i=g_id: commands.result(g_i)), pos),)
            return o
            