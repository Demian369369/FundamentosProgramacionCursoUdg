def mayor_de_tres_numeros(a, b, c):
    return max(a, b, c)
def menor_de_tres_numeros(a, b, c):
    return min(a, b, c)
def promedio_de_tres_numeros(a, b, c):
    return (a + b + c) / 3
def menu():
    print("Ejercicios Switch")
    print("1. Mayor de 3 números.")
    print("2. Menor de 3 números.")
    print("3. Promedio de 3 números.")
    print("4. Salir.")
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion == 4:
                print("Saliendo del programa.")
                break
            if opcion in [1, 2, 3]:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                c = float(input("Ingrese el tercer número: "))
            switcher = {
                1: lambda: print(f"El mayor de los tres números es: {mayor_de_tres_numeros(a, b, c)}"),
                2: lambda: print(f"El menor de los tres números es: {menor_de_tres_numeros(a, b, c)}"),
                3: lambda: print(f"El promedio de los tres números es: {promedio_de_tres_numeros(a, b, c)}"),
            }
            func = switcher.get(opcion, lambda: print("Opción no válida. Inténtelo de nuevo."))
            func()
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
menu()
