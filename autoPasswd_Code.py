import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  # pip install Pillow
import secrets
import string

# Open new Window + window size
screen = tk.Tk()
screen.geometry('700x500')
screen.title('AutoPasswd')

# background_image
background_image = Image.open("1.jpg")
background_image = background_image.resize((700,500), Image.ANTIALIAS)
bgImage = ImageTk.PhotoImage(background_image)
label1 = tkinter.Label(image=bgImage)
label1.image = bgImage
label1.pack()

# Auto password function
def autoPasswd():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(int(passwd_Length.get())))
    txtBox.delete(0, END)
    txtBox.insert(0,password)

# Buttons hover style function 
def on_enter(e):
    btn['bg'] = 'gray30'
def on_leave(e):
    btn['bg'] = 'gray73'
   
def on_enter2(e):
    exit_Button['bg'] = 'gray30'
def on_leave2(e):
    exit_Button['bg'] = 'gray73'
    
# Combobox creation + text
passwd_Length = ttk.Combobox(screen, width=20)
myLabel2 = Label(screen, text="Password Length:", font=('Arial', 12) )
myLabel2.place(x=120, y=100)

# Adding combobox drop down list with values
passwd_Length['values'] = (4,6,8,10,12)
passwd_Length.place(x=300,y=100)
passwd_Length.current(0)

# Button
btn = tk.Button(screen, text ="Generate Password", pady=5, bd=2, width=15, font=('Arial', 12, 'bold'), bg='gray73', activebackground ="white", command=autoPasswd)
btn.place(x=300, y=200)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

myLabel = Label(screen, text="Your New Password:", font=('Arial', 12) )
myLabel.place(x=120, y=260)

# Entry
txtBox = Entry(screen, width=23, bd=4)
txtBox.place(x=300, y=260)

# Exit Button
exit_Button = tk.Button(screen, text="EXIT", width=14, height=2, bd=10, font=("Arial", 12, "bold"), bg='gray73', activebackground ="red", command=screen.destroy)
exit_Button.place(x=500, y=400)
exit_Button.bind("<Enter>", on_enter2)
exit_Button.bind("<Leave>", on_leave2)

screen.mainloop()