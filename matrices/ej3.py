#3.Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los números
#pares.

matrix = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(3):
    for j in range(4):
        num = int(input("introduce un número: "))
        matrix[i][j] = num

print(matrix)

for i in range(3):
    for j in range(4):
        if matrix[i][j] % 2 == 0:
            print(f"{matrix[i][j]} es par y esta en la fila: { i} y en la columna:{ j}")
