//#include <stdio.h>
int main() {
    float pesos, tasaCambio, dolares;
    printf("Ingresa la cantidad de pesos: ");
    scanf("%f", &pesos);
    printf("Ingresa la tasa de cambio (pesos por dólar): ");
    scanf("%f", &tasaCambio);
    dolares = pesos / tasaCambio;
    printf("La cantidad en dólares es: %.2f\n", dolares);
    return 0;
}
