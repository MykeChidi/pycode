import tkinter as tk
from tkinter import messagebox
import random
import string
import sqlite3
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        self.conn = sqlite3.connect('passwords.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT, 
            password TEXT)
        ''')

        self.service_label = tk.Label(root, text="Sitename:")
        self.service_label.pack()
        self.service_entry = tk.Entry(root)
        self.service_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="#")
        self.password_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.save_button = tk.Button(root, text="Save Password", command=self.save_password)
        self.save_button.pack()

        self.retrieve_button = tk.Button(root, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack()

        self.update_button = tk.Button(root, text="Update Password", command=self.update_password)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Password", command=self.delete_password)
        self.delete_button.pack()

    def generate_password(self):
        length = 12
        all_characters = string.ascii_letters + string.digits + string.punctuation
        if self.service_entry.get():
            password = ''.join(random.choice(all_characters) for i in range(length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        else:
            self.service_label.config(text="Please enter a sitename ")

    def save_password(self):
        service = self.service_entry.get()
        password = self.password_entry.get()
        if service and password:
            encrypted_password = self.cipher_suite.encrypt(password.encode())
            self.cursor.execute('INSERT INTO passwords (service, password) VALUES (?, ?)', (service, encrypted_password))
            self.conn.commit()
            messagebox.showinfo("Success", "Password saved successfully")
            self.service_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both sitename and password")

    def retrieve_password(self):
        service = self.service_entry.get()
        if service:
            self.cursor.execute('SELECT password FROM passwords WHERE service=?', (service,))
            encrypted_password = self.cursor.fetchone()
            if encrypted_password:
                password = self.cipher_suite.decrypt(encrypted_password[0]).decode()
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, password)
            else:
                messagebox.showerror("Error", "No password found for this service")
        else:
            self.service_label.config(text="Please enter the sitename")
            
    def delete_password(self):
        service = self.service_entry.get()
        if service:
            self.cursor.execute('DELETE FROM passwords WHERE service=?', (service,))
            self.conn.commit()
            messagebox.showinfo("Success", "Password deleted successfully")
            self.service_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter the sitename")

    def update_password(self):
        service = self.service_entry.get()
        new_password = self.password_entry.get()
        if service and new_password:
            encrypted_password = self.cipher_suite.encrypt(new_password.encode())
            self.cursor.execute('UPDATE passwords SET password=? WHERE service=?', (encrypted_password, service))
            self.conn.commit()
            messagebox.showinfo("Success", "Password updated successfully")
            self.service_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both sitename and new password")


if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()
    