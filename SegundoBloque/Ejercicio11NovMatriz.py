filas = 3
columnas = 5
matriz = []
print("Ingrese 15 números para llenar la matriz de 3x5:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = int(input(f"Ingrese el número para la posición [{i+1},{j+1}]: "))
        fila.append(numero)
    matriz.append(fila)
suma_filas = [sum(fila) for fila in matriz]
mayor_suma = max(suma_filas)
fila_mayor_suma = suma_filas.index(mayor_suma) + 1  
print("\nMatriz de 3x5:")
for fila in matriz:
    print("\t".join(map(str, fila)))
print("\nSuma de cada fila:")
for i, suma in enumerate(suma_filas, start=1):
    print(f"Suma de la fila {i}: {suma}")

print(f"\nLa fila con la mayor suma es la fila {fila_mayor_suma} con una suma de {mayor_suma}.")
