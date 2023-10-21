import tkinter as tk
from tkinter import messagebox

def clear_all():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_d.delete(0, tk.END)

    operation_var.set("Addition")

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"
def calculate_determinant():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        d = int(entry_d.get())

        operarion = operation_var.get()

        if operarion == "Determinant":
            result = (a * d) - (b * c)
        elif operarion == "Addition":
            result = a + b + c + d
        elif operarion == "Subtraction":
            result = a - b - c - d
        elif operarion == "Multiplication":
            result = a * b * c * d
        else:
            result = "invalid operation"

        messagebox.showinfo("Result", f"Result {result}")

    except ValueError:
        messagebox.showerror("Error", "invalid output")

root = tk.Tk()
root.title("matrix calculator")


root=tk.Tk()
root.title("Matrix determinant calculator")

Label_a = tk.Label(root, text="valor a:",)
Label_a.grid(row=0, column=0, sticky="w")
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

Label_b = tk.Label(root, text="valor b: ",)
Label_b.grid(row=1, column=0, sticky="w")
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

Label_c = tk.Label(root, text="valor c: ",)
Label_c.grid(row=2, column=0, sticky="w")
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

Label_d = tk.Label(root, text="valor d:",)
Label_d.grid(row=3, column=0, sticky="w")
entry_d = tk.Entry(root)
entry_d.grid(row=3, column=1)

operation_var = tk.StringVar()
operation_var.set("determinant")
operation_label = tk.Label(root, text="Select Operation: ",)
operation_label.grid(row=4, column=0, sticky="w")
operation_menu = tk.OptionMenu(root, operation_var, "Determinant", "Addition", "Subtraction", "Multiplication")
operation_menu.grid(row=4, column=1, sticky="w")

clear_button = tk.Button(root, text="Clear", command=clear_all)
clear_button.grid(row=8, column=0, columnspan=8, pady=10)

calculate_button = tk.Button(root, text="Calcular Determinante", command=calculate_determinant)
calculate_button.grid(row=5, columnspan=2, sticky="w")

for entry in(entry_a, entry_b, entry_c, entry_d):
    entry.bind("<Return>", focus_next_entry)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
