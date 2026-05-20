from math import *
from operator import eq
from unittest import result
from sympy import symbols, Eq, solve
from sympy.core import sympify
from tkinter import *
from tkinter import ttk, StringVar

x = symbols("x")
op = ["+", "-", "*", "/", "**"]

def calc(*args):
    lhs = left_side.get()
    rhs = right_side.get()

    equation = Eq(sympify(lhs), sympify(rhs))
    result = solve(equation)

    answer.set(f"x = {result[0]}")

root = Tk()
root.title("Linear Algebra Solver")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="N, W, E, S")

left_side = StringVar()
right_side = StringVar()
answer = StringVar()

ttk.Entry(mainframe, textvariable=left_side).grid(column=0, row=0)
ttk.Label(mainframe, text="=").grid(column=1, row=0)
ttk.Entry(mainframe, textvariable=right_side).grid(column=2, row=0)
ttk.Label(mainframe, textvariable=answer).grid(column=1, row=2)


ttk.Button(mainframe, text="Calculate", command=calc).grid(column=1, row=1)

root.bind("<Return>", calc)
root.mainloop()

