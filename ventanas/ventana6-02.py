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

ventana = tk.Tk()
ventana.title("Calculadora con Grid")
ventana.geometry("450x550")

tk.Label(ventana, text="Primer número:").grid(row=0, column=0, padx=10, pady=5, )
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=10, pady=5, )
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1, padx=10, pady=5)


opcion = tk.IntVar()
tk.Label(ventana, text="Selecciona la operación:").grid(row=2, column=0, columnspan=2, pady=10)

tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).grid(row=3, column=0, columnspan=2, padx=100)
tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).grid(row=4, column=0, columnspan=2,  padx=100)
tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).grid(row=3, column=2, columnspan=2, padx=100)
tk.Radiobutton(ventana, text="División", variable=opcion, value=4).grid(row=4, column=2, columnspan=2, padx=100)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=7, column=0, columnspan=2, pady=20)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=8, column=0, columnspan=2)

ventana.mainloop()