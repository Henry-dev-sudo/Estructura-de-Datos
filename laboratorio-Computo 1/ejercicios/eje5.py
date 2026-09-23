# Ejercicio 5: Crear un programa que demuestre el uso de diferentes tipos de variables en un contexto real: 
# Instrucciones: 
# Simular el registro de un estudiante universitario 
# Incluir: nombre (str), edad (int), promedio (float), becado (bool) 
# Mostrar toda la información de manera organizada 
# Realizar cálculos con las variables numérica 

print("Registro de Estudiante Universitario")

# Declaración de variables
nombre = "Alex"
edad = 19
promedio = 6.5
becado = True

# Mostrar información del estudiante
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Promedio: {promedio}")
print(f"Becado: {becado}")

# Calcular el promedio ajustado (por ejemplo, sumar 1 punto si está becado)
if becado:
    promedio_ajustado = promedio + 1.0
    print(f"Promedio ajustado: {promedio_ajustado}")