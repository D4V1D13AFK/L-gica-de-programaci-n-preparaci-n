#6. Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila.
matrix = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

num_may = 0
suma_may = 0

for i in range(4):
    for j in range(4):
        num = int(input("introduce un número a la matriz: "))
        matrix[i][j] = num

print(matrix)

for i in range(4):
    num_may = 0
    for j in range(4):
        if  num_may == 0 or matrix[i][j] > num_may:
            num_may = matrix[i][j]
    suma_may+=num_may

promedio = suma_may/4
print(promedio)