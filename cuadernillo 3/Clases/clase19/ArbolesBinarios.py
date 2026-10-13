# Caso Práctico: Reestructuración del Catálogo de E-commerce para "NovaMart"

# Contexto del Proyecto:  
# La empresa de retail "NovaMart" está migrando su tienda en línea hacia una nueva 
# arquitectura de microservicios. Uno de los mayores cuellos de botella actuales es el 
# menú de navegación: la base de datos relacional tarda demasiado en devolver las categorías anidadas, 
# causando una mala experiencia de usuario.

# El equipo de Arquitectura de Software ha determinado que la jerarquía de categorías 
# debe cargarse en la memoria caché del servidor web al iniciar el sistema. Para lograr búsquedas
#  y recorridos ultrarrápidos, se requiere modelar este catálogo utilizando una 
# estructura de datos jerárquica: un Árbol Binario.

# LAPTOPS y CELULARES.  
# COCINA y MUEBLES. 

# Creamos la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Creamos la raíz del árbol
raiz = Nodo("Producto")

raiz.izquierdo = Nodo("Tecnologia")
raiz.derecho = Nodo("Hogar")

# Creamos hijos
# Subcategorías de Tecnología
raiz.izquierdo.izquierdo = Nodo("Laptops")
raiz.izquierdo.derecho = Nodo("Celulares")

# Subcategorías de Hogar
raiz.derecho.izquierdo = Nodo("Cocina")
raiz.derecho.derecho = Nodo("Muebles")

# Mostramos la información del árbol
print("Raiz del arbol: ")
print("Valor", raiz.valor)

print("Mostrar hijos: ")
print("Izquierdo: ", raiz.izquierdo.valor)
print("Derecho: ", raiz.derecho.valor)

def es_hoja(nodo):
    return nodo.izquierdo is None and nodo.derecho is None

print("Laptops es hoja: ", es_hoja(raiz.izquierdo.izquierdo))
print("Tecnologia es hoja: ", es_hoja(raiz.izquierdo))
print("Muebles es hoja: ", es_hoja(raiz.derecho.derecho))
print("Hogar es hoja: ", es_hoja(raiz.derecho))


