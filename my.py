import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string

def generate_password(length, include_upper=True, include_digits=True, include_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    all_characters = lower
    if include_upper:
        all_characters += upper
    if include_digits:
        all_characters += digits
    if include_special:
        all_characters += special
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def on_generate_click():
    length = int(length_var.get())
    include_upper = upper_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()
    
    password = generate_password(length, include_upper, include_digits, include_special)
    password_var.set(password)

# Create the main windows
root = tk.Tk()
root.title("Password Generator")

# Password length
length_var = tk.IntVar(value=12)
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, sticky="e")
length_entry = tk.Spinbox(root, from_=4, to_=32, textvariable=length_var)
length_entry.grid(row=0, column=1)

# Include uppercase
upper_var = tk.BooleanVar(value=True)
upper_check = tk.Checkbutton(root, text="Include Uppercase", variable=upper_var)
upper_check.grid(row=1, column=0, columnspan=2)

# Include digits
digits_var = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.grid(row=2, column=0, columnspan=2)

# Include special characters
special_var = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.grid(row=3, column=0, columnspan=2)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_click)
generate_button.grid(row=4, column=0, columnspan=2)

# Password display
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, wraplength=200)
password_label.grid(row=5, column=0, columnspan=2)

# Copy to clipboard button
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2)

# Run the application
root.mainloop()