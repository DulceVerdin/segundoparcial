import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacion = opcion.get()

        if operacion == 1:
            resultado = num1 + num2
        elif operacion == 2:
            resultado = num1 - num2
        elif operacion == 3:
            resultado = num1 * num2
        elif operacion == 4:
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
            resultado = num1 / num2
        else:
            messagebox.showwarning("Advertencia", "Selecciona una operación")
            return

        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora con Radiobotones")
ventana.geometry("350x300")

# Entradas
tk.Label(ventana, text="Primer número:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo número:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Variable para los Radiobotones
opcion = tk.IntVar()

# Aquí deberías agregar los Radiobuttons para que 'opcion' tome valores del 1 al 4
# Ejemplo: tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).pack()
tk.Label(ventana, text="Selecciona la operacion").pack(pady=10)
tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).pack()
tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).pack()
tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).pack()
tk.Radiobutton(ventana, text="División", variable=opcion, value=4).pack()

# Botón calcular
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()
