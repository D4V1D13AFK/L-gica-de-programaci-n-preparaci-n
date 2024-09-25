#5. Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar cuál es la
#fila que tiene la mayor suma.

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

suma_may = 0
suma = 0
fila_mayor = 0  # Inicializar fila_mayor

# Llenar la matriz con los valores ingresados por el usuario
for i in range(4):
    for j in range(3):
        num = int(input("Introduce un número: "))
        matrix[i][j] = num

print(matrix)

# Calcular la suma de cada fila y determinar cuál tiene la mayor suma
for i in range(4):
    suma = 0
    for j in range(3):
        suma += matrix[i][j]
    if suma > suma_may:  # Comparar si la suma actual es mayor que la anterior
        suma_may = suma
        fila_mayor = i  # Guardar el índice de la fila con la mayor suma

print(f"La fila {fila_mayor} tiene la mayor suma: {suma_may}")




