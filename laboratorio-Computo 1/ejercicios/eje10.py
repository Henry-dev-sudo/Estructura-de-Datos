# Ejercicio 10: Trabajar con conjuntos de materias de diferentes carreras: 
# Instrucciones: 
# Crear 3 conjuntos:  
# Ingeniería de Software 
# Ingeniería en Sistemas 
# Ingeniería en Ciencia de Datos 
# Cada conjunto debe tener al menos 6 materias 
# Encontrar materias comunes entre todas las carreras 
# Encontrar materias exclusivas de cada carrera 
# Crear la unión de todas las materias 
# Mostrar cuántas materias únicas hay en total 

conjunto_software = {"Programación", "Estructuras de Datos", "Bases de Datos", "Ingeniería de Software", "Sistemas Operativos", "Redes"}
conjunto_sistemas = {"Programación", "Estructuras de Datos", "Bases de Datos", "Ingeniería en Sistemas", "Sistemas Operativos", "Seguridad Informática"}
conjunto_datos = {"Programación", "Estructuras de Datos", "Bases de Datos", "Ingeniería de Datos", "Aprendizaje Automático", "Minería de Datos"}
# Materias comunes entre todas las carreras
materias_comunes = conjunto_software.intersection(conjunto_sistemas, conjunto_datos)
# Materias exclusivas de cada carrera   
materias_exclusivas_software = conjunto_software - conjunto_sistemas - conjunto_datos
materias_exclusivas_sistemas = conjunto_sistemas - conjunto_software - conjunto_datos
materias_exclusivas_datos = conjunto_datos - conjunto_software - conjunto_sistemas 
# Unión de todas las materias
union_materias = conjunto_software.union(conjunto_sistemas, conjunto_datos)

print("Materias comunes entre todas las carreras:", materias_comunes)
print("Materias exclusivas de Ingeniería de Software:", materias_exclusivas_software)
print("Materias exclusivas de Ingeniería en Sistemas:", materias_exclusivas_sistemas)
print("Materias exclusivas de Ingeniería en Ciencia de Datos:", materias_exclusivas_datos)
print("Unión de todas las materias:", union_materias)
print("Número total de materias únicas:", len(union_materias))