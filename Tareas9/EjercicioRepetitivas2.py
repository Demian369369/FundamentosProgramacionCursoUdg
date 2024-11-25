def multiplicacion_por_sumas_sucesivas():
    print("\n--- Problema 1: Multiplicación por sumas sucesivas ---")
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))
    resultado = 0
    contador = 0
    while contador < abs(num2):
        resultado += num1
        contador += 1
    if num2 < 0:
        resultado = -resultado
    print(f"Usando while: {num1} * {num2} = {resultado}")
    resultado = 0
    contador = 0
    while True:
        resultado += num1
        contador += 1
        if contador >= abs(num2):
            break
    if num2 < 0:
        resultado = -resultado
    print(f"Simulando do-while: {num1} * {num2} = {resultado}")
    resultado = 0
    for _ in range(abs(num2)):
        resultado += num1
    if num2 < 0:
        resultado = -resultado
    print(f"Usando for: {num1} * {num2} = {resultado}")

def contar_numeros():
    print("\n--- Problema 2: Contar números dentro de rangos ---")
    contador_cien = 0
    contador_mayores_50 = 0
    contador_menores_50 = 0
    i = 0
    while i < 10:
        numero = int(input(f"Ingrese el número {i + 1} (0-100): "))
        if numero == 100:
            contador_cien += 1
        elif 50 < numero < 100:
            contador_mayores_50 += 1
        elif 0 < numero < 50:
            contador_menores_50 += 1
        i += 1

    print(f"Usando while: Números iguales a 100: {contador_cien}, Mayores a 50 y menores a 100: {contador_mayores_50}, Menores a 50 y mayores a 0: {contador_menores_50}")
    i = 0
    while True:
        numero = int(input(f"Ingrese el número {i + 1} (0-100): "))
        if numero == 100:
            contador_cien += 1
        elif 50 < numero < 100:
            contador_mayores_50 += 1
        elif 0 < numero < 50:
            contador_menores_50 += 1
        i += 1
        if i >= 10:
            break

    print(f"Simulando do-while: Números iguales a 100: {contador_cien}, Mayores a 50 y menores a 100: {contador_mayores_50}, Menores a 50 y mayores a 0: {contador_menores_50}")
    contador_cien = 0
    contador_mayores_50 = 0
    contador_menores_50 = 0
    for i in range(10):
        numero = int(input(f"Ingrese el número {i + 1} (0-100): "))
        if numero == 100:
            contador_cien += 1
        elif 50 < numero < 100:
            contador_mayores_50 += 1
        elif 0 < numero < 50:
            contador_menores_50 += 1

    print(f"Usando for: Números iguales a 100: {contador_cien}, Mayores a 50 y menores a 100: {contador_mayores_50}, Menores a 50 y mayores a 0: {contador_menores_50}")
multiplicacion_por_sumas_sucesivas()
contar_numeros()
