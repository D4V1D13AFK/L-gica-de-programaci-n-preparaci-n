#20.Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales

matrix = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

matrix_2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

respuesta = 0

for i in range(4):
    for j in range(5):
        num = int(input("introduce un número en la matriz 1: "))
        matrix[i][j] = num

for k in range(4):
    for l in range(5):
        num2 = int(input("introduce un número en la matriz 2: "))
        matrix_2 [k][l] = num2

print(matrix)
print(matrix_2)

for m in range(4):
    for n in range(5):
        if matrix[m][n] != matrix_2[m][n]:
            respuesta += 1

if respuesta > 0:
    print("las matrices no son iguales")
else:
    print("las matrices son iguales")
            
