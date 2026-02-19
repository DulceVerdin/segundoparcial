import math, os

def cuadrado():
    os.system("cls")
    a = int(input("Ingrese el lado uno : "))
    b = int(input("Ingrese el lado dos : "))
    return a*b

def rectangulo():
    os.system("cls")
    a = int(input("Ingrese el valor de la base : "))
    b = int(input("Ingrese el valor de la altura : "))
    return a*b

def triangulo():
    os.system("cls")
    a = int(input("Ingrese el valor de base : "))
    b = int(input("Ingrese el valor de altura : "))
    return a*b/2

def circulo():
    os.system("cls")
    a = int(input("Ingrese el valor de radio : "))
    return math.pi * (a**2)

def trapecio():
    os.system("cls")
    a = int(input("Ingrese el valor de la base mayor : "))
    b = int(input("Ingrese el valor de la base menor: "))
    c= int(input("Ingrese el valor de la altura : "))
    return (a+b) * (c) /2

def menu():
    opcion = 0
    while opcion != 6:
        print("\n--- menu ---")
        print("1.- cuadrado\n2.- rectangulo\n3.- triangulo\n4.- circulo\n5.-trapecio\n6 salir")
        opcion = int(input("Seleccione una opcion : "))

        if opcion == 1:
            print("La area del cuadrado es:", cuadrado())
        elif opcion == 2:
            print("La area del rectangulo es:", rectangulo())
        elif opcion == 3:
            print("La area del triangulo es:", triangulo())
        elif opcion == 4:
            print("La area del circulo es:", circulo())
        elif opcion == 5:
            print("La area del trapecio es:", trapecio())
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")

menu()

if __name__==("__main__"):
    menu()