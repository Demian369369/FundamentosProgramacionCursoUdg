#include <stdio.h>
int main() {
    int edad;
    int costo;
    printf("Ingrese su edad: ");
    scanf("%d", &edad);
    int rango;
    if (edad < 18) {
        rango = 1; 
    } else if (edad <= 50) {
        rango = 2; 
    } else {
        rango = 3; 
    }
    switch (rango) {
        case 1:
            costo = 60;
            break;
        case 2:
            costo = 80;
            break;
        case 3:
            costo = 50;
            break;
        default:
            printf("Edad inválida.\n");
            return 1;
    }
    printf("El costo de la entrada es: $%d pesos\n", costo);
    return 0;
}
