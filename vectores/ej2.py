#2. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor
#número par leído.
vector = [0] * 10
num_mayor = None
pos_mayor = -1  # Inicializamos en -1

for i in range(10):
    num = int(input("Introduce un número: "))
    vector[i] = num
    if num % 2 == 0:  # Verificamos si el número es par
        if num_mayor is None or num > num_mayor:
            num_mayor = num  # Guardamos el mayor número par
            pos_mayor = i  # Guardamos la posición del mayor número par

print(vector)
if pos_mayor != -1:
    print(f"El mayor número par es {num_mayor} y está en la posición {pos_mayor}.")
else:
    print("No se ingresaron números pares.")








