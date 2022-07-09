
from calendar import c
from cmath import exp
from tkinter import *

expression = " "
#function to update expression
def click(n):
    global expression
    expression = expression + str(n)
    equation.set(expression)

#function to evaluate the final expression
def equal():
    try:
        global expression
        result = str(eval(expression))
        equation.set(expression+"="+result)
        expression = " "
    except ZeroDivisionError:
        equation.set("Error")

#function to clear the content
def clear():
    global expression
    expression = " "
    equation.set("")
#create gui window
window=Tk()
window.title("Calculator")
window.geometry("500x500")
equation = StringVar()
#expression field    
t1=Entry(window,textvariable=equation)
t1.grid(columnspan=4, ipadx=70)
#entries
#numbers
b1=Button(window,text="1",width=20,height=2,command=lambda: click(1))
b1.grid(row=2,column=0)
b2=Button(window,text="2",width=20,height=2,command=lambda: click(2))
b2.grid(row=2,column=1)
b3=Button(window,text="3",width=20,height=2,command=lambda: click(3))
b3.grid(row=2,column=2)
b4=Button(window,text="4",width=20,height=2,command=lambda: click(4))
b4.grid(row=3,column=0)
b5=Button(window,text="5",width=20,height=2,command=lambda: click(5))
b5.grid(row=3,column=1)
b6=Button(window,text="6",width=20,height=2,command=lambda: click(6))
b6.grid(row=3,column=2)
b7=Button(window,text="7",width=20,height=2,command=lambda: click(7))
b7.grid(row=4,column=0)
b8=Button(window,text="8",width=20,height=2,command=lambda: click(8))
b8.grid(row=4,column=1)
b9=Button(window,text="9",width=20,height=2,command=lambda: click(9))
b9.grid(row=4,column=2)
b0=Button(window,text="0",width=20,height=2,command=lambda: click(0))
b0.grid(row=5,column=1)
#clear button
cancel=Button(window,text="clear",width=20,height=2,command=clear)
cancel.grid(row=5,column=0)
#buttons for operations
plus=Button(window,text="+",width=20,height=2,command=lambda: click("+"))
plus.grid(row=2,column=3)
minus=Button(window,text="-",width=20,height=2,command=lambda: click("-"))
minus.grid(row=3,column=3)
product=Button(window,text="x",width=20,height=2,command=lambda: click("x"))
product.grid(row=4,column=3)
divide=Button(window,text="/",width=20,height=2,command=lambda: click("/"))
divide.grid(row=5,column=3)
equalto=Button(window,text="=",width=20,height=2,command=equal)
equalto.grid(row=5,column=2)


window.mainloop()
