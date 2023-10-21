import tkinter as tk
from tkinter import messagebox

import numpy as np


def performe_operação():
    try:
        matrix_a = np.array([[int(entry_a.get()), int(entry_b.get())],
                             [int(entry_c.get()), int(entry_d.get())]])
                            ## [int(entry_i.get()), int(entry_j.get())]])

        matrix_b = np.array([[int(entry_e.get()), int(entry_f.get())],
                             [int(entry_g.get()), int(entry_h.get())]])
##                           [int(entry_k.get()), int(entry_l.get())]])

        operation = operation_var.get()

        determinante_a = np.linalg.det(matrix_a)
        determinante_b = np.linalg.det(matrix_b)
        determinante_c_adição = determinante_a + determinante_b
        determinante_c_subtração = determinante_a - determinante_b

        if operation == "adição":
            resultado = matrix_a + matrix_b
        elif operation == "subtração":
            resultado = matrix_a - matrix_b
        elif operation == "determinada_adição":
            resultado = determinante_c_adição
        elif operation == "determinada_subtração":
            resultado = determinante_c_subtração
        elif operation == "multiplicação":
            resultado = np.dot(matrix_a, matrix_b)


        else:
            messagebox.showerror("Erro", "operação invalida")
            return

        messagebox.showinfo("Resultado", "Resultado: \n" + str(resultado))

    except ValueError:
        messagebox.showerror("Erro", "entrada invalida")


root = tk.Tk()
root.title("Matriz Calculator")

tk.Label(root, text="Matriz A").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=0)
entry_d = tk.Entry(root)
entry_d.grid(row=2, column=1)
##entry_i = tk.Entry(root)
##entry_i.grid(row=3, column=0)
##entry_j = tk.Entry(root)
##entry_j.grid(row=3, column=1)

tk.Label(root, text="Matriz B").grid(row=0, column=2)
entry_e = tk.Entry(root)
entry_e.grid(row=1, column=2)
entry_f = tk.Entry(root)
entry_f.grid(row=1, column=3)
entry_g = tk.Entry(root)
entry_g.grid(row=2, column=2)
entry_h = tk.Entry(root)
entry_h.grid(row=2, column=3)
##entry_k = tk.Entry(root)
##entry_k.grid(row=3, column=2)
##entry_l = tk.Entry(root)
##entry_l.grid(row=3, column=3)###

operation_var = tk.StringVar()
operation_var.set("adição")
operation_label = tk.Label(root, text="selecione a operação")
operation_label.grid(row=5, column=0)
operation_menu = tk.OptionMenu(root, operation_var, "adição", "subtração", "multiplicação", "determinada_adição", "determinada_subtração", )
operation_menu.grid(row=4, column=0, columnspan=1)

calculate_button = tk.Button(root, text="Calcular", command=performe_operação)
calculate_button.grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
