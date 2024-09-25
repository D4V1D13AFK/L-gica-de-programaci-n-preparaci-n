#4. Leer una matriz 4x3 entera y determinar en qué posiciones exactas se encuentran los números
#primos

matrix = [[0,0,0],
          [0,0,0],
          [0,0,0],
          [0,0,0]]

def es_primo(n):
    if n < 2:
        return False
    for k in range(2,n):
        if n % k == 0:
            return False
    return True


for i in range(4):
    for j in range(3):
        num = int(input("introduce un número: "))
        matrix [i][j] = num

print(matrix)

for i in range(4):
    for j in range(3):
        if es_primo(matrix[i][j]) is True:
            print(f"el número: {matrix[i][j]} es primo y esta en la fila: {i} y en la columna: {j}") 



