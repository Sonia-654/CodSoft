import tkinter as tk
from tkinter import messagebox

# Sample dataset
items = {
    "Action": ["Mad Max", "John Wick", "Gladiator"],
    "Comedy": ["The Mask", "Superbad", "Step Brothers"],
    "Romance": ["The Notebook", "Titanic", "La La Land"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

# Recommendation logic
def recommend():
    genre = genre_var.get()
    if genre in items:
        recommendations = items[genre]
        result_var.set("Recommended: " + ", ".join(recommendations))
    else:
        result_var.set("No recommendations available.")

# GUI setup
root = tk.Tk()
root.title("Recommendation System")
root.geometry("400x250")
root.config(bg="#f0f8ff")

tk.Label(root, text="Select your preferred genre:", font=("Arial", 12), bg="#f0f8ff").pack(pady=10)

genre_var = tk.StringVar()
genre_menu = tk.OptionMenu(root, genre_var, *items.keys())
genre_menu.pack()

tk.Button(root, text="Get Recommendations", command=recommend, font=("Arial", 12), bg="#add8e6").pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 12), wraplength=350, bg="#f0f8ff").pack(pady=10)

root.mainloop()
