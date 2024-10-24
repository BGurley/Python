from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ----- Find Password ----- #
def find_password():
    website = siteInput.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists")


# ------ Password Generator ----- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters +password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    pwInput.insert(0, password)
    pyperclip.copy(password)
    print("Generated Password copied!")

# ----- Save Password ----- #

def save():
    
    website= siteInput.get()
    email = emailInput.get()
    password = pwInput.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you havent left any fields empty")
    else: 
        is_ok = messagebox.showinfo(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                f"\nPassword: {password} \n Is it ok to save?")
        if is_ok: 
            try: 
                with open ("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updatung old data with new data
                data.update(new_data)

                with open ("data.json", "w") as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                siteInput.delete(0, END)
                emailInput.delete(0, END)
                pwInput.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Tomato Image Placement 
canvas = Canvas(width = 200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels #

# Website Label
siteLabel = Label(text="Website: ", font=("Arial", 10))
siteLabel.grid(column=0, row=1)

# Email/Username Label
eLabel = Label(text="Email/Username: ", font=("Arial", 10))
eLabel.grid(column=0, row=2)

# Password Label
pwLabel = Label(text="Password: ", font=("Arial", 10))
pwLabel.grid(column=0, row=3)


# Entrys #

# Website Entry
siteInput = Entry(width=21)
siteInput.grid(column=1, row=1)

# Email/Username Entry
emailInput = Entry(width=30)
emailInput.grid(column=1, row=2, columnspan=1)

# Password Entry
pwInput = Entry(width=21)
pwInput.grid(column=1, row=3)


# Buttons #

# Password Button
pwButton = Button(text="Generate Password", command=generate_password, width=15)
pwButton.grid(column=2, row=3)

# Add Button
addButton = Button(text="Add", width=36, command=save)
addButton.grid(column=1, row=4, columnspan=2)

# Search Button
searchButton = Button(text="Search", command=find_password, width=15)
searchButton.grid(column=2, row=1)

window.mainloop()