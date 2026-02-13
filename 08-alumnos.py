# Lista donde se guardarán los alumnos
alumnos = []

# Preguntar cuántos alumnos se van a registrar
cantidad = int(input("¿Cuántos alumnos deseas registrar? "))

# Registrar alumnos
for i in range(cantidad):
    print(f"\nAlumno {i+1}")
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    promedio = float(input("Promedio: "))
    
    # Crear diccionario del alumno
    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }
    
    # Agregar a la lista
    alumnos.append(alumno)

# Imprimir todos los alumnos registrados
print("\n Lista de alumnos: ")

for i, alumno in enumerate(alumnos, start=1):
    print(f"\nAlumno {i}")
    for clave, valor in alumno.items():
        print(clave, ":", valor)