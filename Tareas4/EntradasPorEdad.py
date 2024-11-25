edad = int(input("Ingrese su edad: "))
if edad < 18:
    costo = 60
elif 18 <= edad <= 50:
    costo = 80
else:
    costo = 50
print(f"El costo de la entrada es: ${costo} pesos")











def costo_entrada(edad):
    switcher = {
        (0, 17): 60, 
        (18, 50): 80, 
        (51, float('inf')): 50 
    }
    for rango, costo in switcher.items():
        if rango[0] <= edad <= rango[1]:
            return costo
    return None 
edad = int(input("Ingrese su edad: "))
costo = costo_entrada(edad)
print(f"El costo de la entrada es: ${costo} pesos")
