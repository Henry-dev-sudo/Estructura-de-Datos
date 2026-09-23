# Ejercicio 8: Crear un programa que trabaje con una cadena de texto usando slicing: 
# Instrucciones: 
# Usar la frase: "Universidad de Oriente - El Salvador" 
# Extraer solo "Universidad" 
# Extraer solo "El Salvador" 
# Mostrar la frase completa al revés 
# Mostrar cada tercera letra de la frase 

frase = "Universidad de Oriente - El Salvador"

print("Extraer solo 'Universidad':", frase[:11]) # Extraer solo "Universidad"
print("Extraer solo 'El Salvador':", frase[-11:]) # Extraer solo
print("Frase completa al revés:", frase[::-1]) # Mostrar la frase completa al revés
print("Cada tercera letra:", frase[::3]) # Mostrar cada tercera letra de la frase

