estudiantes = ["Ana", "Luis", "Carlos", "María"] #creacion de lista
print (estudiantes[0]) #imprimme "Ana"

#Agregas elementos a la lista
estudiantes.append("Pedro") #agrega al final de la lista
print(estudiantes)

#Eliminar un elemento de la lista
estudiantes.remove("Luis") #elimina el elemento "Luis"
print(estudiantes)

#Ejercicio
lista_mercado= ["manzana", "manzana", "banana", "uva", "manzana"]
print(lista_mercado)

#acceder al indice banana
print(lista_mercado[2]) #imprime "banana"

lista_mercado.append("pera") #agrega "pera" al final de la lista
print(lista_mercado)

#Eliminar dos ocurrencias de "manzana" en una sola línea
for i in range(2): lista_mercado.remove("manzana")
print(lista_mercado)