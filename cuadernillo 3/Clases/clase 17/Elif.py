# Elif permite evaluar otra condicion cuando la anterior no se cumple

nota = 5.5

if  nota >= 9:
    print("Excelente")  
elif nota >= 7:
    print("Aprobado")
elif nota >= 5 and nota < 7:
    print("Eres muy bruto va ah insifuciencia")
else:
    print("Reprobado")