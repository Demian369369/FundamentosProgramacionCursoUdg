sucursales = 4
meses = 6
ventas = []
print("Ingrese las ventas mensuales para cada sucursal (en pesos):")
for i in range(sucursales):
    fila = []
    for j in range(meses):
        venta = float(input(f"Ventas de la Sucursal {i+1} en el mes {j+1}: "))
        fila.append(venta)
    ventas.append(fila)
venta_total = sum(sum(fila) for fila in ventas)
ventas_por_sucursal = [sum(fila) for fila in ventas]
mayor_venta = max(ventas_por_sucursal)
menor_venta = min(ventas_por_sucursal)
sucursal_mayor_venta = ventas_por_sucursal.index(mayor_venta) + 1
sucursal_menor_venta = ventas_por_sucursal.index(menor_venta) + 1
print("\nMatriz de ventas mensuales (sucursales x meses):")
for i, fila in enumerate(ventas, start=1):
    print(f"Sucursal {i}: " + "\t".join(f"{venta:.2f}" for venta in fila))
print(f"\nVenta total por todas las tiendas: ${venta_total:.2f}")
for i, total in enumerate(ventas_por_sucursal, start=1):
    print(f"Venta total de la Sucursal {i}: ${total:.2f}")
print(f"Sucursal que más vendió: Sucursal {sucursal_mayor_venta} con ${mayor_venta:.2f}")
print(f"Sucursal que menos vendió: Sucursal {sucursal_menor_venta} con ${menor_venta:.2f}")
