#20. Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los elementos de
#una de las matrices es igual a cada uno de los elementos de la otra matriz multiplicado por el entero
#leído.

matrix = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

matrix_2 = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

respuesta = 0
respuesta_2 = 0

for i in range(4):
    for j in range(5):
        num = int(input("introduce un número a la matriz 1: "))
        matrix[i][j]=num

print("comienza la segunda matriz")

for k in range(4):
    for l in range(5):
        num2 = int(input("introduce un número a la matriz 2: "))
        matrix_2[k][l]=num2

entero = int(input("introduce un entero: "))

print(matrix)
print(matrix_2)

for m in range(4):
    for n in range(5):
        if matrix[m][n] == entero * matrix_2[m][n]:
            respuesta += 1

for m in range(4):
    for n in range(5):
        if matrix_2[m][n] == entero * matrix[m][n]:
            respuesta_2 += 1



if respuesta == 20 or respuesta_2 == 20:
    print("es verdadero una matriz es resultado de la otra al ser multiplicada por el entero elegido")
else:
    print("ningua matriz al ser multiplicada por el entero da como resultado la otra")         




