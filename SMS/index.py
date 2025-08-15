from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from app import Main

def login():
    uid = username_entry.get()
    pwd = password_entry.get()
    if  pwd == "password":
        messagebox.showinfo("Login Success", "Welcome to the Student Management System!")
        app.destroy()
        Main()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

app = CTk()
app.title("Student Management System - Login")
app.iconbitmap("./assets/illustration.ico")

app._set_appearance_mode("Dark")
set_default_color_theme("./assets/breeze.json")

illustration_img = Image.open("./assets/illustration_i.png")
illustration_img = illustration_img.resize((200, 280))
illustration_photo = ImageTk.PhotoImage(illustration_img)

width = 550
height = 350
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
app.geometry(f"{width}x{height}+{x}+{y}")
app.resizable(False, False)

left_frame = CTkFrame(app, width=100)
left_frame.pack(side=LEFT, fill=BOTH)

illustration_label = CTkLabel(left_frame, image=illustration_photo, text="")
illustration_label.pack(side=BOTTOM, pady=20, padx=20)

right_frame = CTkFrame(app, fg_color="transparent")
right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0))

header = CTkLabel(right_frame, text="Login Here!", font=("Kanit", 24, "bold"))
header.pack(pady=20, padx=20)
username_label = CTkLabel(right_frame, text="Username", font=("Kanit", 16))
username_label.pack(pady=(10, 0), padx=20, anchor=W)
username_entry = CTkEntry(right_frame, placeholder_text="Enter your username")
username_entry.pack(padx=20, fill=X)
password_label = CTkLabel(right_frame, text="Password", font=("Kanit", 16))
password_label.pack(pady=(10, 0), padx=20, anchor=W)
password_entry = CTkEntry(right_frame, placeholder_text="Enter your password", show="*")
password_entry.pack(padx=20, fill=X)
login_button = CTkButton(right_frame, text="Login💨", font=("Kanit", 16), command=login)
login_button.pack(pady=(20, 0), padx=20, fill=X)

app.mainloop()