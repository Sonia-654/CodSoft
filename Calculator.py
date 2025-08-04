@ -0,0 +1,48 @@
import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == '+':
            result.set(num1 + num2)
        elif op == '-':
            result.set(num1 - num2)
        elif op == '*':
            result.set(num1 * num2)
        elif op == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Division by 0")
        else:
            result.set("Invalid Operator")
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter first number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Select operator").grid(row=2, column=0)
operator = tk.StringVar()
operator.set('+') 
op_menu = tk.OptionMenu(root, operator, '+', '-', '*', '/')
op_menu.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Result").grid(row=4, column=0)
result = tk.StringVar()
tk.Entry(root, textvariable=result, state='readonly').grid(row=4, column=1)

root.mainloop()
