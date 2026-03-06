import tkinter as tK
from tkinter import messagebox
from PIL import Image,ImageTk


root =tK.Tk()
root.title("cerrar con confirmacion")
root.geometry("500x400")

def cerrar():
    respuesta = messagebox.askyesno("Salir","¿Deseas cerrar la aplicacion?" )
    if respuesta:
        root.destroy()


imagen = Image.open("imagen2.png")
fondo = ImageTk.PhotoImage(imagen)
label_fondo = tK.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
frame_acciones = tK.LabelFrame(root, text="Acciones", bg="#1E3A8A", fg="white", padx=10, pady=10)
frame_acciones.place(x=200, y=250, width=200, height=100)
tK.Button(frame_acciones, text="Salir", command=cerrar).pack(pady=20)

root.mainloop()

