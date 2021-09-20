
'''
def MouseWheelHandler(event):
    global count

    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1 
        return 1 

    count += delta(event)
    print(count)

import tkinter
root = tkinter.Tk()
count = 0
root.bind("<MouseWheel>",MouseWheelHandler)
# root.bind("<Button-4>",MouseWheelHandler)
# root.bind("<Button-5>",MouseWheelHandler)
root.mainloop()
'''

from tkinter import *
root = Tk()
root.geometry("400x400")
def scrolllistbox(event):
    ''' scrolling both listbox '''
    print(event.delta)
    listbox2.yview_scroll(int(-1*(event.delta/120)), "units")
    listbox1.yview_scroll(int(-1*(event.delta/120)), "units")


def random_insert():
    ''' adding some numbers to the listboxes '''
    for i in range(100):
        listbox1.insert(END, i)
        listbox2.insert(END, i + 100)

# SCROLLBAR
scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

# LISTBOX 1
listbox1 = Listbox(root)
listbox1.pack()


# attach listbox to scrollbar with yscrollcommand
# listbox1.config(yscrollcommand=scrollbar.set)

# The second one
listbox2 = Listbox(root)
listbox2.pack()
listbox2.config(yscrollcommand=scrollbar.set)
# scroll the first one when you're on the second one
# listbox2.bind("<MouseWheel>", scrolllistbox)
root.bind("<MouseWheel>", scrolllistbox)

# scroll also the second list when you're on the first
listbox1.bind("<MouseWheel>", scrolllistbox)

random_insert()
#scrollbar.config(command=listbox.yview)

root.mainloop()


