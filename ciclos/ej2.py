#2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

num = int(input("introduce un número: "))

for i in range(1,num):
    if i % 2 == 0:
        print(i)
