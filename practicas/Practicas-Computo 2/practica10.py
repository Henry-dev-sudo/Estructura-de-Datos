# # Ejercicio 1: Historial de Navegación con Botones Atrás/Adelante

# # Modela la navegación de un explorador web donde se requiere desplazar hacia adelante y hacia atrás entre pestañas:

# # Utilice la clase ListaDoblementeEnlazada para agregar 5 URLs en secuencia.
# # Demuestre el recorrido desde la primera página cargada hasta la última mediante recorrer_adelante().
# # Demuestre el retorno desde la última página hasta la primera usando los enlaces traseros mediante recorrer_atras().

# class NodoDoble:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None
#         self.anterior = None

# class ListaDoblementeEnlazada:
#     def __init__(self):
#         self.cabeza = None
#         self.cola = None

#     def insertar_final(self, dato):
#         nuevo_nodo = NodoDoble(dato)
#         if self.cabeza is None:
#             self.cabeza = nuevo_nodo
#             self.cola = nuevo_nodo
#         else:
#             nuevo_nodo.anterior = self.cola
#             self.cola.siguiente = nuevo_nodo
#             self.cola = nuevo_nodo

#     def recorrer_adelante(self):
#         actual = self.cabeza
#         while actual is not None:
#             print(actual.dato, end=" <-> ") 
#             actual = actual.siguientente
#         print("None")

#     def recorrer_atras(self):
#         actual = self.cola
#         while actual is not None:
#             print(actual.dato, end=" <-> ") 
#             actual = actual.anterior
#         print("None")

# historial = ListaDoblementeEnlazada()

# # 1. Agregar 5 URLs en el orden en que se visitaron
# historial.insertar_final("google.com")
# historial.insertar_final("youtube.com")
# historial.insertar_final("univo.sv.edu")
# historial.insertar_final("github.com")
# historial.insertar_final("facebook.com")

# # 2. Botón "Adelante": de la primera a la última página
# print("Recorrido hacia adelante (primera -> última):")
# historial.recorrer_adelante()

# # 3. Botón "Atrás": de la última a la primera página
# print("\nRecorrido hacia atrás (última -> primera):")
# historial.recorrer_atras()

# # Ejercicio 2: Reproductor de Música (Pistas musicales Siguiente y Anterior)

# # Simule el comportamiento de una lista de reproducción multimedia:

# # Implemente un método insertar_inicio(dato) que agregue canciones al inicio actualizando los punteros cabeza y anterior.
# # Cree un método eliminar_pista(nombre) que desconecte el nodo correspondiente ajustando adecuadamente sus nodos adyacentes.
# # Elimine la pista ubicada al centro y muestre el estado de la lista en ambos sentidos tras la modificación.

# class NodoDoble:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None
#         self.anterior = None


# class ListaDoblementeEnlazada:
#     def __init__(self):
#         self.cabeza = None
#         self.cola = None

#     def insertar_final(self, dato):
#         nuevo_nodo = NodoDoble(dato)
#         if self.cabeza is None:
#             self.cabeza = nuevo_nodo
#             self.cola = nuevo_nodo
#         else:
#             nuevo_nodo.anterior = self.cola
#             self.cola.siguiente = nuevo_nodo
#             self.cola = nuevo_nodo

#     def insertar_inicio(self, dato):
#         nuevo_nodo = NodoDoble(dato)
#         if self.cabeza is None:
#             self.cabeza = nuevo_nodo
#             self.cola = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.cabeza   # el nuevo mira al antiguo primero
#             self.cabeza.anterior = nuevo_nodo    # el antiguo primero mira al nuevo
#             self.cabeza = nuevo_nodo             # ahora el primero es el nuevo

#     def eliminar_cancion(self, nombre):
#         actual = self.cabeza
#         while actual is not None and actual.dato != nombre:
#             actual = actual.siguiente

#         if actual is None:
#             return False

#         if actual.anterior is not None:
#             actual.anterior.siguiente = actual.siguiente
#         else:
#             self.cabeza = actual.siguiente

#         if actual.siguiente is not None:
#             actual.siguiente.anterior = actual.anterior
#         else:
#             self.cola = actual.anterior

#         return True

#     def recorrer_adelante(self):
#         actual = self.cabeza
#         while actual is not None:
#             print(actual.dato, end=" <-> ")
#             actual = actual.siguiente
#         print("None")

#     def recorrer_atras(self):
#         actual = self.cola
#         while actual is not None:
#             print(actual.dato, end=" <-> ")
#             actual = actual.anterior
#         print("None")

# playlist = ListaDoblementeEnlazada()

# # Cada canción se agrega al inicio, así que la última agregada queda primera
# playlist.insertar_inicio("DtMF")
# playlist.insertar_inicio("Drowning")
# playlist.insertar_inicio("Slow ride")
# playlist.insertar_inicio("Ando en la Disco")
# playlist.insertar_inicio("Vehemencia")

# print("Lista original:")
# playlist.recorrer_adelante()

# # Eliminar la pista del centro
# playlist.eliminar_cancion("Slow ride")

# print("\nTras eliminar 'Slow ride':")
# print("Adelante (siguiente):")
# playlist.recorrer_adelante()
# print("Atrás (anterior):")
# playlist.recorrer_atras()


# Ejercicio 3: Búsqueda Bidireccional Óptima

# Optimice la búsqueda de un elemento según su proximidad a los extremos:

# Cree un método buscar_desde_cola(objetivo) que inicie la inspección desde 
# la cola recorriendo hacia la cabeza con el puntero anterior.
# Compare el número de iteraciones requeridas para encontrar un valor 
# cercano al final buscando desde la cabeza frente a buscar desde la cola.

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    # Búsqueda desde la cabeza hacia la cola
    def buscar_desde_cabeza(self, objetivo):
        actual = self.cabeza
        iteraciones = 0
        while actual is not None:
            iteraciones += 1
            if actual.dato == objetivo:
                return True, iteraciones
            actual = actual.siguiente
        return False, iteraciones
    # Búsqueda desde la cola hacia la cabeza
    def buscar_desde_cola(self, objetivo):
        actual = self.cola
        iteraciones = 0
        while actual is not None:
            iteraciones += 1
            if actual.dato == objetivo:
                return True, iteraciones
            actual = actual.anterior      
        return False, iteraciones

lista = ListaDoblementeEnlazada()

# Lista con 20 elementos
for i in range(1, 21):
    lista.insertar_final(i)

objetivo = 19   # un valor cercano al final

encontrado_cabeza, iter_cola = lista.buscar_desde_cabeza(objetivo)
encontrado_cola, iter_cabeza = lista.buscar_desde_cola(objetivo)

print(f"Buscando el valor {objetivo} en una lista de 20 elementos")
print(f"Desde la cabeza: encontrado={encontrado_cabeza}, iteraciones={iter_cola}")
print(f"Desde la cola:   encontrado={encontrado_cola}, iteraciones={iter_cabeza}")