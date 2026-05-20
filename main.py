from math import *
from tkinter import *
from tkinter import ttk

var1 = int(input("Enter the first number: "))
var2 = int(input("Enter the second number: "))


def calculate(*args):














dsdsds

root = Tk()
root.title("Linear Algebra Solver")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="N, W, E, S")

linear = StringVar()
linear_entry = ttk.Entry(mainframe, width=7, textvariable=linear)
linear_entry.grid(column=2, row=1 , sticky="W, E")

answer = StringVar()
ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky="W, E")

ttk.Button(mainframe, text="Solve", command="calculate").grid(column=3, row=3, sticky="W")

ttk.Label(mainframe, text=linear).grid(column=3, row=1, sticky="W")
ttk.Label(mainframe, textvariable="equals").grid(column=1, row=2, sticky="E")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

linear_entry.focus()
root.bind("<return>", calculate)

root.mainloop()
