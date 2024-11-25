graph TD
    A[Inicio] --> B[Mostrar Menú Principal]
    B --> C{Elegir opción}
    C -->|Opción 1| D[Usar if-elif-else]
    C -->|Opción 2| E[Usar switch-case simplificado]
    C -->|Opción 3| F[Salir del programa]
    D --> G[Ingresar calificación]
    E --> G
    G --> H{Validar calificación}
    H -->|Válida| I{Determinar tipo de alumno}
    H -->|Inválida| J[Mostrar "Calificación inválida"]
    I -->|100| K[EXCELENTE]
    I -->|90-99| L[MUY BUENO]
    I -->|80-89| M[BUENO]
    I -->|70-79| N[REGULAR]
    I -->|60-69| O[MALO]
    I -->|0-59| P["=( (Insuficiente)"]
    K --> Q[Mostrar resultado]
    L --> Q
    M --> Q
    N --> Q
    O --> Q
    P --> Q
    J --> Q
    Q --> R{Continuar?}
    R -->|Sí| B
    R -->|No| S[Fin]
    F --> S