from tkinter import *
from tkinter import ttk
import math


window = Tk()
window.title("Calculator")
display = Entry(window,bg = "white", width=30,borderwidth=3)
display.grid(row=0,column=0,columnspan=5,padx=1,pady=20)

def ButtonClicked(number):
    current = display.get()
    display.delete(0,END)
    display.insert(0,str(current)+str(number))
    
def ClearClicked():
    display.delete(0,END)

def operator(operate):
    global FirstNumber, operation
    operation = operate
    FirstNumber = display.get()
    display.delete(0,END)

def DisplayResult():
    SecondNumber = display.get()
    display.delete(0,END)
    # print("\n\n\n\n\n\n")
    if operation == "+":
        add = float(FirstNumber),float(SecondNumber)
        display.insert(0,sum(add))
    elif operation == "-":
        subtraction = float(FirstNumber) - float(SecondNumber)
        display.insert(0,subtraction)
    elif operation == "X":
       display.insert(0,float(FirstNumber)*float(SecondNumber))
    elif operation == "/":
        display.insert(0,float(FirstNumber)/float(SecondNumber))
    else:
        display.insert(0,(float(FirstNumber)/float(SecondNumber))*100)
    
       
CleanAll = Button(window,text="C",padx=40,pady=10,command=ClearClicked)
PiButton = Button(window,text = "Pi",padx=49,pady=10,command=lambda:ButtonClicked(3.14))
CleanAll.grid(row=2,column=0),PiButton.grid(row=2,column=3)


num0 = Button(window,text="0",padx=40,pady=10, command=lambda:ButtonClicked(0))
num1 = Button(window,text="1",padx=40,pady=10, command=lambda:ButtonClicked(1))
num2 = Button(window,text="2",padx=40,pady=10, command=lambda:ButtonClicked(2))
num3 = Button(window,text="3",padx=40,pady=10, command=lambda:ButtonClicked(3))
num4 = Button(window,text="4",padx=40,pady=10, command=lambda:ButtonClicked(4))
num5 = Button(window,text="5",padx=40,pady=10, command=lambda:ButtonClicked(5))
num6 = Button(window,text="6",padx=40,pady=10, command=lambda:ButtonClicked(6))
num7 = Button(window,text="7",padx=40,pady=10, command=lambda:ButtonClicked(7))
num8 = Button(window,text="8",padx=40,pady=10, command=lambda:ButtonClicked(8))
num9 = Button(window,text="9",padx=40,pady=10, command=lambda:ButtonClicked(9))

num7.grid(row=3,column=0),num8.grid(row=3,column=1),num9.grid(row=3,column=2)
num4.grid(row=4,column=0),num5.grid(row=4,column=1),num6.grid(row=4,column=2)
num1.grid(row=5,column=0),num2.grid(row=5,column=1),num3.grid(row=5,column=2)
num0.grid(row=6,column=0)


DotButton = Button(window,text=".",padx=41,pady=10,command=lambda:ButtonClicked("."))
PercentageButton = Button(window,text="%",padx=39,pady=10,command=lambda:operator("%"))
AddButton = Button(window,text="+",padx=49,pady=10,command=lambda:operator("+"))
SubtractButton = Button(window,text="-",padx=51,pady=10,command=lambda:operator("-"))
MultiplyButton = Button(window,text="X",padx=40,pady=10,command=lambda:operator("X"))
DivisionButton = Button(window,text="/",padx=40,pady=10,command=lambda:operator("/"))
ResultButton = Button(window,text="=",padx=51.4,pady=32, comman=lambda:DisplayResult())

DivisionButton.grid(row=2,column=2)
MultiplyButton.grid(row=2,column=1)
ResultButton.grid(row=5,column=3,rowspan=2)
DotButton.grid(row=6,column=1),PercentageButton.grid(row=6,column=2),AddButton.grid(row=4,column=3)
SubtractButton.grid(row=3,column=3)


window.mainloop()