import tkinter as tk
from tkinter import messagebox

FILE_NAME = "users.txt"


# ---------------- SIGN UP FUNCTION ----------------
def sign_up():
    username = entry_username.get()
    password = entry_password.get()

    # Save user data in file
    file = open(FILE_NAME, "a")
    file.write(username + "," + password + "\n")
    file.close()

    messagebox.showinfo("Success", "Account created successfully!")


# ---------------- SIGN IN FUNCTION ----------------
def sign_in():
    username = entry_username.get()
    password = entry_password.get()

    try:
        file = open(FILE_NAME, "r")
        users = file.readlines()
        file.close()

        # check each saved user
        for user in users:
            saved_username, saved_password = user.strip().split(",")

            if username == saved_username and password == saved_password:
                messagebox.showinfo("Success", "Login successful!")
                return

        messagebox.showerror("Error", "Invalid username or password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No account found. Please sign up first.")


# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")


# Username input
tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()


# Password input
tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()


# Buttons
tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)
tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)


root.mainloop()