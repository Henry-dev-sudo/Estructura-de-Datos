class Nodo:
    # Constructor de la clase Nodo
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Creamos los nodos del árbol binario
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)
n10 = Nodo(10)

# Establecemos las relaciones entre los nodos para formar el árbol binario
n1.izquierda = n2
n1.derecha = n3

n2.izquierda = n4
n2.derecha = n5

n5.izquierda = n8

n3.izquierda = n6
n3.derecha = n7

n7.izquierda = n9
n7.derecha = n10

raiz = n1

# Funciones para recorrer el árbol y obtener información
def recorrer_preorden(nodo):
    # CASO BASE: Si no hay nodo, termina.
    if nodo is None:
        return

    # 1. Procesar RAÍZ (nodo actual)
    print(nodo.valor, end=" ")
    
    # 2. Recorrer lado IZQUIERDO
    recorrer_preorden(nodo.izquierda)
    
    # 3. Recorrer lado DERECHO
    recorrer_preorden(nodo.derecha)

def contar_nodos(nodo):
    if nodo is None:
        return 0

    return (
        1 # El nodo actual
        + contar_nodos(nodo.izquierda)
        + contar_nodos(nodo.derecha)
    )

def altura(nodo):
    if nodo is None:
        return 0

    alt_izq = altura(nodo.izquierda)
    alt_der = altura(nodo.derecha)

    # +1 por el nivel actual
    return 1 + max(alt_izq, alt_der)

print(" Informacion del arbol ")

print("\n Recorrido del arbol: ")
recorrer_preorden(raiz)
print()

total_nodos = contar_nodos(raiz)
print("\n Cantodad total de nodos: ", total_nodos)

altura_arbol = altura(raiz)
print("\n Altura del arbol: ", altura_arbol)