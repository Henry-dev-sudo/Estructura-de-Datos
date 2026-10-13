# Clase Nodo: cada nodo guarda un valor y dos enlaces (izquierdo y derecho)
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


# Ejercicio 1: Árbol Genealógico Familiar
print("Ejercicio 1: Árbol Genealógico Familiar")

# Nivel 1: el abuelo es la raíz
abuelo = Nodo("Abuelo Carlos")

# Nivel 2: los dos hijos del abuelo
abuelo.izq = Nodo("Padre Luis")
abuelo.der = Nodo("Tía María")

# Nivel 3: los nietos (dos por cada hijo)
abuelo.izq.izq = Nodo("Nieto Pedro")
abuelo.izq.der = Nodo("Nieta Ana")
abuelo.der.izq = Nodo("Nieto Juan")
abuelo.der.der = Nodo("Nieta Sofía")

# Imprimimos las relaciones accediendo a los atributos
print("Abuelo:", abuelo.valor)
print("Hijos del abuelo:", abuelo.izq.valor, "y", abuelo.der.valor)
print("Hijos de Luis:", abuelo.izq.izq.valor, "y", abuelo.izq.der.valor)
print("Hijos de María:", abuelo.der.izq.valor, "y", abuelo.der.der.valor)


# Ejercicio 2: Menú Interactivo de Decisiones
print("\n Ejercicio 2: Menú Interactivo de Decisiones ")

# Recorrido preorden: primero el nodo, luego izquierda y derecha
def preorden(nodo):
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izq)
        preorden(nodo.der)

# Recorrido postorden: primero izquierda y derecha, al final el nodo
def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor)

# Raíz: pregunta inicial
soporte = Nodo("¿El equipo enciende?")

# Opciones "Sí" y "No"
soporte.izq = Nodo("Sí: Tiene internet?")
soporte.der = Nodo("No: Está conectado a la corriente?")

# Acciones finales de la rama "Sí"
soporte.izq.izq = Nodo("Sí: Cerrar el ticket, problema resuelto")
soporte.izq.der = Nodo("No: Revisar el cable de red")

# Acciones finales de la rama "No"
soporte.der.izq = Nodo("Sí: Llevar el equipo a revisión técnica")
soporte.der.der = Nodo("No: Conectar el cable de corriente")

print("Recorrido Preorden (orden en que se evalúan las opciones)")
preorden(soporte)

print("Recorrido Postorden (cierre de procesos, de hojas a raíz)")
postorden(soporte)


# Ejercicio 3: Reporte de Auditoría de Carpetas
print("\n Ejercicio 3: Reporte de Auditoría de Carpetas ")

# Cuenta todos los nodos (carpetas + archivos)
def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izq) + contar_nodos(nodo.der)

# Cuenta solo las hojas (nodos sin hijos): los archivos finales
def contar_hojas(nodo):
    if nodo is None:
        return 0
    # Si no tiene hijo izquierdo ni derecho, es una hoja
    if nodo.izq is None and nodo.der is None:
        return 1
    return contar_hojas(nodo.izq) + contar_hojas(nodo.der)

# Busca un nombre dentro del árbol
def buscar_valor(nodo, objetivo):
    if nodo is None:
        return False
    if nodo.valor == objetivo:
        return True
    return buscar_valor(nodo.izq, objetivo) or buscar_valor(nodo.der, objetivo)

# Construimos la jerarquía de carpetas
documentos = Nodo("Documentos")
documentos.izq = Nodo("Fotos")
documentos.der = Nodo("Tareas")
documentos.izq.izq = Nodo("vacaciones.jpg")
documentos.izq.der = Nodo("familia.jpg")
documentos.der.izq = Nodo("matematicas.docx")
documentos.der.der = Nodo("informatica.pdf")

total = contar_nodos(documentos)
archivos = contar_hojas(documentos)
carpetas = total - archivos  # lo que no es archivo, es carpeta

print("Total de elementos:", total)
print("Total de carpetas:", carpetas)
print("Total de archivos (hojas):", archivos)

# Buscamos el archivo que escriba el usuario
nombre = input("Escriba el nombre del archivo a buscar: ")
if buscar_valor(documentos, nombre):
    print("El archivo", nombre, "SÍ existe en el árbol.")
else:
    print("El archivo", nombre, "NO existe en el árbol.")