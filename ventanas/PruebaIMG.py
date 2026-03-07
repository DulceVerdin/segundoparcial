import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Prueba")
ventana.geometry("700x300")

img = Image.open("prueba.jpg")
img = img.resize((700, 300))
image = ImageTk.PhotoImage(img)

label_fondo = tk.Label(ventana, image = image)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

ventana.mainloop()