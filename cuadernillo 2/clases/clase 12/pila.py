pila = []
pila.append("Iniciar sesion") # append() para agregar un elemento al final de la lista
print(pila)
pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("Hola k ase")

print("Pila actual: ", pila)

# Desapilar un elemento
accion = pila.pop()

print("\n Acccion retirada: ")
print(accion) 

print("\n Penultima accion retirada: ")
print(pila) 