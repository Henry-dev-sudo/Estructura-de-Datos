colaTienda = [] # creamos una cola vacia porque 
# esta iniciando a abrir la tienda

# Operacion ENQUEUE
# Tienda Rosita
colaTienda.append("Ana")
colaTienda.append("Carlos")
colaTienda.append("Luis")

print("Clientes dde la tienda Rosita: ", colaTienda) # Este mensaje es para mostrar los clientes que estan 
# en la cola de la tienda

# Operacion Peek
print("El primer cliente en la cola es: ", colaTienda[0]) # Este mensaje es para mostrar el primer cliente 
# que esta en la cola de la tienda 

# Operacion SIZE
# Consulta cuantos clientes hay
print("Clientes en espera: ", len(colaTienda)) # Este mensaje es para mostrar cuantos clientes 
# hay en la cola de la tienda

# Operación DEQUEUE
# Atiende al primer cliente en la cola
cliente = colaTienda.pop(0) # Este mensaje es para mostrar el primer cliente que esta en la cola de la tienda
print("Atendiendo al cliente: ", cliente) # Este mensaje es para mostrar el primer cliente que esta 
# en la cola de la tienda   

# Mostrar los clientes que siguen
print("Los clientes de la cola sin: ", colaTienda) # Este mensaje es para mostrar los clientes que
# siguen en la cola de la tienda

# Operacion rear
# Consulta quien esta al final de la cola
print("El ultimo cliente en la cola es: ", colaTienda[-1]) # Este mensaje es para mostrar el ultimo 
# cliente que esta en la cola de la tienda

cliente = colaTienda.pop(0)
print("Atendiendo al cliente: ", cliente) 
cliente = colaTienda.pop(0)
print("Atendiendo al cliente: ", cliente) 

# Operacion IS EMPTY
# Comprueba si todavia hay clientes en la cola
if not colaTienda: # Este mensaje es para mostrar si todavia hay clientes en la cola de la tienda
    print("No hay clientes esperando") 
else: 
    print("Todavia hay clientes esperando") # Este mensaje es para mostrar si todavia hay clientes 
    # en la cola de la tienda