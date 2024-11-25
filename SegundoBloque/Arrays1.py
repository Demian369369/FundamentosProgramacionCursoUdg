def obtener_arreglo(nombre_arreglo):
    arreglo = []
    for i in range(3):
        while True:
            try:
                valor = input(f"Ingrese el elemento {i + 1} del {nombre_arreglo}: ")
                if not valor.isnumeric():
                    print("Entrada inválida. Por favor, ingrese un número entero.")
                    continue
                valor = int(valor)
                if abs(valor) > 10**6: 
                    print("El número es demasiado grande. Ingrese un número entre -1,000,000 y 1,000,000.")
                    continue
                arreglo.append(valor)
                break 
            except ValueError:
                print("Entrada inválida. Por favor, intente de nuevo.")
    return arreglo
arreglo_usuario = obtener_arreglo("arreglo de 3 elementos")
print("Los elementos ingresados son:")
print(arreglo_usuario)
