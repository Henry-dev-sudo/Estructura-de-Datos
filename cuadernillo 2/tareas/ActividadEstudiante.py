# Instrucciones: Modifica el programa para administrar los 
# empleados de dos departamentos utilizando los métodos de conjuntos (Sets).
# Sigue los pasos descritos para cada departamento.

ventas = {"Ana", "Carlos", "Maria"}
soporte = {"Jose", "Luis", "Maria"}
# Parte A — Departamento de Ventas
print("Empleados en ventas:", ventas)

ventas.add("Pedro")
ventas.add("Pedro")  # Intento de agregar nuevamente a "Pedro"
ventas.remove("Carlos") # Intento de eliminar a "Carlos"
ventas.discard("Roberto")  # Intento de eliminar a "Roberto"
empleado_retirado = ventas.pop() # Extracción de un empleado
print("Empleado retirado:", empleado_retirado)
ventas.clear() # Limpieza del conjunto de ventas
print("Conjunto de ventas vacío:", ventas)

# Parte B — Departamento de Soporte
print("\nEmpleados en soporte:", soporte)
# Realiza nuevamente las operaciones anteriores, pero utilizando el conjunto soporte.
soporte.add("Pedro")
soporte.add("Pedro")  # Intento de agregar nuevamente a "Pedro"
soporte.remove("Luis")
soporte.discard("Roberto")  # Intento de eliminar a "Roberto"
empleado_retirado = soporte.pop()
print("Empleado retirado:", empleado_retirado)
soporte.clear()
print("Conjunto de soporte vacío:", soporte)
