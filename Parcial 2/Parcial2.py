# Parcial 2 - Manejo y Estructura de Datos
# Sistema de gestion de pedidos - Distribuidora "Las naranjas"
# Integrantes: Henry Aldair Zelaya, Alex Gabriel Rivera Trujillo



# A. COLA (FIFO) - solicitudes de clientes

def registrar_solicitud(cola, codigo, cliente):
    # La nueva solicitud se agrega al final para respetar el orden de llegada.
    # Cada solicitud se guarda como un diccionario con su codigo y su cliente.
    cola.append({"codigo": codigo, "cliente": cliente})
    print("Solicitud", codigo, "registrada a nombre de", cliente)

def atender_solicitud(cola):
    # Primero se verifica que haya solicitudes pendientes.
    # Si no se revisa, pop(0) daria error con una lista vacia.
    if len(cola) == 0:
        print("No hay solicitudes para atender.")
        return None
    # pop(0) retira la primera solicitud, porque es la que llego antes.
    sol = cola.pop(0)
    print("Atendiendo solicitud", sol["codigo"], "de", sol["cliente"])
    return sol

# Mostrar todas las solicitudes en la cola
def mostrar_solicitudes(cola):
    if len(cola) == 0:
        print("No hay solicitudes pendientes.")
        return
    print("Solicitudes pendientes : ")
    # posicion es solo un contador para numerar la lista en pantalla
    posicion = 1
    for sol in cola:
        # Se muestran desde la primera solicitud hasta la ultima.
        print(" ", posicion, "-", sol["codigo"], "|", sol["cliente"])
        posicion += 1

# Revisa si un codigo de solicitud ya esta en la cola.
def codigo_repetido_cola(cola, codigo):
    # Se recorre la cola y se compara cada codigo con el que se quiere registrar.
    for sol in cola:
        if sol["codigo"] == codigo:
            return True
    # Si termino el recorrido sin encontrarlo, el codigo no esta repetido.
    return False



# B. PILA (LIFO) - despachos

def registrar_despacho(pila, cod_operacion, cod_producto):
    # El nuevo despacho queda en la cima de la pila.
    # Cada despacho guarda el codigo de operacion y el codigo del producto.
    pila.append({"operacion": cod_operacion, "producto": cod_producto})
    print("Despacho", cod_operacion, "registrado (producto", str(cod_producto) + ")")


def retirar_despacho(pila):
    # Se verifica que la pila no este vacia antes de retirar.
    if len(pila) == 0:
        print("No hay despachos para retirar, la pila esta vacia.")
        return None
    # pop() sin numero retira el ultimo elemento, que es la cima.
    desp = pila.pop()
    print("Se retiro el despacho", desp["operacion"], "(producto", str(desp["producto"]) + ")")
    return desp


def mostrar_despachos(pila):
    if len(pila) == 0:
        print("No hay despachos registrados.")
        return
    print("Despachos registrados (la cima es el ultimo):")
    # recorre al reves para que se vea primero la cima
    # range(inicio, fin, paso): empieza en el ultimo indice y baja de 1 en 1 hasta 0
    for i in range(len(pila) - 1, -1, -1):
        d = pila[i]
        print(" ", d["operacion"], "| producto", d["producto"])

# Revisa si un codigo de operacion ya esta en la pila.
def codigo_repetido_pila(pila, operacion):
    # Se recorre la pila y se compara cada codigo de operacion.
    for desp in pila:
        if desp["operacion"] == operacion:
            return True
    return False



# C. ARBOL BINARIO DE BUSQUEDA - codigos de productos

class Nodo:
    def __init__(self, valor):
        # Cada nodo guarda un codigo y referencias a sus dos posibles hijos.
        # None significa que ese hijo todavia no existe.
        self.valor = valor
        self.izq = None
        self.der = None

# Inserta un valor en el arbol binario de busqueda, devuelve la nueva raiz.
def insertar(raiz, valor):
    # Si no hay nodo, se crea el lugar donde se insertara el valor.
    if raiz is None:
        return Nodo(valor)
    # Los valores menores van a la izquierda y los mayores a la derecha.
    # La funcion se llama a si misma (recursion) hasta encontrar un espacio vacio.
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    elif valor > raiz.valor:
        raiz.der = insertar(raiz.der, valor)
    else:
        # Si no es menor ni mayor, es igual: el codigo ya estaba.
        print("El codigo", valor, "ya existe en el arbol.")
    return raiz

# Busca un valor en el arbol binario de busqueda, devuelve True si lo encuentra.
def buscar(raiz, valor):
    # La busqueda termina cuando se encuentra el valor o una rama vacia.
    if raiz is None:
        return False
    if valor == raiz.valor:
        return True
    # Si el valor es menor se busca a la izquierda, si no, a la derecha.
    if valor < raiz.valor:
        return buscar(raiz.izq, valor)
    return buscar(raiz.der, valor)

# Recorrido inorden del arbol binario de busqueda, devuelve los valores ordenados.
def inorden(raiz, resultado):
    # Recorrer izquierda, raiz y derecha devuelve los valores ordenados.
    # resultado es una lista donde se van guardando los valores visitados.
    if raiz is not None:
        inorden(raiz.izq, resultado)
        resultado.append(raiz.valor)
        inorden(raiz.der, resultado)
    return resultado

# Busca el nodo con el menor valor en un arbol binario de busqueda.
def minimo(raiz):
    # el menor siempre esta lo mas a la izquierda
    # se baja por la izquierda hasta que ya no haya mas hijos
    while raiz.izq is not None:
        raiz = raiz.izq
    return raiz

# Elimina un nodo del arbol y devuelve la nueva raiz.
def eliminar(raiz, valor):
    # Si se llega a una rama vacia, el codigo no estaba en el arbol.
    if raiz is None:
        print("El codigo", valor, "no existe, no se puede eliminar.")
        return None
    # Primero se busca el nodo, igual que en buscar().
    if valor < raiz.valor:
        raiz.izq = eliminar(raiz.izq, valor)
    elif valor > raiz.valor:
        raiz.der = eliminar(raiz.der, valor)
    else:
        # Se encontro el nodo: puede tener cero, uno o dos hijos.
        # Si falta un hijo, se reemplaza el nodo por el hijo que existe.
        # Si no tiene hijos, devuelve None y el nodo simplemente desaparece.
        if raiz.izq is None:
            return raiz.der
        if raiz.der is None:
            return raiz.izq
        # Con dos hijos se usa el menor valor de la rama derecha.
        # Ese valor se copia en este nodo y luego se elimina el nodo original.
        sucesor = minimo(raiz.der)
        raiz.valor = sucesor.valor
        raiz.der = eliminar(raiz.der, sucesor.valor)
    return raiz



# Entradas validadas

def pedir_texto(mensaje):
    while True:
        # strip() quita los espacios que haya al inicio y al final
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        # No se permite continuar con un texto vacio.
        print("No puede quedar vacio, intente de nuevo.")


def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()
        # try intenta convertir el texto a numero; si falla, salta al except
        try:
            return int(dato)
        except ValueError:
            # Se repite la pregunta hasta recibir un numero valido.
            print("Debe escribir un numero entero.")

# Muestra todo lo que hay registrado en las tres estructuras.
def mostrar_todo(cola, pila, raiz):
    print("\n------ RESUMEN GENERAL ------")
    # Se reutilizan las funciones que ya existen para cada estructura.
    mostrar_solicitudes(cola)
    print()
    mostrar_despachos(pila)
    print()
    # El arbol se muestra con el recorrido inorden.
    codigos = inorden(raiz, [])
    if len(codigos) == 0:
        print("El arbol esta vacio.")
    else:
        print("Codigos de productos en inorden:", codigos)
    print("-----------------------------")

# Menu principal
def mostrar_menu():
    # Presenta al usuario las operaciones disponibles.
    print("\n====== LAS NARANJAS - GESTION DE PEDIDOS ======")
    print(" COLA (solicitudes)")
    print("  1. Registrar solicitud")
    print("  2. Atender siguiente solicitud")
    print("  3. Mostrar solicitudes pendientes")
    print(" PILA (despachos)")
    print("  4. Registrar despacho")
    print("  5. Mostrar despachos")
    print("  6. Retirar ultimo despacho")
    print(" ARBOL (productos)")
    print("  7. Insertar codigo de producto")
    print("  8. Buscar codigo de producto")
    print("  9. Mostrar codigos (inorden)")
    print(" 10. Eliminar codigo de producto")
    print(" 11. Mostrar todo lo registrado")
    print(" 12. Salir")



def main():
    # Se inicializan las estructuras de datos: cola, pila y arbol.
    # La cola y la pila empiezan como listas vacias y el arbol sin raiz.
    cola = []
    pila = []
    raiz = None

    while True:
        # El menu se repite hasta que el usuario elige la opcion 12.
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()

        if opcion == "1":
            # Registra una nueva solicitud en la cola.
            # upper() convierte a mayusculas para que p001 y P001 sean el mismo codigo.
            codigo = pedir_texto("Codigo de la solicitud (ej. P001): ").upper()
            # Solo se pide el nombre si el codigo no esta repetido.
            if codigo_repetido_cola(cola, codigo):
                print("Ese codigo ya existe en la cola, use otro.")
            else:
                cliente = pedir_texto("Nombre del cliente: ")
                registrar_solicitud(cola, codigo, cliente)
        elif opcion == "2":
            atender_solicitud(cola)
        elif opcion == "3":
            mostrar_solicitudes(cola)
        elif opcion == "4":
            # Registra un nuevo despacho en la pila.
            operacion = pedir_texto("Codigo de operacion (ej. D001): ").upper()
            # Primero se revisa que el codigo de operacion no este repetido.
            if codigo_repetido_pila(pila, operacion):
                print("Ese codigo de operacion ya existe en la pila, use otro.")
            else:
                producto = pedir_entero("Codigo del producto: ")
                registrar_despacho(pila, operacion, producto)
        elif opcion == "5":
            mostrar_despachos(pila)
        elif opcion == "6":
            retirar_despacho(pila)
        elif opcion == "7":
            # Inserta un codigo y muestra el arbol en orden ascendente.
            # raiz se vuelve a asignar porque insertar() devuelve la raiz del arbol.
            codigo = pedir_entero("Codigo a insertar: ")
            raiz = insertar(raiz, codigo)
            print("Codigos actuales:", inorden(raiz, []))
        elif opcion == "8":
            codigo = pedir_entero("Codigo a buscar: ")
            if buscar(raiz, codigo):
                print("El codigo", codigo, "SI existe.")
            else:
                print("El codigo", codigo, "NO existe.")
        elif opcion == "9":
            # inorden(raiz, []) empieza con una lista vacia para guardar los codigos.
            codigos = inorden(raiz, [])
            if len(codigos) == 0:
                print("El arbol esta vacio.")
            else:
                print("Codigos en inorden:", codigos)
        elif opcion == "10":
            # Elimina el codigo indicado y muestra los valores restantes.
            codigo = pedir_entero("Codigo a eliminar: ")
            raiz = eliminar(raiz, codigo)
            print("Codigos actuales:", inorden(raiz, []))
        elif opcion == "11":
            # Muestra la cola, la pila y el arbol juntos.
            mostrar_todo(cola, pila, raiz)
        elif opcion == "12":
            print("Programa finalizado.")
            break
        else:
            # Cualquier cosa que no sea una opcion del menu llega hasta aqui.
            print("Opcion invalida, escriba un numero del menu.")
main()