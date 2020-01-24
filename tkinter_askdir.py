from tkinter.filedialog import askopenfilename , askdirectory



def askdir():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filedir = askdirectory() # show an "Open" dialog box and return the path to the selected directory
    return filedir
