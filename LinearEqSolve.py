from math import *
from operator import eq
from sympy import symbols, Eq, solve
from tkinter import *
from tkinter import ttk

from sympy.core import sympify

x = symbols("x")
op = ["+", "-", "*", "/"]

def calculate(*args):
    lhs = linear.get()
    rhs = equals.get()

    equation = Eq(sympify(lhs), sympify(rhs))
    result = solve(equation, x)

    answer.set(f"x = {result[0]}")




root = Tk()
root.title("Linear Algebra Solver")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="N, W, E, S")

linear = StringVar()
linear_entry = ttk.Entry(mainframe, width=7, textvariable=linear)
linear_entry.grid(column=2, row=1 , sticky="W, E")

answer = StringVar()
ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky="W, E")

ttk.Button(mainframe, text="calculate", command=calculate).grid(column=3, row=3, sticky="W")

ttk.Label(mainframe, text=linear).grid(column=3, row=1, sticky="W")
ttk.Label(mainframe, textvariable="equals").grid(column=1, row=2, sticky="E")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

linear_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
