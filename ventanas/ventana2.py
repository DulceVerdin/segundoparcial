import tkinter as tk
#creamos la ventana principal 
ventana = tk.Tk()
#le damos un titulo a la ventana 
ventana.title("Mi primera applicaciom")
#le damos un tamaño a la ventana
ventana.geometry("400x300")

#creamos una etiqueta
etiqueta = tk.Label(ventana, text="Hola mundo", font=("Arial",16,"bold"))
etiqueta.pack(pady=20)
#Mostramos la etiqueta en la ventana
ventana.mainloop()