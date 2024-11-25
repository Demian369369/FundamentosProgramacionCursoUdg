def registrar_ventas(ventas):
    for mes in range(12):
        for agencia in range(5):
            ventas[mes][agencia] = float(input(f"Ingrese ventas para Mes {mes+1}, Agencia {agencia+1}: "))

def mostrar_resumen(ventas):
    for agencia in range(5):
        total_agencia = sum(ventas[mes][agencia] for mes in range(12))
        print(f"Agencia {agencia+1}: Total Ventas = {total_agencia}")

def total_agencia_3(ventas):
    total = sum(ventas[mes][2] for mes in range(12))
    print(f"Total de ventas de la Agencia 3: {total}")

def promedio_diciembre(ventas):
    promedio = sum(ventas[11]) / len(ventas[11])
    print(f"Promedio de ventas en diciembre: {promedio:.2f}")

def mayores_ventas_mayo(ventas):
    ventas_mayo = [ventas[4][agencia] for agencia in range(5)]
    max_ventas = max(ventas_mayo)
    agencia_max = ventas_mayo.index(max_ventas) + 1
    print(f"Agencia con mayores ventas en mayo: Agencia {agencia_max} con {max_ventas} ventas")

def menores_ventas_anuales(ventas):
    ventas_totales_mensuales = [sum(ventas[mes]) for mes in range(12)]
    min_ventas = min(ventas_totales_mensuales)
    mes_min = ventas_totales_mensuales.index(min_ventas) + 1
    print(f"Mes con menores ventas: Mes {mes_min} con {min_ventas} ventas")

def main():
    ventas = [[0 for _ in range(5)] for _ in range(12)]  # Matriz de 12x5 
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar ventas")
        print("2. Mostrar resumen de ventas")
        print("3. Total de ventas de la Agencia 3")
        print("4. Promedio de ventas en diciembre")
        print("5. Agencia con mayores ventas en mayo")
        print("6. Mes con menores ventas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_ventas(ventas)
        elif opcion == "2":
            mostrar_resumen(ventas)
        elif opcion == "3":
            total_agencia_3(ventas)
        elif opcion == "4":
            promedio_diciembre(ventas)
        elif opcion == "5":
            mayores_ventas_mayo(ventas)
        elif opcion == "6":
            menores_ventas_anuales(ventas)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
if __name__ == "__main__":
    main()
