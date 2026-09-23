# Ejercicio 6: Crear una lista con los nombres de 5 materias de Ingeniería de Software 
# y realizar las siguientes operaciones: 

# Instrucciones:  
# a) Mostrar la lista completa  
# b) Agregar 2 materias más usando append()  
# c) Insertar una materia en la posición 2 
# d) Eliminar la última materia usando remove()  
# e) Mostrar el número total de materias  
# Materias sugeridas: Programación, Estructura de Datos, Base de Datos, Ingeniería de Software, Redes 

print("Lista de Materias de Ingeniería de Software")
materias = ["Programación", "Estructura de Datos", "Base de Datos", "Ingeniería de Software", "Redes"]
# a) Mostrar la lista completa
print("Materias:", materias)

print("\n")
# b) Agregar 2 materias más usando append() 
materias.append("Sistemas Operativos")
materias.append("Ingles Técnico")
print("Materias después de agregar 2 más:", materias)

print("\n")
# c) Insertar una materia en la posición 2 (una materia nueva, no repetida)
materias.insert(2, "Redes Avanzadas")
print("Materias después de insertar en la posición 2:", materias)

print("\n")
# d) Eliminar la última materia usando remove()
ultima_materia = materias[-1]
materias.remove(ultima_materia)
print(f"Materias después de eliminar la última materia ('{ultima_materia}'):", materias)

print("\n")
# e) Mostrar el número total de materias
print("Número total de materias:", len(materias))