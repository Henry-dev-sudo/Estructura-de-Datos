# sistema  de acelaracion usando funciones donde cada vez que presiones
# el acelerador aumente en 10 km

# Funcion acelerar: recibe la velocidad actual como parametro (velocidad),
# le suma 10 km/h y devuelve el nuevo valor con return.
def acelerar(velocidad):
    nueva_velocidad = velocidad + 10
    return nueva_velocidad

# pedimos la velocidad inicial al usuario
# input() devuelve texto, por eso usamos int() para convertirlo a numero entero
velocidad = int(input("Ingrese la velocidad inicial del vehículo (en km/h): "))

# Si el usuario escribe una velocidad inicial negativa, la tomamos como 0 (detenido)
if velocidad < 0:
    velocidad = 0

# pedimos al usuario que presione el acelerador
# llamamos a acelerar() y guardamos el resultado en la misma variable
velocidad = acelerar(velocidad)
print("Despues de acelarar tu velocidad es: ", velocidad, "km/h")

# aplicar el lifo completo, desaselerar el carro
# Funcion desacelerar: hace lo contrario a acelerar, resta 10 km/h
# a la velocidad recibida y devuelve el resultado.
def desacelerar(velocidad):
    nueva_velocidad = velocidad - 10
    # Una velocidad no puede ser negativa: si el resultado baja de 0,
    # el vehiculo queda detenido (0 km/h)
    if nueva_velocidad < 0:
        nueva_velocidad = 0
    return nueva_velocidad
# llamamos a desacelerar() con la velocidad actual (la que ya fue acelerada)
velocidad = desacelerar(velocidad)
print("Despues de desacelerar tu velocidad es: ", velocidad, "km/h")