# Actividad Práctica en Clase
# Sistema Integral de Caja y Despacho

# Implemente las siguientes funcionalidades obligatorias en su programa de simulación:

# Fila en Caja (FIFO): Atender clientes en estricto orden de llegada usando collections.deque con popleft(). 
# Validar qué sucede cuando se intenta cobrar y no hay nadie en la fila.
# Bolsa de Productos (LIFO): Cada cliente tiene una bolsa (pila). Al momento de pagar, los productos se ingresan 
# en un orden, pero el cajero debe desempacar o registrar primero el último producto guardado (pop()).
# Módulos de Cupones y Membresías (Sets): Manejar un conjunto de códigos de membresía vigentes. 
# Registrar el cupón usado para evitar que se repita en la misma sesión.

from collections import deque

# CLASE CLIENTE
class Cliente:

    def agregar_datos(self, nombre, productos, cupon, membresia):
        self.nombre = nombre
        self.productos = productos
        self.cupon = cupon
        self.membresia = membresia

# CREAR FILA DE CLIENTES
fila = deque()

# CLIENTE 1
cliente1 = Cliente()
cliente1.agregar_datos(
    "Henry",
    ["Pan", "Leche", "Huevos"],
    "DESC10",
    "MEMB001"
)

fila.append(cliente1)

# CLIENTE 2
cliente2 = Cliente()
cliente2.agregar_datos(
    "Isvi",
    ["Arroz", "Frijoles"],
    "DESC10",
    ""
)

fila.append(cliente2)

# CLIENTE 3
cliente3 = Cliente()
cliente3.agregar_datos(
    "Oscar",
    ["Detergente"],
    "",
    "MEMB999"
)

fila.append(cliente3)

# CLIENTE 4
cliente4 = Cliente()
cliente4.agregar_datos(
    "Pedro",
    ["Cafe", "Azucar", "Galletas"],
    "",
    ""
)

fila.append(cliente4)

# SET DE MEMBRESÍAS VÁLIDAS
membresias = {"MEMB001", "MEMB002", "MEMB003"}

# SET DE CUPONES USADOS
cupones_usados = set()

print("CLIENTES EN LA FILA:", len(fila))

# ATENDER CLIENTES
while len(fila) > 0:
    # FIFO
    cliente = fila.popleft()

    print("Atendiendo a:", cliente.nombre)
    print("\nProductos registrados:")

    # VALIDAR SI HAY PRODUCTOS
    if len(cliente.productos) == 0:
        print("La bolsa está vacía.")
    else:
        # LIFO
        while len(cliente.productos) > 0:
            producto = cliente.productos.pop()
            print("-", producto)

    # VALIDAR CUPÓN
    print("\nCupón:")

    if cliente.cupon == "":
        print("No presentó cupón.")
    elif cliente.cupon in cupones_usados:
        print("Cupón rechazado, ya fue utilizado.")
    else:
        cupones_usados.add(cliente.cupon)
        print("Cupón aplicado correctamente.")

    # VALIDAR MEMBRESÍA
    print("\nMembresía:")

    if cliente.membresia == "":
        print("No presentó membresía. \n")
    elif cliente.membresia in membresias:
        print("Membresía válida. \n")
    else:
        print("Membresía no válida. \n")

# VALIDAR FILA VACÍA
print("\n")
print("Intentando atender otro cliente...")

if len(fila) == 0:
    print("No hay clientes en la fila.")

# MOSTRAR CUPONES USADOS
print("\nCupones usados en esta sesión:")
print(cupones_usados)