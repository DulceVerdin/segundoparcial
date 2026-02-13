import os
alumno1 = {
    "nombre":"",
    "edad":0,
    "materia":"",
    "calificacion":""
    }
ico201=[]
os.system('cls')
num=int(input("¿Cuantos alunnos,quieres ingresar?"))
for i in range(num):
    nombre = input("Nombre del alumno:")
    edad = int(input("Edad del alumno:" ))
    materia = input("Materia del alumno:")
    calificacion = int(input("Calificaciom del alumno:" ))

     
    alumno1["nombre"]= nombre
    alumno1["edad"] = edad
    alumno1["Materia"] = materia
    alumno1["calificacion"] = calificacion


    ico201.append(alumno1.copy())
    #print("Lista de alumnos ingresados:")
    #for alumno in ico201:
     #   print(alumno)

cantidad = len(ico201)
suma = 0
for alumno in ico201:
    suma += alumno["calificacion"]

if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0

print("Total de alumnos registrados:", cantidad)
print("Promedio de calificaciones:", promedio)


    