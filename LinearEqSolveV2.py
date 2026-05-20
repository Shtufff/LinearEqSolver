#Imports all the required packages.
from sympy import symbols, Eq, solve, sympify
from tkinter import *
from tkinter import ttk

#Tells sympify that x is a maths symbol and not the actual letter x.
x = symbols("x")

#Calc function for getting the left and right side of the equation and solving it.
#Takes user input from both left and right side, via TKinters .get method.
def calc(*args):
     lhs = left_side.get()
     rhs = right_side.get()

#Starts a equation, using sympify to convert lhs and rhs into maths.
     equation = Eq(sympify(lhs), sympify(rhs))
     result = solve(equation, x)

#Not gonna lie, not sure what this does, I found it in the sympify docs and it works, I think its say x = the result variable, then pulling x from a list. X being in positon 0 in that list?
     answer.set(f"x = {result[0]}")

#Starts TKinter and assigns it a title.
root = Tk()
root.title("Linear Algebra Solver")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="N, W, E, S")

#Allows for user input of the left and right side of the equation.
left_side = StringVar()
right_side = StringVar()
answer = StringVar()

#Positions and sizes the text boxs, and buttons in the GUI.
ttk.Entry(mainframe, textvariable=left_side).grid(column=0, row=0)
ttk.Label(mainframe, text="=").grid(column=1, row=0)
ttk.Entry(mainframe, textvariable=right_side).grid(column=2, row=0)
ttk.Label(mainframe, textvariable=answer).grid(column=1, row=2)

#Positions the calculate button, and tells it what function to run on press.
ttk.Button(mainframe, text="Calculate", command=calc).grid(column=1, row=1)

#When the user presses the enter key, run the calc function
root.bind("<Return>", calc)

#Starts TKinter GUI and keeps it open.
root.mainloop()

