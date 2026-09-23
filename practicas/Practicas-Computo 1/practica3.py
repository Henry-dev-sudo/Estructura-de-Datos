# Enunciado del Ejercicio:

# Deberá construir un programa en Python que resuelva dos casos de uso de la vida real aplicando al menos dos patrones estructurados diferentes aprendidos en la explicación del cuaderno (elija entre LIFO, FIFO o Álgebra de Sets).

# Caso 1 (LIFO o FIFO): Diseñe una solución basada en el patrón seleccionado (ejemplo: sistema deshacer/rehacer, atención a clientes en un banco, cola de reproducción musical o gestión de tareas pendientes).
# Caso 2 (Gestión con Sets): Implemente un sistema de validación de elementos (ejemplo: control de accesos por roles, filtro de etiquetas duplicadas en publicaciones o verificación de requisitos académicos).
# Documentación y explicación: Agregue comentarios en el notebook justificando por qué eligió cada estructura y qué métodos utilizó para resolver el problema.

# Caso 2 (Gestion de sets): Verificacio de requisitos academicos 

# Sistema verficador de requisitos academicos para estudiantes de bachilleerato
# Este sistema deve aprobar que todas las materias deben ser aprobadas con una nota mínima de 6 para poder graduarse.

# Conjunto de materias obligatorias
materias_obligatorias = {"Matemáticas", "Física", "Lenguaje", "Ciencias"}


Alumno_Henry = {
    "Nombre": "Henry Zelaya",
    "materias": { 
        "Matemáticas": 7,
        "Física": 5,
        "Lenguaje": 5,
        "Ciencias": 9,
        "Física": 8   # materia repetida
    }
}
# elimine una materia para ver como el sistema detecta que no se cursó una materia obligatoria ejemplo: "Matemáticas".

# Eliminar materias repetidas usando set de llaves
materias_cursadas = set(Alumno_Henry["materias"].keys())

# Verificar que cursó todas las materias requeridas
if materias_obligatorias.issubset(materias_cursadas):
    # Crear un set con las materias reprobadas
    reprobadas = {materia for materia, nota in Alumno_Henry["materias"].items() if nota < 6}
    
    if not reprobadas:
        print(f"El alumno {Alumno_Henry['Nombre']} ha aprobado todas las materias y puede graduarse.")
    else:
        print(f"El alumno {Alumno_Henry['Nombre']} no puede graduarse. Reprobó:")
        # Recorremos directamente el set de materias reprobadas
        for materia in reprobadas:
            print(" -", materia)
else:
    print(f"El alumno {Alumno_Henry['Nombre']} no cursó todas las materias requeridas, materia faltante: {materias_obligatorias - materias_cursadas}")
