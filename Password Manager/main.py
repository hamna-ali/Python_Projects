from random import choice, randint, shuffle
import pyperclip
from tkinter import messagebox
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    p_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = web_input.get()
    email = u_input.get()
    password = p_input.get()

    if website == "" or password == "":
        # Optional: show a warning if essential fields are empty
        messagebox.showinfo(title="Oops!",message="these field can't be empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are details entered:\n Email: {email}\n"
                                       f"Password: {password}\n Are these OK to enter")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            # Clear website and password fields after saving
            web_input.delete(0, END)
            p_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# ---------------------------- LOGO ------------------------------- #
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# ---------------------------- WEBSITE FIELD ------------------------------- #
web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0, sticky="e")  # align right
web_input = Entry(width=35,relief="solid", bd=1)
web_input.focus()
web_input.grid(row=1, column=1, columnspan=2, sticky="w")

# ---------------------------- USERNAME FIELD ------------------------------- #
user_label = Label(text="Email/Username:", bg="white")
user_label.grid(row=2, column=0, sticky="e")
u_input = Entry(width=35,relief="solid", bd=1)
u_input.insert(0, 'hamnaali435@gmail.com')
u_input.grid(row=2, column=1, columnspan=2, sticky="w")

# ---------------------------- PASSWORD FIELD ------------------------------- #
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky="e")
p_input = Entry(width=32,relief="solid", bd=1)
p_input.grid(row=3, column=1, sticky="w")

gp_button = Button(text="Generate Password",command=generate_password)
gp_button.grid(row=3, column=2, sticky="w")

# ---------------------------- ADD BUTTON ------------------------------- #
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=10, sticky="w")





window.mainloop()