import tkinter as tk

# Rule-based response function
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot."
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "weather" in user_input:
        return "I can't check the weather, but I hope it's nice outside!"
    elif "bye" in user_input:
        return "See you soon!"
    else:
        return "Sorry, I didn't understand that."

# Function to handle sending messages
def send_message():
    user_text = user_entry.get()
    if user_text.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_text + "\n")
    response = get_response(user_text)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Rule-Based Chatbot")

chat_log = tk.Text(root, state=tk.DISABLED, width=60, height=20, bg="lightyellow", font=("Arial", 12))
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

root.mainloop()
