# Practica 2: Estructuras de datos 
# Tema: Conjuntos (Set) vs Listas y Tuplas en Python

# Actividad: Crear un programa que demuestre el uso de listas, tuplas y sets en Python.
# miniprograma utilizando los tipos de datos (listas,tuplas, set)

# lista de reproduccion musical

# # LISTA
# Se utiliza para almacenar las canciones porque
# podemos agregar y eliminar canciones.
print("LISTA:")
canciones = ["Rust", "Wonderwall", "Everlong"]
print("\nTus canciones favoritas son: ")
for cancion in canciones:
    print("~" + cancion)
# Agregando una cancion a la lista
canciones.append("I Don't Wanna Be Me")
canciones.remove("Rust")
print("\nTus canciones favoritas actualizadas son: ")
for cancion in canciones:
    print("~" + cancion)

# 2. Coleccion de videojuegos-generos
# Set
# El set elimina automáticamente los elementos repetidos:
generos = { "Aventura", "Acción", "RPG", "Estrategia", "Acción" } # Se utiliza un set para almacenar los géneros de videojuegos porque no queremos duplicados.  
print("\nSET:")
print(generos)

# Registro de cursos aprobados-cursos ya aprobados
# # TUPLA
# Se utiliza una tupla para almacenar los cursos aprobados porque no queremos que se modifi
cursos_aprobados = ("Matemáticas", "Física", "Química") # Se utiliza una tupla para almacenar los cursos aprobados porque no queremos que se modifiquen.
print("\nTUPLA:")
print("Tus cursos aprobados son: ")
print(cursos_aprobados)


# 3. Inventario de productos basico
# set
# Se utiliza un set para almacenar los productos porque no queremos duplicados o agregar nuevos productos.
productos = {"Laptop", "Mouse", "Teclado", "Monitor", "Mouse", "Laptop"} 
print("\nSET:")
print(productos)
productos.add("Auriculares") # agregando un nuevo producto al inventario
print("\nInventario actualizado: ") 
print(productos)