import math, os

def suma():
    os.system("cls")
    a = int(input("Ingrese el primer valor : "))
    b = int(input("Ingrese el segundo valor : "))
    return a+b

def resta():
    os.system("cls")
    a = int(input("Ingrese el primer : "))
    b = int(input("Ingrese el segundo : "))
    return a-b

def multiplicacion():
    os.system("cls")
    a = int(input("Ingrese el primer valor : "))
    b = int(input("Ingrese el segundo valor : "))
    return a*b

def division():
    os.system("cls")
    a = int(input("Ingrese el primer valor : "))
    b = int(input("Ingrese el segundo valor : "))
    if b == 0:
        return "Error: división entre cero"
    return a/b

def menu():
    opcion = 0
    while opcion != 5:
        print("\n--- menu ---")
        print("1.- suma\n2.- resta\n3.- multiplicacion\n4.- division\n5.- salir")
        opcion = int(input("Seleccione una opcion : "))

        if opcion == 1:
            print("La suma es:", suma())
        elif opcion == 2:
            print("La resta es:", resta())
        elif opcion == 3:
            print("La multiplicacion es:", multiplicacion())
        elif opcion == 4:
            print("La division es:", division())
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")

menu()

 