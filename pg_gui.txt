import tkinter as tk
from tkinter import messagebox

USER_CREDENTIALS = {"admin": "password123"}

class LoginPage:
    def __init__(self, root, on_success):
        self.root = root  # Receive root from main.py
        self.on_success = on_success
        self.create_login_page()

    def create_login_page(self):
        self.clear_window()

        tk.Label(self.root, text="OM SAI LUXURY PG", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.authenticate_user).pack(pady=10)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            self.on_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
