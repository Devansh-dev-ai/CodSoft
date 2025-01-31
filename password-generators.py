import random
from tkinter import *
from tkinter import ttk
import string

window = Tk()
heading = Label(window, text="Password Generator")
heading.pack()

frame = Frame(window, padx=10, pady=20)
frame.pack()
result = Label(window,text= "Generated password")
result.pack()

UserInputFrame = Entry(frame, width=50)
UserInputFrame.grid(row=0, column=0, columnspan=2)

number = string.ascii_letters + string.digits + string.punctuation

def password_generator_fun():
    UserInput = UserInputFrame.get()
    try:
        length = int(UserInput)
        random_character = random.choices(number, k=length)
        a = "".join(random_character)
        print(length, "\n\n")
        print(random_character)
        global result
        result.destroy()
        result = Label(window,text=f"{a}")
        result.pack()
        # result.config(text=f"{a}")

    except ValueError:
        result.destroy()
        result = Label(window,text="Invalid input. Please enter a valid number.")
        result.pack()

def CopyPassword():
    frame.clipboard_clear()
    frame.clipboard_append(result.cget("text"))

SubmitButton = Button(frame, text="Submit",  command=password_generator_fun)
copy_button = Button(frame, text="Copy Output", command=CopyPassword)
copy_button.grid(row=1, column=1), SubmitButton.grid(row=1, column=0)
window.mainloop()
