def obtener_arreglo(nombre_arreglo):
    arreglo = []
    for i in range(5):
        while True:
            try:
                valor = input(f"Ingrese el elemento {i + 1} del {nombre_arreglo} (debe ser un entero): ")
                valor = int(valor)
                if abs(valor) > 10**6:  
                    print("El número es demasiado grande. Ingrese un número entre -1,000,000 y 1,000,000.")
                    continue
                arreglo.append(valor)
                break  
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return arreglo
arreglo1 = obtener_arreglo("primer arreglo")
arreglo2 = obtener_arreglo("segundo arreglo")
arreglo_suma = []
for i in range(5):
    suma = arreglo1[i] + arreglo2[i]
    arreglo_suma.append(suma)
print("El arreglo resultante de la suma es:")
print(arreglo_suma)
