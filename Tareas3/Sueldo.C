#include <stdio.h>

int main() {
    float sueldo_base, venta1, venta2, venta3, comision, total_comisiones, sueldo_total;
        printf("Ingresa el sueldo base del vendedor: ");
        scanf("%f", &sueldo_base);
        printf("Ingresa el importe de la primera venta: ");
        scanf("%f", &venta1);
        printf("Ingresa el importe de la segunda venta: ");
        scanf("%f", &venta2);
        printf("Ingresa el importe de la tercera venta: ");
        scanf("%f", &venta3);
    comision = 0.10;
    total_comisiones = (venta1 + venta2 + venta3) * comision;
    sueldo_total = sueldo_base + total_comisiones;
    printf("El total de comisiones por las ventas es: %.2f\n", total_comisiones);
    printf("El sueldo total del mes (base + comisiones) es: %.2f\n", sueldo_total);
    return 0;
}
