def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Calcular la potencia de un número")
    print("2. Calcular el promedio de alturas")
    print("3. Calcular el factorial de un número")
    print("4. Salir")
def calcular_potencia():
    while True:
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        resultado = 1
        for _ in range(abs(exponente)):
            resultado *= base
        if exponente < 0:  
            resultado = 1 / resultado
        print(f"La potencia de {base} ^ {exponente} es {resultado}")
        
        if not desea_continuar("¿Desea realizar otro cálculo de potencia?"):
            break
def calcular_promedio_alturas():
    while True:
        cantidad = int(input("Ingrese la cantidad de personas: "))
        if cantidad <= 0:
            print("La cantidad de personas debe ser mayor a cero.")
            continue
        suma_alturas = 0.0
        for i in range(1, cantidad + 1):
            altura = float(input(f"Ingrese la altura de la persona {i} (en metros): "))
            suma_alturas += altura
        promedio = suma_alturas / cantidad
        print(f"El promedio de alturas es: {promedio:.2f} metros.")
        if not desea_continuar("¿Desea calcular otro promedio de alturas?"):
            break
def calcular_factorial():
    while True:
        numero = int(input("Ingrese un número entero no negativo: "))
        if numero < 0:
            print("El factorial solo se calcula para números no negativos.")
            continue
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es {factorial}")
        if not desea_continuar("¿Desea calcular otro factorial?"):
            break
def desea_continuar(mensaje):
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Opción inválida. Por favor, ingrese 's' para sí o 'n' para no.")
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            calcular_potencia()
        elif opcion == "2":
            calcular_promedio_alturas()
        elif opcion == "3":
            calcular_factorial()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
main()
