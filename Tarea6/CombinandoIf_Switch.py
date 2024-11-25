def tipo_alumno_if(calificacion):
    if calificacion == 100:
        return "EXCELENTE"
    elif 90 <= calificacion <= 99:
        return "MUY BUENO"
    elif 80 <= calificacion <= 89:
        return "BUENO"
    elif 70 <= calificacion <= 79:
        return "REGULAR"
    elif 60 <= calificacion <= 69:
        return "MALO"
    elif 0 <= calificacion <= 59:
        return "=( (Insuficiente)"
    else:
        return "Calificación inválida"
def tipo_alumno_switch(calificacion):
    tipos = [
        "=( (Insuficiente)",  # 0-59
        "MALO",               # 60-69
        "REGULAR",            # 70-79
        "BUENO",              # 80-89
        "MUY BUENO",          # 90-99
        "EXCELENTE"           # 100
    ]
    if 0 <= calificacion <= 59:
        return tipos[0]
    elif 60 <= calificacion <= 69:
        return tipos[1]
    elif 70 <= calificacion <= 79:
        return tipos[2]
    elif 80 <= calificacion <= 89:
        return tipos[3]
    elif 90 <= calificacion <= 99:
        return tipos[4]
    elif calificacion == 100:
        return tipos[5]
    else:
        return "Calificación inválida"
def main():
    while True:
        try:
            print("\n*** Menú Principal ***")
            print("1. Usar if-elif-else")
            print("2. Usar switch-case simplificado")
            print("3. Salir")
            opcion = int(input("Introduce tu opción: "))
            if opcion == 3:
                print("Saliendo del programa...")
                break
            calificacion = int(input("Introduce la calificación del alumno (0-100): "))
            if opcion == 1:
                tipo = tipo_alumno_if(calificacion)
            elif opcion == 2:
                tipo = tipo_alumno_switch(calificacion)
            else:
                print("Opción no válida")
                continue
            print(f"El tipo de alumno es: {tipo}")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
if __name__ == "__main__":
    main()
