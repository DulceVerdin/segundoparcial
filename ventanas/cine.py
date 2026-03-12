import tkinter as Tk
from tkinter import messagebox
from PIL import Image, ImageTk

boleto = 12

def procesar():
    try:
        nombre = entry_nombre.get()
        numPersonas = int(entry_personas.get())
        numBoletos = int(entry_boletos.get())
        usa_cineco = var_cineco.get()  

        if numPersonas == 1 and numBoletos > 7:
            messagebox.showerror("Error", "No puedes comprar más de 7 boletos.")
            return
        elif numPersonas == 2 and numBoletos > 14:
            messagebox.showerror("Error", "No puedes comprar más de 14 boletos.")
            return
        elif numPersonas >= 3 and numBoletos > 21:
            messagebox.showerror("Error", "No puedes comprar más de 21 boletos.")
            return
        elif numPersonas < 1:
            messagebox.showerror("Error", "El número de personas debe ser al menos 1.")
            return

        subtotal = numBoletos * boleto

        if numBoletos > 5:
            descuento = subtotal * 0.15
        elif 3 <= numBoletos <= 5:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        total = subtotal - descuento

        if usa_cineco == 1:  
            descuento_cineco = total * 0.10
            total -= descuento_cineco
            messagebox.showwarning("Advertencia", 
                "Se aplicó un 10% de descuento por pagar con tarjeta CINECO.")
        else:
            descuento_cineco = 0
            messagebox.showinfo("Información", 
                "No se aplicó descuento adicional por tarjeta CINECO.")

        total_var.set(f"{total:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Debes ingresar valores válidos.")

ventana = Tk.Tk()
ventana.title("Cinepolis")
ventana.geometry("800x400")

img = Image.open("Cinepolis.png")
img = img.resize((800, 400))
imagen = ImageTk.PhotoImage(img)

label_fondo = Tk.Label(ventana, image=imagen)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

frame_izq = Tk.Frame(ventana, bg="#0E5DB7", bd=5)
frame_izq.pack(side="left", padx=20, pady=20)

Tk.Label(frame_izq, text="Nombre", fg="white", bg="#0E5DB7").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = Tk.Entry(frame_izq)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

Tk.Label(frame_izq, text="Cantidad Compradores", fg="white", bg="#0E5DB7").grid(row=1, column=0, padx=10, pady=5)
entry_personas = Tk.Entry(frame_izq)
entry_personas.grid(row=1, column=1, padx=10, pady=5)

Tk.Label(frame_izq, text="Cantidad de Boletos", fg="white", bg="#0E5DB7").grid(row=2, column=0, padx=10, pady=5)
entry_boletos = Tk.Entry(frame_izq)
entry_boletos.grid(row=2, column=1, padx=10, pady=5)

var_cineco = Tk.IntVar()
Tk.Label(frame_izq, text="Tarjeta CINECO", fg="white", bg="#0E5DB7").grid(row=3, column=0, pady=5)

rbSi = Tk.Radiobutton(frame_izq, text="Sí", variable=var_cineco, value=1, fg="white", bg="#0E5DB7")
rbSi.grid(row=3, column=1)

rbNo = Tk.Radiobutton(frame_izq, text="No", variable=var_cineco, value=0, fg="white", bg="#0E5DB7")
rbNo.grid(row=4, column=1)

frame_der = Tk.Frame(ventana, bg="#0E5DB7", bd=5)
frame_der.pack(side="right", padx=20, pady=20)

Tk.Label(frame_der, text="Total a Pagar", fg="white", bg="#0E5DB7").grid(row=0, column=0, padx=10, pady=5)
total_var = Tk.StringVar()
entry_total = Tk.Entry(frame_der, textvariable=total_var, state="readonly")
entry_total.grid(row=0, column=1, padx=10, pady=5)

frame_deba = Tk.Frame(ventana, bg="#0E5DB7", bd=5)
frame_deba.pack(side="bottom", pady=20)

Tk.Button(frame_deba, text="Procesar", command=procesar).grid(row=0, column=0, padx=10, pady=10)
Tk.Button(frame_deba, text="Salir", command=ventana.quit).grid(row=0, column=1, padx=10, pady=10)

ventana.mainloop()