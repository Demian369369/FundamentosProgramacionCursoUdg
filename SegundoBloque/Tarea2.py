def llenar_vector():
    vector = []
    for i in range(10):
        while True:
            try:
                valor = int(input(f"Ingrese el elemento {i + 1} del vector (entero): "))
                vector.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return vector
def opcion_inversa():
    print("\n--- Opción 1: Inversa ---")
    vector = llenar_vector()
    vector_inverso = vector[::-1]
    print("Vector original:", vector)
    print("Vector inverso:", vector_inverso)
def opcion_numero_mayor():
    print("\n--- Opción 2: Número Mayor ---")
    vector = llenar_vector()
    max_valor = max(vector)
    max_indice = vector.index(max_valor)
    print(f"El valor máximo es {max_valor} en la posición {max_indice}")
def opcion_nombre_domicilio():
    print("\n--- Opción 3: Nombre y Domicilio ---")
    nombre = input("Ingrese su nombre: ")
    domicilio = input("Ingrese su domicilio: ")
    print(f"Nombre: {nombre}")
    print(f"Domicilio: {domicilio}")
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Inversa")
        print("2. Número Mayor")
        print("3. Nombre y Domicilio")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            opcion_inversa()
        elif opcion == '2':
            opcion_numero_mayor()
        elif opcion == '3':
            opcion_nombre_domicilio()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
            continue
        regresar = input("\n¿Desea regresar al menú principal? (s/n): ").strip().lower()
        if regresar != 's':
            print("Saliendo del programa...")
            break
menu()
