#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros
#comprendidos entre 1 y el número leído.
num = int(input("introduce un número: "))
suma = 0
for i in range(1,num+1):
    suma+=i
print(suma)

