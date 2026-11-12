# Creamos la base para el arbol de destinos utilizando las clases de NodoDestino
class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

# Función recursiva para mostrar la jerarquía del árbol
def mostrar_arbol(nodo, nivel=0):
    print("  " * nivel + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)

# Función recursiva para buscar un destino en el árbol
def buscar_destino(nodo, nombre_buscado):
    if nodo.nombre.lower() == nombre_buscado.lower():
        return nodo
    for hijo in nodo.hijos:
        resultado = buscar_destino(hijo, nombre_buscado)
        if resultado:
            return resultado
    return None

#Creamos el arbol
terminal_central = NodoDestino("Terminal Central")

z_oriental = NodoDestino("Zona Oriental")
z_central = NodoDestino("Zona Central")
z_occidental = NodoDestino("Zona Occidental")

terminal_central.agregar_hijo(z_oriental)
terminal_central.agregar_hijo(z_central)
terminal_central.agregar_hijo(z_occidental)

z_oriental.agregar_hijo(NodoDestino("San Miguel"))
z_oriental.agregar_hijo(NodoDestino("La Unión"))
z_oriental.agregar_hijo(NodoDestino("Usulután"))

z_central.agregar_hijo(NodoDestino("San Salvador"))
z_central.agregar_hijo(NodoDestino("La Libertad"))

z_occidental.agregar_hijo(NodoDestino("Santa Ana"))
z_occidental.agregar_hijo(NodoDestino("Ahuachapán"))


#Con el arbol creado, lo siguiente que sigue es crear el array para fifo y para lifo, ademas de la funcion extra
#Que agarramos dentro de las funciones adicionales
pila_salidas = []      # El ultimo en entrar es el primero en salir
cola_pasajeros = []    # El primero en entrar es el primero en salir
codigos_buses = set()  # Mejora: Usamso set para eliminar duplicados de codigos de buses
contador_salidas = 1


#Creamos todas las funciones que necesitamos para el menu principal

def mostrar_destinos_disponibles():
    print("\nDESTINOS DISPONIBLES ")
    mostrar_arbol(terminal_central)

#Iniciamos con la funciones de registrar pasajero
def registrarPasajero():
    nombre = input("Ingrese el nombre del pasajero: ").strip()
    mostrar_destinos_disponibles()
    destino = input("Ingrese el destino del pasajero: ").strip()   #Siguiente paso dentro de esta funcion es ingresar el destion
    if not destino:
        print("El destino no puede estar vacío.")                  #El error si esta vacio
        return
    
    if not buscar_destino(terminal_central, destino):                           #Codigo de error si el destino no esta en el arbol
        print(f" El destino '{destino}' no existe en el sistema.")              #Devolmenos lo escrito en el input y lo mostramos como error
        return

    pasajero = {"nombre": nombre, "destino": destino}                           #Si logra llegar hasta aqui, mostramos el pasajero
    cola_pasajeros.append(pasajero)                                             #Lo anadimos a la cola de pasajeros
    print(f"Pasajero {nombre} registrado correctamente.")                       #Mostramos un mensaje final
     #Mostramos el input para la terminal
    if not nombre:                                                 #Creamos una condicion para mostrar que si no hay nombre, de error
        print("El nombre no puede estar vacío.")                    #Usamos strip para eliminar espacios
        return

def atenderPasajero():                                               #Funcion atender pasajeros   
    if len(cola_pasajeros) == 0:                                      #Funcion atender pasajeros, si no tiene nada mostramos error
        print("No hay pasajeros en espera.")
        return
    
    pasajero_atendido = cola_pasajeros.pop(0)                        #Si el pasajero existe, lo buscamos y lo mostramos
    print("\nPASAJERO ATENDIDO")
    print(f"Nombre: {pasajero_atendido['nombre']}")
    print(f"Destino: {pasajero_atendido['destino']}")
    print(f"Restantes en espera: {len(cola_pasajeros)}")                #Mostramos pasajeros en espera

def mostrarCola():                                                 #Funcion mostrar cola de pasajeros
    if len(cola_pasajeros) == 0:                                    #Error si no hay pasajeros en espera
        print("La cola de pasajeros está vacía.")
        return
    
    print("\nPASAJEROS EN ESPERA (FIFO)")                   #Un for each version python para mostrar pasajeros por cada uno que haya
    for i, p in enumerate(cola_pasajeros, 1):
        print(f"{i}. Nombre: {p['nombre']} | Destino: {p['destino']}")
    print(f"Total en espera: {len(cola_pasajeros)}")                #Imprimimos total de pasajeros

def registrarSalida():                                                                         #Funcion registrar salida de bus
    global contador_salidas
    codigo = input("Ingrese el código del bus (ej. BUS-001): ").strip().upper()                 
    if not codigo:
        print("El código del bus no puede estar vacío.")                                        #Mostramos error si no hay codigos
        return
    
    # MEJORA 1: Validación para evitar códigos duplicados
    if codigo in codigos_buses:                                                                 #Con el set que hicimos antes, los codigos deberian de estar filtraods
        print(f"El código de bus '{codigo}' ya se encuentra registrado.")                       #Si ya esta en el set, mostramos error
        return

    mostrar_destinos_disponibles()
    destino = input("Ingrese el destino del bus: ").strip()                                     #Siguiente paso de la funciones es pedir destino
    if not destino:
        print("El destino no puede estar vacío.")                                               #Error si esta vacio 
        return
    
    if not buscar_destino(terminal_central, destino):                                           #Si el destino no esta en el arbol, dar error
        print(f"El destino '{destino}' no existe en esta ruta")
        return

    codigo_salida = f"S{contador_salidas:03d}"
    contador_salidas += 1
    salida = {
        "codigo": codigo,
        "codigo_salida": codigo_salida,
        "destino": destino
    }                                                                                               #Si todo esta correcto, guardamos los datos en un diccionario
    pila_salidas.append(salida)                                                                     #Anadimos a la pila
    codigos_buses.add(codigo)                                                                       # Se guarda en el conjunto para bloquear duplicados
    print(f"Salida registrada: {codigo_salida}")                                                   #Codigo de exito

def deshacerSalida():                                                                               #Borramos codigo de salida
    if len(pila_salidas) == 0:                                                                      #Errror si no se encuentra el codigo
        print("No hay salidas registradas para deshacer.")                                      
        return
    
    salida_retirada = pila_salidas.pop()                                                            #Mostramos el codigo que se retiro de la pila
    codigos_buses.remove(salida_retirada["codigo"])                                                 # Se libera el código del conjunto
    print(f"Se ha deshecho la última salida: Bus {salida_retirada['codigo']}")              #Codigo de exito

def consultarCimaPila():                                                                            #Funcion extra
    if len(pila_salidas) == 0:                                                                      #Si no hay pilas, mostramos error
        print("No hay salidas de buses registradas.")                                                     
        return
    
    cima = pila_salidas[-1]                                                                        #Agarramos el ultimo agregado a la pila
    print("\n ÚLTIMA SALIDA REGISTRADA (Cima de la Pila)")                                   #Mostramos el ultimo
    print(f"Código de Bus: {cima['codigo']}")                                                       #Mostramos el codigo
    print(f"Destino: {cima['destino']}") 
    print(f"Código de Salida: {cima['codigo_salida']}")                                           #Mostramos el destino

def mostrarPila():                                                                                  #Funcion mostrar pila de salidas
    if len(pila_salidas) == 0:                                                                      #Si no hay salidas, mostramos error
        print("No hay salidas de buses registradas.")
        return
    
    print("\nREGISTRO DE SALIDAS (LIFO)")                                                   #Mostramos todas las salidas
    for i in range(len(pila_salidas) - 1, -1, -1):
        s = pila_salidas[i]
        etiqueta = " ÚLTIMA SALIDA" if i == len(pila_salidas) - 1 else ""
        print(f"{i+1}. Bus: {s['codigo']} | Destino: {s['destino']}{etiqueta}")


# MENÚ PRINCIPAL INTERACTIVO
def menu():
    while True:                                                                             
        print("\n========================================")
        print("   SISTEMA DE GESTIÓN - TERMINAL DE BUSES")
        print("========================================")
        print("1. Registrar pasajero (Cola FIFO)")
        print("2. Atender pasajero")
        print("3. Ver pasajeros en espera")
        print("4. Registrar salida de bus (Pila LIFO)")
        print("5. Deshacer última salida")
        print("6. Ver salidas de buses (Pila)")
        print("7. Consultar última salida sin retirar (Mejora 2)")
        print("8. Mostrar árbol de destinos")
        print("9. Buscar destino en el árbol")
        print("10. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrarPasajero()
        elif opcion == "2":
            atenderPasajero()
        elif opcion == "3":
            mostrarCola()
        elif opcion == "4":
            registrarSalida()
        elif opcion == "5":
            deshacerSalida()
        elif opcion == "6":
            mostrarPila()
        elif opcion == "7":
            consultarCimaPila()
        elif opcion == "8":
            print("\n Destinos disponibles de la Ruta La Quemona")
            mostrar_arbol(terminal_central)
        elif opcion == "9":
            buscado = input("Ingrese el nombre del destino a buscar: ").strip()
            if buscado:
                res = buscar_destino(terminal_central, buscado)
                if res:
                    print(f" El destino '{res.nombre}' existe.")
                else:
                    print(f"El destino '{buscado}' no existe.")
            else:
                print("Debe ingresar un nombre válido.")
        elif opcion == "10":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()