matriz = []

print("Introduce los valores para la matriz 3x3:")

for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese el valor para la posición [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz 3x3:")
for fila in matriz:
    print("\t".join(map(str, fila)))
