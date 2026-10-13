
# # Ejercicio 1: Inventario de Producto
# # Una tienda registra la cantidad disponible de cuatro productos durante tres días.

# inventario = [
# [15, 12, 10],
# [8, 10, 7],
# [20, 18, 15],
# [12, 14, 11]
# ]
# # Muestre la matriz de inventario.
# # Calcule el total disponible de cada producto.
# # Calcule el total registrado en cada día.
# # Permita modificar la cantidad de un producto indicando su fila y columna.

# # 1. Mostrar la matriz
# print("Matriz de inventario:")
# for fila in inventario:
#     print(fila)

# # 2. Calcular el total disponible de cada producto
# print("\nTotal disponible de cada producto:")
# for col in range(len(inventario[0])):
#     suma = 0
#     for fila in inventario:
#         suma += fila[col]
#     print("Producto", col+1, ":", suma)

# # 3. Calcular el total registrado en cada día
# print("\nTotal registrado en cada día:")
# for total in inventario: 
#     suma = 0
#     for totalCompleto in total:
#         suma += totalCompleto
#     print("Total registrado en el día ", inventario.index(total) + 1, ": ", suma)

# # 4. Modificar la cantidad de un producto
# fila = int(input("\nIngrese la fila (1-4): ")) - 1
# col = int(input("Ingrese la columna (1-3): ")) - 1
# nuevo = int(input("Ingrese el nuevo valor: "))

# inventario[fila][col] = nuevo

# print("\nMatriz actualizada:")
# for fila in inventario:
#     print(fila)

# Ejercicio 2: Registro de Temperaturas
# Una matriz contiene las temperaturas registradas durante cinco días y en tres momentos diferentes del día.

temperaturas = [
[24, 28, 25],
[23, 29, 26],
[25, 30, 27],
[22, 27, 24],
[24, 28, 26]
]

# Muestre la matriz de temperaturas.
print("Matriz de temperaturas:")
print("Matriz de temperaturas:")
for fila in temperaturas:
    print(fila)

# Calcule el promedio de temperatura de cada día.
print("\nPromedio de temperatura de cada día:")
filas = len(temperaturas)
col = len(temperaturas[0])

for columna in range(col):
    suma = 0
    for fila in range(filas):
        suma += temperaturas[fila][columna]
    promedio = suma / filas
    print("Promedio de temperatura en el momento del día", columna + 1, ":", promedio)
# Calcule el promedio correspondiente a cada momento del día.
print("\nPromedio de temperatura correspondiente a cada momento del día:")
for fila in range(filas):
    suma = 0
    for columna in range(col):
        suma += temperaturas[fila][columna]
    promedio = suma / col
    print("Promedio de temperatura en el día", fila + 1, ":", promedio)

# Determine la temperatura más alta registrada
print("\nDeterminando la temperatura más alta registrada:")
max_temp = temperaturas[0][0]
for fila in range(filas):
    for columna in range(col):
        if temperaturas[fila][columna] > max_temp:
            max_temp = temperaturas[fila][columna]
print("La temperatura más alta registrada es:", max_temp)

# Ejercicio 3: Registro de Asistencia
# Una matriz representa la asistencia de cinco estudiantes durante cinco días.
# 1 representa una asistencia y 0 representa una inasistencia.

asistencia = [
[1, 1, 0, 1, 1],
[1, 0, 1, 1, 1],
[1, 1, 1, 1, 0],
[0, 1, 1, 0, 1],
[1, 1, 1, 1, 1]
]

# Muestre la matriz de asistencia.
print("\nMatriz de asistencia:")
for fila in asistencia:
    print(fila)
# Calcule cuántas asistencias tiene cada estudiante.
print("\nCantidad de asistencias por estudiante:")
for fila in range(filas):
    suma = 0
    for columna in range(col):
        suma += asistencia[fila][columna]
    print("Estudiante", fila + 1, ":", suma)
# Calcule cuántos estudiantes asistieron cada día.
print("\nCantidad de estudiantes que asistieron cada día:")
for columna in range(col): 
    suma = 0
    for fila in range(filas):
        suma += asistencia[fila][columna]
    print("Día", columna + 1, ":", suma)
# Identifique al estudiante con mayor cantidad de asistencias.
print("\nIdentificando al estudiante con mayor cantidad de asistencias:")
maxAsistencias = 0
estudianteMax = 0
for fila in range(filas):
    suma = 0
    for columna in range(col):
        suma += asistencia[fila][columna]
    if suma > maxAsistencias:
        maxAsistencias = suma
        estudianteMax = fila + 1
        print("Estudiante con mayor cantidad de asistencias:", estudianteMax, "con", maxAsistencias, "asistencias.")