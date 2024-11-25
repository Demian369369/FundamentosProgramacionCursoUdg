sueldo_base = float(input("Ingresa el sueldo base del vendedor: "))
venta1 = float(input("Ingresa el importe de la primera venta: "))
venta2 = float(input("Ingresa el importe de la segunda venta: "))
venta3 = float(input("Ingresa el importe de la tercera venta: "))
comision = 0.10
total_comisiones = (venta1 + venta2 + venta3) * comision
sueldo_total = sueldo_base + total_comisiones
print(f"El total de comisiones por las ventas es: {total_comisiones:.2f}")
print(f"El sueldo total del mes (base + comisiones) es: {sueldo_total:.2f}")
