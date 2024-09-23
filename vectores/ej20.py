vector = [0]*10
min_prim = None
pos_prim = None

def es_primo(n):
    if n < 2:
        return False
    for j in range(2,n):
        if n % j == 0:
            return False
    return True
 
for i in range(10):
    num = int(input("introduce un número: "))
    vector [i] = num
    if es_primo(num) is True:
        if min_prim is None or num < min_prim:
            min_prim = num
            pos_prim = i

print("Vector:", vector)
if pos_prim is not None:
    print("Posición del número primo mínimo:", pos_prim)
else:
    print("No se encontraron números primos.")



