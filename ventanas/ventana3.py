import tkinter as tk
#creamos la ventana principal 
def saludos():
    label_resultado.config(text="Hola alumnos Python")
ventana= tk.Tk()
#le damos un titulo a la ventana 
ventana.title("Ejemplo de botones")
#le damos un tamaño a la ventana
ventana.geometry("400x300")
boton=tk.Button(ventana, text="saludar",command=saludos)
boton.pack(pady=20)
#creamos una etiqueta
label_resultado= tk.Label(ventana, text="preciona el boton", font=("Arial",16,"bold"))
label_resultado.pack(pady=20)
#Mostramos la etiqueta en la ventana
ventana.mainloop()