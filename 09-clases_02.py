import math, os

class operasBas:
    n1 = 0
    n2 = 0
    res = 0
    def sumar(self):
        self.res=self.n1+self.n2
        return self.res
    
    def resta(self):
        self.res=self.n1-self.n2
        return self.res
    
    def multiplicacion(self):
        self.res=self.n1*self.n2
        return self.res
    
    def division(self):
        self.res=self.n1/self.n2
        return self.res
    
#Pedir numeros con variable def y self
    def pedirNumeros(self): #Es parte de la clase y siempre debe estar entre ()
        self.n1 = int(input("n1: "))
        self.n2 = int(input("n2: "))

    def imprimir(self):
        print("El resultado es: ", self.res)
    
def main():
    obj = operasBas()
    op = 0

    while op != 5:
        os.system("cls")
        print("1.- suma\n2.- resta\n3.- multiplicacion\n4.- division\n5.- salir")
        op = int(input("OPCION: "))
        if op == 1:
            obj.pedirNumeros()
            obj.sumar()
            obj.imprimir()
            input()
        if op == 2:
            obj.pedirNumeros()
            obj.resta()
            obj.imprimir()
            input()
        if op == 3:
            obj.pedirNumeros()
            obj.multiplicacion()
            obj.imprimir()
            input()
        if op == 4:
            obj.pedirNumeros()
            obj.division()
            obj.imprimir()
            input()
        if op == 5:
            obj.pedirNumeros()
            obj.division()
            obj.imprimir()
            input()    
        elif op == 6:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")

if __name__=="__main__":
    main()

