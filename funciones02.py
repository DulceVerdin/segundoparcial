import os

def suma():
    os.system("cls")
    a = int(input('Numero1: '))
    b = int(input('Numero2: '))
    res = a + b
    print("La suma es: ",res)
    return res
    #input()
    
def resta():
    os.system("cls")
    a = int(input('Numero1: '))
    b = int(input('Numero2: '))
    res = a - b
    print("La resta es: ",res)
    input()
    
def menu():
    op = 0
    while op != 5:
        os.system("cls")
        print("1.- +\n 2.- -\n 3.- * \n 4.- / \n 5.- salir\n")
        op = int(input('OPCION'))
        if op == 1:
            suma()
        if op == 2:
            resta()
    
if __name__("__Main__"):
    menu()

