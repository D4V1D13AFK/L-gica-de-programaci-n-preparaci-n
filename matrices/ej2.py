#3. Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los números
#pares
matriz = [[1, 2, 3, 4],
          [5, 4, 6, 10],
          [78, 51, 42, 63]]

contador_filas = 0

for filas in matriz:
    contador_filas += 1
    contador_column = 0  # Reiniciar el contador de columnas para cada fila
    for columnas in filas:
        contador_column += 1
        if columnas % 2 == 0:
            print(f"el número {columnas} es par y está en la fila {contador_filas} y en la columna {contador_column}")
