from datetime import datetime

def fecha_valida(fecha_str):
    """
    Comprueba si una fecha ingresada es válida.
    """
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def es_bisiesto(anio):
    """
    Comprueba si un año es bisiesto.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def calcular_edad(fecha_actual_str, fecha_nacimiento_str):
    """
    Calcula la edad basada en la fecha actual y la fecha de nacimiento.
    """
    fecha_actual = datetime.strptime(fecha_actual_str, "%d/%m/%Y")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad
def main():
    while True:
        fecha_actual = input("Ingresa la fecha actual (dd/mm/yyyy): ")
        if fecha_valida(fecha_actual):
            break
        print("Fecha inválida. Intenta de nuevo.")

    n = int(input("¿Cuántas personas deseas registrar? "))
    for i in range(n):
        print(f"\nPersona {i + 1}:")
        
        while True:
            fecha_nacimiento = input("Ingresa la fecha de nacimiento (dd/mm/yyyy): ")
            if fecha_valida(fecha_nacimiento):
                break
            print("Fecha inválida. Intenta de nuevo.")
        
        anio_nacimiento = int(fecha_nacimiento.split("/")[-1])
        if es_bisiesto(anio_nacimiento):
            print(f"El año {anio_nacimiento} es bisiesto.")
        else:
            print(f"El año {anio_nacimiento} no es bisiesto.")
        
        edad = calcular_edad(fecha_actual, fecha_nacimiento)
        print(f"La edad de la persona es: {edad} años.")

if __name__ == "__main__":
    main()
