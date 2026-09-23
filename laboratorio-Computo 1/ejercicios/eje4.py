# Ejercicio 4: Crear un programa que declare variables de diferentes tipos de datos básicos
#  y muestre su información: 
# Instrucciones: 
# Crear al menos una variable de cada tipo: int, float, str, bool 
# Usar la función type() para mostrar el tipo de cada variable 
# Mostrar el valor y tipo de cada variable en formato legible 
# # Realizar al menos una operación compatible entre las variables, por ejemplo,
# concatenar cadenas o realizar una operación matemática. 
# Ejemplo de salida esperada: 
# Variable: edad = 20, Tipo: <class 'int'> 
# Variable: promedio = 8.5, Tipo: <class 'float'> 
# Variable: nombre = "Juan", Tipo: <class 'str'> 
# Variable: activo = True, Tipo: <class 'bool'>

# Declaración de variables
edad = 20
promedio = 8.5
nombre = "hENRY"
activo = True

# Mostrar valor y tipo de cada variable
print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f"Variable: nombre = \"{nombre}\", Tipo: {type(nombre)}")
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

# Operación compatible: concatenación de cadenas
saludo = "Hola, mi nombre es " + nombre
print(f"Variable: saludo = {saludo}, Tipo: {type(saludo)}")
