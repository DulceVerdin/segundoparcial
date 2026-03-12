import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


colores = {
    "Negro": 0, "Café": 1, "Rojo": 2, "Naranja": 3,
    "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7,
    "Gris": 8, "Blanco": 9
}

multiplicador = {
    "Negro": 1, "Café": 10, "Rojo": 100, "Naranja": 1000,
    "Amarillo": 10000, "Verde": 100000, "Azul": 1000000,
    "Violeta": 10000000, "Gris": 100000000, "Blanco": 1000000000
}

tolerancia = {
    "Oro": 0.05,
    "Plata": 0.10
}


def calculo():
    b1 = var1.get()
    b2 = var2.get()
    b3 = var3.get()

    if var_tol.get() == 1:
        tol = "Oro"
    elif var_tol.get() == 2:
        tol = "Plata"
    else:
        messagebox.showerror("Error", "Selecciona una tolerancia")
        return

    
    valor = (colores[b1] * 10 + colores[b2]) * multiplicador[b3]

    
    minimo = valor * (1 - tolerancia[tol])
    maximo = valor * (1 + tolerancia[tol])

    
    lbl_res_ohm.config(text=f"{valor} Ω")
    lbl_res_min.config(text=f"{minimo:.0f} Ω")
    lbl_res_max.config(text=f"{maximo:.0f} Ω")


ventana = tk.Tk()
ventana.title("Resistencia")
ventana.geometry("250x500")
ventana.configure(bg="#5EC5EE")

tk.Label(ventana, text="Calcular Valor de resistencias",
         bg="#00FF55", font=("Arial", 12, "bold"), bd=0).pack()


img_pil = Image.open("resistencia.jpg")
img_pil_resized = img_pil.resize((200, 150), Image.Resampling.LANCZOS)
tk_image = ImageTk.PhotoImage(img_pil_resized)

label_imagen = tk.Label(ventana, image=tk_image, bg="#87CEEB", pady=10)
label_imagen.image = tk_image
label_imagen.pack(pady=15)


opciones = list(colores.keys())

var1 = tk.StringVar(ventana); var1.set(opciones[0])
var2 = tk.StringVar(ventana); var2.set(opciones[0])
var3 = tk.StringVar(ventana); var3.set(opciones[0])


frame_color1 = tk.Frame(ventana, bg="#87CEEB")
frame_color1.pack(pady=5)
tk.Label(frame_color1, text="Color 1", bg="#87CEEB", width=15).pack(side="left")
tk.OptionMenu(frame_color1, var1, *opciones).pack(side="left")

f2 = tk.Frame(ventana, bg="#87CEEB")
f2.pack(pady=5)
tk.Label(f2, text="Color 2", bg="#87CEEB", width=15).pack(side="left")
tk.OptionMenu(f2, var2, *opciones).pack(side="left")

f3 = tk.Frame(ventana, bg="#87CEEB")
f3.pack(pady=5)
tk.Label(f3, text="Color 3", bg="#87CEEB", width=15).pack(side="left")
tk.OptionMenu(f3, var3, *opciones).pack(side="left")


tk.Label(ventana, text="Tolerancia", bg="#87CEEB", font=("Arial", 10, "bold")).pack(pady=10)
var_tol = tk.IntVar(value=1)
tk.Radiobutton(ventana, text="Oro", variable=var_tol, value=1, bg="#87CEEB").pack()
tk.Radiobutton(ventana, text="Plata", variable=var_tol, value=2, bg="#87CEEB").pack()


tk.Button(ventana, text="Calcular", command=calculo, bg="#00FF55", width=15).pack(pady=20)


tk.Label(ventana, text="Valor nominal:", bg="#87CEEB").pack(side="left",padx=5)
lbl_res_ohm = tk.Label(ventana, text="0 Ω", bg="#87CEEB", font=("Arial", 10, "bold"))
lbl_res_ohm.pack()

tk.Label(ventana, text="Valor máximo:", bg="#87CEEB").pack()
lbl_res_max = tk.Label(ventana, text="0 Ω", bg="#87CEEB", font=("Arial", 10, "bold"))
lbl_res_max.pack()



tk.Label(ventana, text="Valor mínimo:", bg="#87CEEB").pack()
lbl_res_min = tk.Label(ventana, text="0 Ω", bg="#87CEEB", font=("Arial", 10, "bold"))
lbl_res_min.pack()

ventana.mainloop()