minutos = int(input("Ingresa la cantidad de minutos: "))
horas = minutos // 60  
minutos_restantes = minutos % 60  
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
