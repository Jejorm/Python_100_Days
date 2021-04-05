import pyperclip
import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
              ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    join = join_entry.get()
    password = password_entry.get()
    model = f"{website} | {join} | {password}\n"

    if len(website) == 0 or len(join) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail/User: {join} "
                                                              f"\nPassword: {password} \n\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file_object:
                file_object.write(model)

            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = tk.PhotoImage(file="logo.png")

canvas = tk.Canvas()
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

join_label = tk.Label(text="Email/Username:")
join_label.grid(column=0, row=2)

join_entry = tk.Entry(width=35)
join_entry.insert(0, "example@email.com")
join_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = tk.Button(text="Add", width=36)
add_button.config(command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
