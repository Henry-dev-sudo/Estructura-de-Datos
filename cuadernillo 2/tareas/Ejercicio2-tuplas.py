# Ejercicio 2: Ubicación de dispositivos
# Una empresa de tecnología registra la ubicación de sus dispositivos mediante 
# coordenadas.
# Cada dispositivo debe almacenar:
# Código del dispositivo
# Nombre
# Ubicación (X, Y)
# Estado

dispositivo1 = ("D001", "Sensor de temperatura", (12.5, 7.8), "Activo")
dispositivo2 = ("D002", "Cámara de seguridad", (5.2, 3.1), "Inactivo")
dispositivo3 = ("D003", "Sensor de humedad", (8.9, 4.6), "Activo")

# Mostrar información de los dispositivos
print("Información del dispositivo 1:", dispositivo1)
print("Información del dispositivo 2:", dispositivo2)   
print("Información del dispositivo 3:", dispositivo3)

# Además
# Crea una tupla llamada dispositivos que contenga las tres tuplas anteriores:
# dispositivos = (dispositivo1, dispositivo2, dispositivo3)
# Luego muestra únicamente la coordenada Y del segundo dispositivo utilizando 
# los índices correspondientes

dispositivos = (dispositivo1, dispositivo2, dispositivo3)
print("Coordenada Y del segundo dispositivo:", dispositivos[1][2][1]) # imprime 3.1