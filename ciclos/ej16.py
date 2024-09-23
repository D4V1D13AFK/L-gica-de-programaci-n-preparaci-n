#Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n leído.

# Leer el número n
n = int(input("Introduce el valor de n: "))

# Inicializar la suma de los múltiplos
suma_multiplos = 0

# Usar un bucle for para calcular la suma de los primeros n múltiplos de 3
for i in range(1, n + 1):
    multiplo = 3 * i
    suma_multiplos += multiplo

# Calcular el promedio entero
promedio_entero = suma_multiplos // n  # División entera

# Mostrar el promedio entero
print(f"El promedio entero de los primeros {n} múltiplos de 3 es: {promedio_entero}")
