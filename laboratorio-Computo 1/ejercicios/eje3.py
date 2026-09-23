# Ejercicio 3: Sin crear variables adicionales, solicitar que el estudiante de la Universidad de Oriente 
# ingrese la siguiente información: (Nombres), (Apellidos), (Materia) y (Carnet)
#  y que se imprima de la siguiente manera: 
# Hola, Bienvenido [Nombres] [Apellidos] gracias por registrarte
#  a la materia de: [Materia], tu usuario para ingresar es: [Carnet]@univo.edu.sv 
# Instrucciones: 
# No crear variables intermedias 
# Usar directamente input () dentro del Print() 
# Usar f-strings para el formateo 

print(f"Hola, Bienvenido {input('Ingrese sus Nombres: ')} {input('Ingrese sus Apellidos: ')} gracias por registrarte a la materia de: {input('Ingrese la Materia: ')}, tu usuario para ingresar es: {input('Ingrese su Carnet: ')}@univo.edu.sv")  # Solicita al usuario que ingrese su información y la imprime en el formato requerido