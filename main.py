from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')']
nr_letters = random.randint(6, 8)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password_input.delete(0, END)
    Password_letters = [random.choice(letters) for _ in range(nr_letters)]
    Password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    Password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    Password_list = Password_letters + Password_numbers + Password_symbols
    random.shuffle(Password_list)

    password = "".join(Password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_input.get()
    username_data = username_input.get()
    password_data = password_input.get()
    new_data = {
        website_data: {
            "Username/Email": username_data,
            "Password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make Sure you haven't left any field Empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # data_file.write(f"{website_data} | {username_data} | {password_data}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- Search PASSWORD ------------------------------- #
def search_password():
    website_data = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No data File Found")
    else:
        if website_data in data:
            website = data[website_data]
            username = website["Username/Email"]
            password = website["Password"]
            messagebox.showinfo(website_data, f"Email: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(website_data, f"No Data Available for Website: {website_data}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
password_manager_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager_image)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_input = Entry(width=22)
website_input.grid(row=1, column=1)
website_input.focus()

username_input = Entry(width=41)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "prajapatidurgesh1518@gmail.com")

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()
