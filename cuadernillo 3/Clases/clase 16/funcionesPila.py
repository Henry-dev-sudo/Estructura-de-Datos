def push(pila, elemento): #creamos la funcion push que recibe como parametros una pila y un elemento
    pila.append(elemento) #agregamos el elemento a la pila

def pop(pila): #creamos para retirar elementos de la pila
    return pila.pop() #retiramos el ultimo elemento de la pila y lo retornamos

# creamos una pila vacia
pila = []
push(pila, "A") #agregamos el elemento A a la pila
push(pila, "B") #agregamos el elemento B a la pila
push(pila, "C") #agregamos el elemento C a la pila
print("Elementos de la pila: ", pila) #mostramos los elementos de la pila
    
elemento = pop(pila) #retiramos el ultimo elemento de la pila y lo guardamos en la variable elemento
print("Elemento retirado: ", elemento) #mostramos el elemento retirado