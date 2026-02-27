import tkinter as tk
from tkinter import messagebox
def sumar():
    try:
        num1 = float(entrada1. numerp.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")


ventana = tk.Tk()
ventana.title("Grid Layout")

tk.Label(ventana, text="Ingresa el primer numero:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(ventana).grid(row=0, column=1, padx=5, pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Ingresa el segundo numero:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(ventana, show="*").grid(row=1, column=1, padx=5, pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Resultado").grid(row=2, column=0, columnspan=2, pady=10)



tk.Button(ventana, text="Sumar", command=sumar).pack(pady=10)


etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()
ventana.mainloop()