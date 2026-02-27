import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x200")

# Entradas de texto
tk.Label(ventana, text="primer numero:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="segundo numero").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botón para sumar
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()
#ejecutar la aplicacion
ventana.mainloop()