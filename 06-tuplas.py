tupla=(1,2,3,4,5,2,3,2)
print(type(tupla) )
print((tupla) )
print("el contenido de la tupla es",tupla[2])
for i in tupla:
    print(i)

print("la cantidad de elementos de la tupla es:",len(tupla))
print("la cantidad de veces que se repite el numero 2 es:",tupla .count(2))
print("El indice del numero3 es:",tupla.index(3))
tupla.append(6)

#esto genera un error , ya que las tuplas son inmutables (no puden cambiar)-