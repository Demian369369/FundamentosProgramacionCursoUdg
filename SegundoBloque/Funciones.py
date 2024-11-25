n_terminos = 5 
serie = []  
def mostrar_mensaje():
    """Imprime un mensaje inicial"""
    print("\n** Programa de ejemplo con funciones y recursividad **")
    print("Este programa genera los primeros términos de la serie de Fibonacci.\n")
def calcular_fibonacci():
    """Genera la serie de Fibonacci de forma recursiva"""
    if len(serie) < 2:  
        serie.append(1 if len(serie) == 0 else 1)
    else:  
        serie.append(serie[-1] + serie[-2])
    if len(serie) < n_terminos:  
        calcular_fibonacci()
def mostrar_serie():
    """Muestra la serie generada"""
    print("Serie de Fibonacci generada:")
    print(" -> ".join(map(str, serie)))
def main():
    mostrar_mensaje()
    calcular_fibonacci()
    mostrar_serie()
main()
