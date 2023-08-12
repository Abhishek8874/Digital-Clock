#importing modules
from tkinter import *
from time import strftime

root=Tk()# create tkinter window
root.title("Digitl Clock") # adding title on the clock

#function is used to dispaly time on screeen
def time():
    string = strftime('%H: %M: %S %p')
    lbl.config(text=string)
    lbl.after(1000,time)

#styling the clock
lbl = Label(root, font=("arial", 160, 'bold'), bg='black', fg= 'red' )

#pack method to visit row and column
lbl.pack(anchor='center', fill= BOTH, expand=1)

time()

mainloop()

