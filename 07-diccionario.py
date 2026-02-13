'''
Docstringnfor 07-diccionario
¿Que es un diccionario
un diccionario es una estructura de datos que almacena informacion en pares claves-valior

no se accede por posicion, si no por clave.
Ejemplo:
'''
alumno= {
"nombre": "Ana",
"Edad":21,
"Carrera":"Ingenieria"
}
print(type(alumno))
print(alumno)

print("print(alumno['nombre']) =", alumno["nombre"])
print("print(alumno.get('edad')) = ",alumno.get("edad"))

#Agregar o modifiar valores
alumno["promedio"]= 9.2
print(alumno)
alumno["edad"]=22
print(alumno)

#eliminar un par clave
del alumno['Carrera']
print(alumno)

#Recorrer un diccionario
for clave in alumno:
    print(clave)
    print(clave, ":", alumno[clave])
    #funciones utiles para diccioarios
    print("Cantidad de pares clave-valor:",len(alumno))
    print("Claves del diccionario:",alumno.keys())
    print("Valores del diccionario:",alumno.values())
    print("Pares clave-valor:",alumno.items())

    alumno1= {
        "nombre":"",
        "edad": 0,
        "carrera":"Ingenieria"
    }

    ico291=[alumno1,alumno1,alumno1]