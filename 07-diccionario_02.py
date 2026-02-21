import math, os
alumnos=[]
while True:
    try:
        num= int(input("¿Cuantos alumnos quieres ingresar?"))
        break #Si la conversion es exitosa salimos del bucle
    except ValueError:
        print("Error: Por favor ingresa un numeor entero valido")

for i in range (num):
    nombre= input("Nombre del alumno: ")
    edad= input("Edad del alumno: ")
    materia= input("Materia del alumno: ")
    calificacion=float(input("Calificacion del alumno: "))

    alumno ={
        "nombre": nombre,
        "edad": edad,
        "materia": materia,
        "calificacion": calificacion
    }
    alumnos.append(alumno)

    os.system("cls")
    print(f"Se ingresaron {len(alumnos)} alumnos.")

    #Calcular el promedio de las calificaciones
    if alumnos:
        total_calificaciones=sum(alumno["calificacion"] for alumno in alumnos)
        promedio=total_calificaciones/len(alumnos)
        print(f"Promedio de calificaciones: {promedio}")
    else:
        print("No se ingresaron las calificaciones.")

    #Mostrar la lista completa de alumnos
    print("Lista completa de alumnos: ")
    for alumno in alumnos:
        print(alumno)