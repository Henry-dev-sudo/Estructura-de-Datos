# Ejercicio 7: Dada la siguiente lista de días de la semana, realizar operaciones de slicing: 

# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] 
# Instrucciones:  
# a) Mostrar los primeros 3 días  
# b) Mostrar los últimos 2 días  
# c) Mostrar los días laborales (Lunes a Viernes)  
# d) Mostrar el fin de semana  
# e) Mostrar todos los días en orden inverso  
# f) Mostrar un días pares. 

print("Lista de días de la semana")
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("primeros 3 días:", dias[:3]) # a) Mostrar los primeros 3 días

print("últimos 2 días:", dias[-2:]) # b) Mostrar los últimos 2 días
print("días laborales:", dias[:5]) # c) Mostrar los días laborales (Lunes a Viernes)
print("fin de semana:", dias[-2:]) # d) Mostrar el fin de semana
print("días en orden inverso:", dias[::-1]) # e) Mostrar todos los días en orden inverso
print("días pares:", dias[1::2]) # f) Mostrar un días pares.
