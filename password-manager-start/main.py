from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#password generator project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbol + password_numbers + password_letters
    shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {website:{
        'email': email,
        'password': password
    }}

    if len(website) == 0 and len(password) == 0:
        messagebox.askokcancel(title='Oops', message="Please don't leave any fields empty!!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


#------------------------------SEARCH WEBSITE-----------------------------------------#
def search():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="Data File Not Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"email:{email} \n password: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)
#labelz
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
#entries
website_input = Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'Email@mail.com')

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

#button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="add", width=44, highlightthickness=0, command=save_details)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()