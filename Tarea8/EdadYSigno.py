from datetime import datetime

def calcular_edad(dia_nac, mes_nac, anio_nac):
    hoy = datetime.now()
    edad = hoy.year - anio_nac - ((hoy.month, hoy.day) < (mes_nac, dia_nac))
    return edad

def obtener_signo_zodiacal(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        signo = "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo = "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        signo = "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        signo = "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo = "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo = "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo = "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo = "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        signo = "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo = "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        signo = "Sagitario"
    else:  
        signo = "Capricornio"
    return signo

def programa_anios_y_signo():
    print("==================================")
    print("PROGRAMA AÑOS Y SIGNO")
    print("1. Calcular tu edad.")
    print("2. Saber tu signo zodiacal.")
    print("==================================")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":  # Estructura selectiva doble
        print("\n--- Cálculo de Edad ---")
        dia_nac = int(input("Ingresa tu día de nacimiento: "))
        mes_nac = int(input("Ingresa tu mes de nacimiento (1-12): "))
        anio_nac = int(input("Ingresa tu año de nacimiento: "))
        
        edad = calcular_edad(dia_nac, mes_nac, anio_nac)
        print(f"Tienes {edad} años.")
    
    elif opcion == "2":  # Estructura selectiva múltiple
        print("\n--- Cálculo de Signo Zodiacal ---")
        dia = int(input("Ingresa tu día de nacimiento: "))
        mes = int(input("Ingresa tu mes de nacimiento (1-12): "))
        
        signo = obtener_signo_zodiacal(dia, mes)
        print(f"Tu signo zodiacal es {signo}.")
    
    else:
        print("Opción no válida. Por favor elige entre 1 o 2.")
programa_anios_y_signo()
