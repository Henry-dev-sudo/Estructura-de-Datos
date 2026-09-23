# Ejercicios de tuplas.
# Ejercicio 1: Sistema de configuración de servidor.
# Una aplicación necesita almacenar configuraciones que no deben modificarse 
# accidentalmente durante la ejecución.
# Crea una tupla llamada configuración con la siguiente información:
# Nombre de aplicación
# Versión
# Servidor
# Puerto
# Modo de ejecución

# Creacion de tupla
configuracion = ("Aplicacion: Sistema Academico", "Version: 1.0.0", "Servidor: localhost", "Puerto: 8080", "Modo: producción")

# Acceso
print( configuracion[1:4]) #imprime "Version: 1.0.0", "Puerto: 8080", "Servidor: localhost":

# longitud de la tupla

print("Longitud de la tupla: ", len(configuracion))
