#3. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor
#número primo leído.
vector = [0] * 10
num_mayor = None
pos_mayor = -1

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(10):
    num = int(input("Introduce un número: "))
    vector[i] = num
    if es_primo(num):
        if num_mayor is None or num > num_mayor:
            num_mayor = num
            pos_mayor = i

if pos_mayor != -1:
    print(f"El número primo mayor es {num_mayor} y se encuentra en la posición {pos_mayor}.")
else:
    print("No hay números primos en el vector.")









