# Ejercicio 9: Crear un sistema de coordenadas usando tuplas: 
# Instrucciones: 
# Crear 5 tuplas que representen coordenadas (x, y) de diferentes puntos 
# Almacenar las tuplas en una lista llamada puntos 
# Calcular la distancia de cada punto al origen (0,0) 
# Mostrar cuál punto está más cerca del origen 

puntos = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
distancias = []

for punto in puntos:
    distancia = (punto[0]**2 + punto[1]**2)**0.5
    distancias.append(distancia)

print("Puntos:", puntos)
print("Distancias al origen:", distancias)
print("Punto más cercano al origen:", puntos[distancias.index(min(distancias))])