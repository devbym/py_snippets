#### Quick TKinter fileselector ####

from tkinter.filedialog import askopenfilename


def askfilename():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename # return path to file as a string or empty string if none selected
