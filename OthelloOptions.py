##from tkinter import *
##
##master = Tk()
##
##v = IntVar()
##
####Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
####Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)
##
from tkinter import *

root = Tk()
var = IntVar()

MODES = [4, 6, 8, 10, 12, 14, 16]

##v = StringVar()
##v.set("L") # initialize


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   return var.get()

for num in MODES:
    b = Radiobutton(root, text=str(num),
                    variable=var, value=num, command = sel)
    b.pack(anchor=W)





##R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
##                  command=sel)
##R1.pack( anchor = W )
##
##R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
##                  command=sel)
##R2.pack( anchor = W )
##
##R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
##                  command=sel)
##R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
root.destroy()
