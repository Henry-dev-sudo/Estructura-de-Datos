producto = {
    "codigo": "P001",
    "nombre": "Teclado Mecánico",
    "precio": 45.00,
    "stock": 20,
    "disponible": True
}

# podemo consultar el nombre del producto
print(producto["nombre"])

# cambiar la disponibilidad del producto y el stock
producto["disponible"] = False
print(producto["disponible"])
producto["stock"] = 0
print(producto["stock"])
