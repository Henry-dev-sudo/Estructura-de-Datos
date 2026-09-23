
# Ejercicio 11: Una empresa de desarrollo de software necesita llevar un registro de los módulos que forman parte de un sistema. 
# Crea una lista llamada módulos con los siguientes elementos: 
# Módulos = Autenticación, Usuarios, Productos, Reportes, Notificaciones. 
# Instrucciones:
# Desarrolla un programa que realice las siguientes acciones: 
# a) Mostrar la lista completa de módulos. 
# b) Agregar el módulo "Pagos" utilizando append(). 
# c) Insertar "Dashboard" en la posición 2 utilizando insert(). 
# d) Modificar "Productos" por "Inventario" utilizando su índice. 
# e) Eliminar "Notificaciones" utilizando remove(). 
# f) Mostrar cuántos módulos tiene actualmente el sistema utilizando len(). 
# g) Mostrar la lista final. 

modulos = ["Autenticación", "Usuarios", "Productos", "Reportes", "Notificaciones"]
# a) Mostrar la lista completa de módulos
print("Lista completa de módulos:", modulos)
print("\n")
# b) Agregar el módulo "Pagos" utilizando append()
modulos.append("Pagos")
print("Lista después de agregar 'Pagos':", modulos)
print("\n")
# c) Insertar "Dashboard" en la posición 2 utilizando insert()
modulos.insert(2, "Dashboard")
print("Lista después de insertar 'Dashboard' en la posición 2:", modulos)
print("\n")
# d) Modificar "Productos" por "Inventario" utilizando su índice
modulos[3] = "Inventario"
print("Lista después de modificar 'Productos' por 'Inventario':", modulos)
print("\n")
# e) Eliminar "Notificaciones" utilizando remove()
modulos.remove("Notificaciones")
print("Lista después de eliminar 'Notificaciones':", modulos)
print("\n")
# f) Mostrar cuántos módulos tiene actualmente el sistema utilizando len()
print("Número de módulos en el sistema:", len(modulos))
print("\n")
# g) Mostrar la lista final
print("Lista final de módulos:", modulos)