#  haz un sistema  de acelaracion usando funciones donde cada vez que presiones
# el acelerador aumente en 10 km

def acelerar(velocidad):
    nueva_velocidad = velocidad + 10
    return nueva_velocidad

# pedimos la velocidad inicial al usuario
velocidad = int(input("Ingrese la velocidad inicial del vehículo (en km/h): "))

# pedimos al usuario que presione el acelerador
velocidad = acelerar(velocidad)
print("Despues de acelarar tu velocidad es: ", velocidad, "km/h")

# aplicar el lifo completo, desaselerar el carro
def desacelerar(velocidad):
    nueva_velocidad = velocidad - 10
    return nueva_velocidad
velocidad = desacelerar(velocidad)
print("Despues de desacelerar tu velocidad es: ", velocidad, "km/h")

