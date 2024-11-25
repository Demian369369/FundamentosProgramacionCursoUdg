def solicitar_matriz():
    while True:
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        if filas == columnas:
            print("La matriz es cuadrada.")
            return filas, columnas
        else:
            print("La matriz no es cuadrada. Por favor ingrese nuevamente.")
def llenar_matriz(filas, columnas):
    matriz = []
    print("Ingrese los valores para la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la posición [{i+1},{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
def imprimir_matriz(matriz):
    print("\nMatriz:")
    for fila in matriz:
        print("\t".join(map(str, fila)))
filas, columnas = solicitar_matriz()
matriz = llenar_matriz(filas, columnas)
imprimir_matriz(matriz)
