contador = 5 
def cuentaAtras():
    global contador
    for _ in range(contador):
        print(contador)
        contador -= 1
    print("Flicitaciones, llegaste a uno")
    return contador
cuentaAtras()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

resultado = factorial(5)
print("El factorial es:", resultado)