#7. Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados en 0

matrix = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(4):
    for j in range(4):
        num = int(input("introduce un número a la matriz: "))
        matrix [i][j] = num

print(matrix)

for i in range(4):
    for j in range(4):
        if matrix[i][j] > 9:
            if matrix[i][j] % 10 == 0:
             print(f"el número: {matrix[i][j]} termina en 0 y esta e la fila: {i} y en la columna: {j}")