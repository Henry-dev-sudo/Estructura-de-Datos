# Sistema de un banco
# Banco los manguitos

cola = [] # creamos una cola vacia que sera usada globalmente
numero_turno = 1 # Variable global para contabilizar los clientes

def registrar_clientes(nombre):
    global numero_turno # Declaramos la variable global para poder modificarla

    # Generar el codigo de turno
    # T = letra que significa turno, :03d minimo de digitos para rellenar son 3 
    # Ejemplo: T001
    
    turno = f"T{numero_turno:03d}" # Generamos el turno con formato T001, T002, etc.
    cliente = [turno, nombre] # Creamos una lista con el turno y el nombre del cliente
    cola.append(cliente) # Agregamos el cliente a la cola
    numero_turno += 1 # Incrementamos el numero de turno para el siguiente cliente

    # Imprimamos el resultado
    print("\nCliente registrado correctamente.")
    print("Turno asignado: ", turno)
    print("Cliente: ", nombre)


    
def ver_siguiente(): # Esto permite ver el siguiente cliente en espera
    if cola:
        siguiente= cola[0]
        print("\nSiguiente cliente en espera:")
        print("Turno:", siguiente[0])
        print("Nombre:", siguiente[1])
    else:
        print("\nNo hay clientes en espera.") 

def atender_cliente(): 
    if cola: 
        cliente = cola.pop(0) # Eliminamos el primer cliente de la cola
        print("\nAtendiendo al cliente:")
        print("Turno:", cliente[0])
        print("Nombre:", cliente[1])
    else:
        print("\nNo hay clientes que atendeer. =).")

def mostrar_cola(): # Esto permite ver todos los clientes en espera
    if not cola:
        print("\nNo hay clientes en esperando.")
    else:
        for cliente in cola:
            print(cliente[0], "-", cliente[1]) # Imprimimos el turno y el nombre del cliente

        print("\nTotal de clientes en espera:", len(cola)) # Imprimimos el total de clientes en espera

        # Para saber quien es el ultimo cliente
        print("Ultimo turno: ", cola[-1][0]) # Imprimimos el turno del ultimo cliente en espera


while True: # Bucle infinito para el menu
    #  Vista de menu: 
    print("\n")
    print("Banco de Manguitos")
    print("1. Registrar cliente")
    print("2. Ver siguiente cliente")
    print("3. llamar al cliente")
    print("4. Mostrar todos los clientes")
    print("5. Salir")

    opcion = input("Seleccione una opción (Numero): ") # Solicitamos al usuario que seleccione una opcion
    if opcion == "1":
        nombre = input("Ingrese su nombre: ") # Solicitamos al usuario que ingrese el nombre
        registrar_clientes(nombre) # Llamamos a la funcion para registrar al cliente

    elif opcion == "2":
        ver_siguiente() # Llamamos a la funcion para ver el siguiente cliente

    elif opcion == "3":
        atender_cliente() # Llamamos a la funcion para atender al cliente

    elif opcion == "4":
        mostrar_cola() # Llamamos a la funcion para mostrar todos los clientes

    elif opcion == "5":
        print("\nSaliendo del sistema...")
        break

    else:
        print("\n Opción no válida. Por favor, seleccione una opción válida.")

    