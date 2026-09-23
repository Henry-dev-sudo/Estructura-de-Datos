# Sistema de un banco
# Banco los manguitos

cola = [] # creamos una cola vacia que sera usada globalmente
numero_turno = 1 # Variable global para contabilizar los clientes

def registrar_clientes(nombre):
    global numero_turno # Declaramos la variable global para poder modificarla

    # Generar el codigo de turno
    # T = letra que significa turno, :03d minimo de digitos para rellenar son 3 
    # Ejemplo: T001
    