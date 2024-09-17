from tkinter import * 
from tkinter.filedialog import * 
from tkinter import messagebox


#fonctions 
my_address_book = {}

def open_file():
    global my_address_book
    open_file = askopenfile(mode = "r")
    if open_file is not None:
        my_address_book = eval(open_file.read())
        for key in my_address_book.keys():
            listbox.insert(END, key)
    else:
        messagebox.showwarning("WARNING", "No address book selected")

def save_file():
    global my_address_book
    save_file = asksaveasfile()
    if save_file:
        print(my_address_book, file = save_file)
        reset()
    else:
        messagebox.showwarning("WARNING", "Adress book not saved")

def reset():
    global my_address_book
    clear_all()
    listbox.delete(0, END)
    my_address_book.clear()

def clear_all():
    name_entry.delete(0, END)


window = Tk()
window.title("Adress Book")
window.geometry("500x500")


#entry + listbox
listbox = Listbox(window, width = 26, height = 20)
listbox.grid(row = 2, column = 1, rowspan = 5, columnspan = 2, pady = 10, padx = 10)
name_entry = Entry(window, width = 15).grid(row = 2, column = 4)
address_entry = Entry(window, width = 15).grid(row = 3, column = 4)
mobile_entry = Entry(window, width = 15).grid(row = 4, column = 4)
email_entry = Entry(window, width = 15).grid(row = 5, column = 4)
birthday_entry = Entry(window, width = 15).grid(row = 6, column = 4)


#labels
title = Label(window, text = "My address book:", font = ("times", 20)).grid(row = 1, column = 1)
name_label = Label(window, text = "Name:", font = ("times", 20)).grid(row = 2, column = 3)
adress_label = Label(window, text = "Address:", font = ("times", 20)).grid(row = 3, column = 3)
mobile_label = Label(window, text = "Mobile:", font = ("times", 20)).grid(row = 4, column = 3)
email_label = Label(window, text = "Email:", font = ("times", 20)).grid(row = 5, column = 3)
birthday_label = Label(window, text = "Birthday:", font = ("times", 20)).grid(row = 6, column = 3)


#buttons
edit_button = Button(window, text = "Edit", font = ("times", 17)).grid(row = 7, column = 1, pady = 10)
delete_button = Button(window, text = "Delete", font = ("times", 17)).grid(row = 7, column = 2)
open_button = Button(window, text = "Open", font = ("times", 17)).grid(row = 1, column = 3)
update_button = Button(window, text = "Update/Add", font = ("times", 17)).grid(row = 7, column = 4)
save_button = Button(window, text = "Save", font = ("times", 17), width = 23).grid(row = 8, column = 1, columnspan = 2)


window.mainloop()