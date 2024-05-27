from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital_Clock")



def time():
    String  = strftime('%H:%M:%S %P')
    label.config(text=String)
    label.after(1000,time)



label = Label(root, font = ("ds-digital",80), background="black",foreground="green")
label.pack(anchor='center')


time()
mainloop()
