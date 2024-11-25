#Hola maestra, este es mi codigo en python, si desea ejecutarlo simplemente tiene que tener un software que
#Permita python y un interprete para compilar el codigo
#Le recomiendo usar Vscode e instalar la extension de python, de esa manera sera facil ya que solo es picarle play



#Los def son funciones pero aqui en python tienen la posibilidad de ser usados como un switch case
def calcular_precio_unitario(precio_base, iva=0.16):
    """Calcula el precio unitario con IVA."""
    return precio_base * (1 + iva)


#Estas serian las "Posibilidades" dentro del switch case
def calcular_descuento(total_sin_descuento, forma_pago):
    """Calcula el descuento según la forma de pago."""
    if forma_pago == 1:  # Esto seria para Efectivo
        return total_sin_descuento * 0.10
    elif forma_pago == 2:  # Esto seria para Tarjeta de crédito
        return total_sin_descuento * 0.05
    elif forma_pago == 3:  # Esto es del Vale de regalo
        return total_sin_descuento * 0.15
    else:
        return 0

#Un switch case para los detalles 
def mostrar_detalle(cantidad_impresoras, precio_unitario_con_iva, total_sin_descuento, forma_pago, descuento, total_a_pagar):
    """Muestra el detalle del pago."""
    formas_pago = {
        1: "Efectivo",
        2: "Tarjeta de crédito",
        3: "Vale de regalo"
    }

#Esto para mostrar en consola
    print(f"\n--- Detalle del Pago ---")
    print(f"Cantidad de impresoras a comprar: {cantidad_impresoras}")
    print(f"Precio unitario (con IVA): ${precio_unitario_con_iva:.2f}")
    print(f"Total sin descuento: ${total_sin_descuento:.2f}")
    print(f"Forma de pago: {formas_pago.get(forma_pago, 'Forma de pago no válida')}")
    print(f"Descuento realizado: ${descuento:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")

def main():
    # Constantes
    PRECIO_UNITARIO = 5000.00  # Precio sin IVA
    IVA = 0.16  # 16%

    # Entrada de datos
    cantidad_impresoras = int(input("Ingrese la cantidad de impresoras a comprar: "))
    print("Seleccione la forma de pago:")
    print("1. Efectivo")
    print("2. Tarjeta de crédito")
    print("3. Vale de regalo")
    forma_pago = int(input("Ingrese el número de la forma de pago: "))

    # Cálculos
    precio_unitario_con_iva = calcular_precio_unitario(PRECIO_UNITARIO, IVA)
    total_sin_descuento = cantidad_impresoras * precio_unitario_con_iva
    descuento = calcular_descuento(total_sin_descuento, forma_pago)
    total_a_pagar = total_sin_descuento - descuento

    # Mostrar resultados
    mostrar_detalle(cantidad_impresoras, precio_unitario_con_iva, total_sin_descuento, forma_pago, descuento, total_a_pagar)

# Esto ayuda a ejecutar el programa maestra(Es para ejecutar el main y es basicamente para activar las funciones)
#Parecido a un while, es como un ciclo boleano que dice que si hay main, llame a main
if __name__ == "__main__":
    main()
