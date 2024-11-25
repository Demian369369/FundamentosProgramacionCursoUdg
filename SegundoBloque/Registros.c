#include <stdio.h>
#include <string.h>
struct Direccion {
    char calle[100];
    int numero;
};

struct Persona {
    char nombre[50];
    int edad;
    struct Direccion direccion; 
};
void inicializarPersona(struct Persona *p, const char *nombre, int edad, const char *calle, int numero) {
    strcpy(p->nombre, nombre);
    p->edad = edad;
    strcpy(p->direccion.calle, calle);
    p->direccion.numero = numero;
}

int main() {
    struct Persona personas[2];
    inicializarPersona(&personas[0], "Juan", 30, "Av. Libertad", 123);
    inicializarPersona(&personas[1], "Ana", 25, "Calle Fenix", 456);
    for (int i = 0; i < 2; i++) {
        printf("Nombre: %s, Edad: %d\n", personas[i].nombre, personas[i].edad);
        printf("Direccion: %s %d\n", personas[i].direccion.calle, personas[i].direccion.numero);
    }
    struct Persona personas2[2][2];
    inicializarPersona(&personas2[0][0], "Carlos", 40, "Calle Sol", 789);
    inicializarPersona(&personas2[0][1], "Maria", 35, "Calle Luna", 101);
    printf("\nArreglo bidimensional:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("Persona %d-%d: %s, Edad: %d\n", i, j, personas2[i][j].nombre, personas2[i][j].edad);
            printf("Direccion: %s %d\n", personas2[i][j].direccion.calle, personas2[i][j].direccion.numero);
        }
    }
    return 0;
}
