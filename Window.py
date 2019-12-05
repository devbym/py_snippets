import csv
from tkinter import messagebox, Tk, ttk , filedialog , Button , Label , Menu

infile = []
s = []

specs = {
    "BE":  ["P" , "1001"],
    "LU" : ["P", "1601" , "1001"],
    "IT" : ["P", "1601"],
    "DE" : ["p", "1601"],
    "NO" : ["P", "1601"],
    "SE" : ["P" , "999", "4"]
    }

countries = list(specs.keys())


def combo_select():
    x = combobox.get()
    if combobox.get() in countries:
        s = specs.get(combobox.get())
    s = tuple(s)
    return s


def ask_file():
    while len(infile) == 0:
        d = filedialog.askopenfile(mode='r',title="Pick a file")
        if not d.name.endswith("txt"):
            messagebox.showinfo("Error", "Select a textfile")
            break
        infile.append(d)
    else:
        infile.clear()
    return d.name

def ffilter(infile = infile, chars=s):
    li = []
    with open("Myfile.csv", 'w') as outfile:
        wr = csv.writer(outfile, dialect='excel', delimiter=",",lineterminator="\n")
        for line in infile:
            if line.startswith(chars):
                li.append(line)
                print(line)
        for i in li:
            i = i.split()
            wr.writerows(i)
    print(li)

#ROOT
root = Tk()
root.title("File cleaner")
root.geometry('200x300')
#TOPFRAME
frame = ttk.Frame(root, padding=(10,10))
frame.grid(row=0, column=0)
label = ttk.Label(frame, text="Pick a country and select a file \n Click process to continue")
combobox = ttk.Combobox(frame, values=countries ,text="Country")
button = ttk.Button(frame, text="Browse file..." , command=ask_file)
button1 = ttk.Button(frame, text="Add", command=combo_select)
button2 = ttk.Button(frame, text="Process", command=ffilter)
label.grid(row=0, column=0)
combobox.grid(row=1,column=0)
button1.grid(row=2,column=0)
button.grid(row=3, column=0)
button2.grid(row=4, column=0)
combobox.bind("<<ComboboxSelected>>")

# ROOT
menubar = Menu(root)

#TOP Menu
filemenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)


def open_help():
    pass

def open_about():
    messagebox.showinfo("About", " Version 0.2 \n Written by: \n Devbym")

def open_settings():
    sett = ttk.Frame(root)
    testbt = ttk.Button(sett,text="Run tests", command='tests')
    testbt.pack(sett)

#TOP LEVEL ITEMS
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)
#CHILD LEVEL ITEMS
helpmenu.add_command(label='Help', command=open_help)
helpmenu.add_command(label='About', command=open_about)
filemenu.add_command(label='Settings', command=open_settings)
filemenu.add_command(label='Quit', command=root.destroy)

root.config(menu = menubar)
root.mainloop()

##  Testing  ##

def tests():
    pass

