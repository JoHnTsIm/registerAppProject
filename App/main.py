import string
from tkinter import *
from tkinter import ttk, filedialog, messagebox, Tk, Checkbutton
import random
import os
from sys import platform
import datetime
import calendar


# creates a sequence of numbers equal to the max days that can one month have
# and insert them into a list
# then returns the list
def generate_day_list_():
    day_list = [""]
    for i in range(1, 31 + 1, 1):
        day_list.append(i)
    return list(day_list)


# creates a list with the names of all the months of a year
# and returns the list
def generate_month_list():
    month_list = [i for i in calendar.month_name]
    return list(month_list)


# creates a list with all the years from the 1800 until now
# and returns the list
def generate_year_list():
    year_list = [""]
    current_year = datetime.datetime.now().date().strftime("%Y")
    for i in range(int(current_year),  1800-1, -1):
        year_list.append(i)
    return list(year_list)


# creates a list with a number sequence from 1 to 30
# and returns the list
def generate_30_num_list():
    num_list = [i for i in range(1, 31, 1)]
    return list(num_list)


# creates the random password
def generate_random_password():
    random_password = ""
    all_characters = string.printable.replace("", "").replace('"', '').strip()
    all_characters += " "

    while len(random_password) < int(password_len_combobox.get()):
        random_char = random.randint(0, 93)
        random_password += all_characters[random_char]
    random_password_fixed = random_password.replace(" ", "(space)")
    password_entry.delete(0, END)
    password_entry.insert(END, random_password_fixed)


# throw's a pop up window to select save location
def select_save_location():
    desktop = ""
    if platform == "linux" or platform == "linux2":
        desktop = os.path.join(os.path.join(os.path.expanduser('~/Desktop')))
    elif platform == "win32":
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    save_location = filedialog.askdirectory(initialdir=desktop,
                                            title="Select Save Location for Register text file")
    if save_location:
        return save_location


# writes the user typed info to the text file and throw's a 'Registered Successfully' message
def write_text_to_file_and_save():
    save_location = select_save_location()
    if save_location:
        save_location = save_location + f"/{file_name_entry.get()}.txt"
        with open(save_location, "w") as file:
            file.write(
                f"First Name: {first_name_entry.get()}\n\n"
                f"Last Name: {last_name_entry.get()}\n\n"
                f"Username: {username_entry.get()}\n\n"
                f"Date_of_Birth: {day_combobox.get()}/{month_combobox.get()}/{year_combobox.get()}\n\n"
                f"Email: {email_entry.get()}\n\n"
                f"Phone: {phone_entry.get()}\n\n"
                f"Password: {password_entry.get()}"
            )
            file.close()
            messagebox.showinfo(title="Successful", message="Registered Successfully")


# starts the 'write_text_to_file_and_save' function
def register():
    write_text_to_file_and_save()


# copy's the current typed password to the clipboard
def copy_password():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(str(password_entry.get()))
    r.destroy()


# show's the current typed or generated password
def show_password():
    if var1.get() == 0:
        password_entry.config(show="*")
    elif var1.get() == 1:
        password_entry.config(show="")


# crates the window and sets basic properties
window = Tk()
window.title("RegistrationApp")
window.config(bg="#333")
window.iconbitmap("icon/register-icon.ico")

# window not resizeable
window.resizable(False, False)

'''Center the window to the screen'''
width = 530  # Width
height = 580  # Height

screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))

entry_frame = Frame(bg="#333")
entry_frame.pack()

# ---------------------------------------

app_title_label = Label(entry_frame, text="RegistrationApp", bg="#333", fg="white", font="Eccentric 30")
app_title_label.grid(column=1, row=0, columnspan=4, pady=15)

# ---------------------------------------

first_name_label = Label(entry_frame, text="First Name", bg="#333", fg="white", font="Verdana 11")
first_name_label.grid(column=1, row=1)

first_name_entry = Entry(entry_frame, font="Verdana 11")
first_name_entry.grid(column=2, row=1, pady=10)

# ---------------------------------------

last_name_label = Label(entry_frame, text="Last Name", bg="#333", fg="white", font="Verdana 11")
last_name_label.grid(column=1, row=2)

last_name_entry = Entry(entry_frame, font="Verdana 11")
last_name_entry.grid(column=2, row=2, pady=10)

# ---------------------------------------

username_label = Label(entry_frame, text="Username", bg="#333", fg="white", font="Verdana 11")
username_label.grid(column=1, row=3)

username_entry = Entry(entry_frame, font="Verdana 11")
username_entry.grid(column=2, row=3, pady=10)

# ----------------------------------------

date_of_birth_label = Label(entry_frame, text="Date of birth", bg="#333", fg="white", font="Verdana 11")
date_of_birth_label.grid(row=4, column=1)

day_combobox = ttk.Combobox(entry_frame, width=2, height=10)
day_combobox.grid(column=2, row=4, padx=10, ipady=1, sticky="w", pady=10)
day_combobox['values'] = (generate_day_list_())
day_combobox.set(1)

month_combobox = ttk.Combobox(entry_frame, width=10, height=10)
month_combobox.grid(column=2, row=4, ipady=1, sticky="w", padx=65)
month_combobox['values'] = (generate_month_list())
month_combobox.set("January")

year_combobox = ttk.Combobox(entry_frame, width=4, height=10)
year_combobox.grid(column=2, row=4, ipady=1, sticky="e", padx=10)
year_combobox['values'] = (generate_year_list())
year_combobox.set("2022")

# ----------------------------------------

email_label = Label(entry_frame, text="Email", bg="#333", fg="white", font="Verdana 11")
email_label.grid(column=1, row=5)

email_entry = Entry(entry_frame, font="Verdana 11")
email_entry.grid(column=2, row=5, pady=10)

# ----------------------------------------

phone_label = Label(entry_frame, text="Phone", bg="#333", fg="white", font="Verdana 11")
phone_label.grid(column=1, row=6)

phone_entry = Entry(entry_frame, font="Verdana 11")
phone_entry.grid(column=2, row=6, pady=10)

# ----------------------------------------

password_label = Label(entry_frame, text="Password", bg="#333", fg="white", font="Verdana 11")
password_label.grid(column=1, row=7)

password_entry = Entry(entry_frame, font="Verdana 11", show="*")
password_entry.grid(column=2, row=7)


password_len_combobox = ttk.Combobox(entry_frame, width=3, height=10)
password_len_combobox.grid(column=3, row=7, padx=7, ipady=1)
password_len_combobox['values'] = (generate_30_num_list())
password_len_combobox.set(10)

password_generate_button = Button(entry_frame, text="Generate Random", bg="#4169e1", fg="white",
                                  font="Arial 10", bd=0, command=generate_random_password)
password_generate_button.grid(column=4, row=7, pady=10, padx=1)

# ----------------------------------------

password_copy_button = Button(entry_frame, text="Copy password", command=copy_password, bg="#666", fg="white")
password_copy_button.grid(column=1, columnspan=2, row=8)

var1 = IntVar()
show_password_checkbutton = Checkbutton(entry_frame, text="Show password", fg="orange", bg="#333",
                                        variable=var1, onvalue=1, offvalue=0, command=show_password)
show_password_checkbutton.grid(column=2, row=8, sticky="e")

# ----------------------------------------

file_name_label = Label(entry_frame, text="File's Name", bg="#333", fg="orange", font="Verdana 12")
file_name_label.grid(column=1, row=9)

file_name_entry = Entry(entry_frame, font="Verdana 11")
file_name_entry.grid(column=2, row=9, pady=25, padx=10)

# ----------------------------------------

register_button = Button(window, text="Select Location &\nRegister",
                         fg="white", bg="#ffa40c", font="Dustismo_Foxman 16", command=register)
register_button.pack(pady=10)


window.mainloop()
