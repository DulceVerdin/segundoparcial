import math, os

class operasBas:
    n1 = 0
    n2 = 0
    n3 = 0
    res = 0
    def cuadrado(self):
        self.res=self.n1*self.n2
        return self.res
    
    def rectangulo(self):
        self.res=self.n1*self.n2
        return self.res
    
    def triangulo(self):
        self.res=(self.n1*self.n2)/2
        return self.res
    
    def circulo(self):
        self.res=self.n1
        return math.pi * (self.res**2)
    
    def trapecio(self):
        self.res=(self.n1+self.n2) * (self.n3) / 2
        return self.res
    

    def pedirNumeros(self, a): 
        self.n1 = int(input("n1: "))
        self.n2 = int(input("n2: "))
        if a == 5:
            self.n3 = int(input("n3: "))

    def imprimir(self):
        print("El resultado es: ", self.res)
    
def main():
    obj = operasBas()
    op = 0
    while op != 6:
        os.system("cls")
        print("1.- cuadrado\n2.- rectangulo\n3.- triangulo\n4.- circulo\n5.- trapecio\n6.- salir")
        op = int(input("OPCION: "))
        if op == 1:
            obj.pedirNumeros(0)
            obj.cuadrado()
            obj.imprimir()
            input()
        if op == 2:
            obj.pedirNumeros(0)
            obj.rectangulo()
            obj.imprimir()
            input()
        if op == 3:
            obj.pedirNumeros(0)
            obj.triangulo()
            obj.imprimir()
            input()
        if op == 4:
            obj.pedirNumeros(0)
            obj.circulo()
            obj.imprimir()
            input()
        if op == 5:
            obj.pedirNumeros(5)
            obj.trapecio()
            obj.imprimir()
            input()    
        elif op == 6:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")

if __name__=="__main__":
    main()

