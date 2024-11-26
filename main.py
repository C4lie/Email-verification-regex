import re
import tkinter as tk
from tkinter import messagebox

# Email validation condition 
email_condition = "^[a-z]+[\._]?[0-9]+[@]\w+[.]\w{2,3}$"

# Function to validate email
def validate_email():
    user_email = email_entry.get()
    if re.search(email_condition, user_email):
        messagebox.showinfo("Validation Result", "Right Email!")
    else:
        messagebox.showerror("Validation Result", "Wrong Email!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x250")

# Add a label
label = tk.Label(root, text="Enter your email address:", font=("Arial", 14))
label.pack(pady=10)

# Add an entry widget for email input
email_entry = tk.Entry(root, font=("Arial", 14), width=30)
email_entry.pack(pady=10)

# Add a button to validate the email
validate_button = tk.Button(root, text="Validate", font=("Arial", 14), command=validate_email)
validate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
