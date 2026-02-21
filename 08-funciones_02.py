import os
def suma():
    os.system("cls")
    a=int(input("Numero 1: "))
    b=int(input("NUmero 2: "))
    res=a+b
    return
    #print("La suma es: ", res)
    #input()

def resta():
    os.system("cls")
    a=int(input("Numero 1: "))
    b=int(input("NUmero 2: "))
    res=a-b
    print("La resta es: ", res)
    input()

def multiplicacion():
    os.system("cls")
    a=int(input("Numero 1: "))
    b=int(input("NUmero 2: "))
    res=a*b
    print("La multiplicacion es: ", res)
    input()

def division():
    os.system("cls")
    a=int(input("Numero 1: "))
    b=int(input("NUmero 2: "))
    res=a/b
    print("La division es: ", res)
    input()

def menu():
    op=0
    while op!=5:
        os.system("cls")
        print(" 1.- +\n 2.- -\n 3.- *\n 4.- / \n 5.- Salir\n")
        op=int(input('OPCION '))
        if op==1:
            suma()
        if op==2:
            resta()
        if op==3:
            multiplicacion()
        if op==4:
            division()
              
if __name__==("__nain__"):
 menu()