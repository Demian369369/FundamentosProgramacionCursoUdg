// #include <stdio.h>
int main() {
    int minutos, horas, minutos_restantes;
    printf("Ingresa la cantidad de minutos: ");
    scanf("%d", &minutos);
    horas = minutos / 60; 
    minutos_restantes = minutos % 60;  
    printf("%d minutos son %d horas y %d minutos.\n", minutos, horas, minutos_restantes);
    return 0;
}
