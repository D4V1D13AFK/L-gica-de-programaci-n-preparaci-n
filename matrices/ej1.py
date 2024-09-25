# Definición de la matriz 4x4
matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Usar un bucle for con índices fijos para llenar la matriz
for filas in range(4):  # Suponiendo que hay 4 filas
    for columnas in range(4):  # Suponiendo que hay 4 columnas
        num = int(input("Introduce un número: "))
        matrix[filas][columnas] = num  # Asigna el número ingresado a la posición correspondiente

print("Matriz ingresada:")
print(matrix)

# Inicializar variables para encontrar el número mayor
mayor = matrix[0][0]  # Suponemos que el primer elemento es el mayor
fila_mayor = 0
columna_mayor = 0

# Buscar el número mayor en la matriz
for filas in range(4):
    for columnas in range(4):
        if matrix[filas][columnas] > mayor:
            mayor = matrix[filas][columnas]  # Actualizar el mayor
            fila_mayor = filas  # Actualizar la fila del mayor
            columna_mayor = columnas  # Actualizar la columna del mayor

# Mostrar el resultado
print(f"El número mayor es {mayor} ubicado en la fila {fila_mayor} y columna {columna_mayor}.")

   

