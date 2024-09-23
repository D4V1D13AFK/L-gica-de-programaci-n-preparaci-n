#1. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor
#número leído.
vector = [0]*10
pos_may = 0
may_num = None

for i in range(10):
    num = int(input("introduce un número: "))
    vector[i]=num

    if may_num is None or num > may_num:
        may_num = num
        pos_may = i

print(f"el número mayor esta en la posición {pos_may}")



