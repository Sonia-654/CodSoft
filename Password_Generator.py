@ -0,0 +1,31 @@
import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            result.set("Length must be > 0")
            return
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(chars, k=length))
        result.set(password)
    except ValueError:
        result.set("Please enter a valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.config(bg="#f0f8ff")

tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)
entry_length = tk.Entry(root, width=10, font=("Arial", 12))
entry_length.pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#add8e6").pack(pady=10)

result = tk.StringVar()
tk.Entry(root, textvariable=result, font=("Arial", 12), state="readonly", width=30).pack()

root.mainloop()
