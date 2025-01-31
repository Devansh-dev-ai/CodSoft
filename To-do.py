from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import Font
import pickle

window = Tk()
window.title("To-Do List")
window.geometry("440x400")

text_font = Font(
    family="Freestyle Script Regular",
    size=10
)

frame = Frame(window, padx=20, pady=20)
frame.pack()

user_list = Listbox(
    frame,
    height=10,
    width=50,
    bg="SystemButtonFace",
    font= text_font,
    highlightthickness=0,
    activestyle="none",
)
user_list.pack(side=LEFT, fill=BOTH, expand=True)

# Create dummy list
# my_list = ["Learn tkinter"]
# for item in my_list:
#     user_list.insert(END, item)

# Add Scrollbar
my_scrollbar = Scrollbar(frame)
my_scrollbar.pack(side=RIGHT, fill=Y)
user_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=user_list.yview)

# Entry box
user_entry_box = Entry(window, width=50)
user_entry_box.pack(pady=20)

# Create functions
def delete_item():
    user_list.delete(ANCHOR)
def add_item():
    user_list.insert(END,user_entry_box.get())
    user_entry_box.delete(0,END)
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir = "E:/Tkinter_Python/data",
        title = "Save file",
        filetypes = (("txt",'.txt'),
                     ("All file","*.*")
                    ),
    )
    if file_name:
        if file_name.endswith("txt"):
            pass
        else:
            file_name = f"{file_name}.txt"
    # Graf all the stuff from the list
    stuff = user_list.get(0,END)
    # Open the file
    output_file = open(file_name,'wb')
    # Actually add the stuff
    pickle.dump(stuff,output_file)
def open_list():
    file_name = filedialog.askopenfilename(
        initialdir = "E:/Tkinter_Python/data",
        title = "Open file",
        filetypes = (("txt",'.txt'),
                     ("All file","*.*")
                    ),
        )
    if file_name:
        user_list.delete(0,END)
        input_file = open(file_name,"rb")
        stuff = pickle.load(input_file)
        for item in stuff:
            user_list.insert(END,item)
def clear_list():
    user_list.delete(0,END)

# Create Menu
user_menu = Menu(window)
window.config(menu= user_menu)
file_menu = Menu(user_menu,tearoff= False)
user_menu.add_cascade(label = "menu",menu = file_menu)

# Add dropdown items
file_menu.add_command(label = "Save", command = save_list)
file_menu.add_command(label = "Open", command = open_list)
file_menu.add_separator()
file_menu.add_command(label = "Clear", command = clear_list)


# Add buttons
create_frame_button = Frame(window)
create_frame_button.pack()

delete_button = Button(create_frame_button,text="Delete",command= delete_item).grid(row=0,column=0)
add_button = Button(create_frame_button,text="Add",command= add_item).grid(row=0,column=1,padx=20)



window.mainloop()
