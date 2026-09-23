# 1. Agregar elementos: s.add(<elem>)
# Inserción
# El método add() permite añadir un elemento al set existente.

# # Declaración e inserción
# set2 = set([1, 2])
# set2.add(3)
# print(set2) # Salida: {1, 2, 3}

set2 = set([1, 2])
set2.add(3)
print(set2) # Salida: {1, 2, 3}

# 2. Remover un elemento: s.remove(<elem>)
# Eliminación Estricta
# El método remove() elimina el elemento que se pasa como parámetro.
# Nota: Si el elemento no existe, lanza una excepción de tipo KeyError.

# # Eliminación directa
# set3 = set([1, 2])
# set3.remove(2)
# print(set3) # Salida: {1}

set3 = set([1, 2])
set3.remove(2)
print(set3) # Salida: {1}


# 3. Descartar un elemento: s.discard(<elem>)
# Eliminación Segura
# El método discard() borra el elemento que se pasa como parámetro. Si no se encuentra en el conjunto, no genera ningún error ni detiene la ejecución del programa.

# # Intento de eliminación sin excepción
# set4 = set([1, 2])
# set4.discard(3)
# print(set4) # Salida: {1, 2}

set4 = set([1, 2])
set4.discard(3)
print(set4) # Salida: {1, 2}

# 4. Extracción aleatoria: s.pop()
# Extracción
# El método pop() elimina y retorna un elemento aleatorio del conjunto (dado que los sets no son ordenados).

# # Extracción de elemento no determinado
# set5 = set([1, 2])
# set5.pop()
# print(set5) # Salida: {2} (o {1})

set5 = set([1, 2])
set5.pop()
print(set5) # Salida: {2} (o {1})

# 5. Vaciar el conjunto: s.clear()
# Limpieza
# El método clear() remueve la totalidad de los elementos, dejando el conjunto vacío (representado como set()).

# # Limpieza total del set
# set6 = set([1, 2])
# set6.clear()
# print(set6) # Salida: set()

set6 = set([1, 2])
set6.clear()
print(set6) # Salida: set()
