from tkinter import *
from tkinter.ttk import *

selection = [""]

def callbackFunc(event):
     selection.pop()
     selection.append(combo.get())
     print(selection)

def _OK():
    window.destroy()

window = Tk() # Creates empty window object
window.title("Country picker")
combo = Combobox(window, values=["BE","IT","DE","FR"])
combo.grid(column=1, row=0 ,columnspan=2)
#combo.current(0)

label_Combobox = Label(window, text="Make a choice: ")
label_Combobox.grid(column = 0, row = 0)

#exit_button = Button(window,text="Exit", command=window.destroy )
#exit_button.grid(row=1, column=1 )

ok_button = Button(window,text="Ok", command=_OK )
ok_button.grid(row=2,column=2,sticky="E",padx=5,pady=5)

combo.bind("<<ComboboxSelected>>", callbackFunc)

#print(combo.current(), combo.get())
 
window.mainloop()
