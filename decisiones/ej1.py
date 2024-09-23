#1. Leer un número entero y determinar si es un número terminado en 4.

num = int(input("introduce un número: "))

unidades = num%10

if unidades == 4:
    print("el número termina en 4")
else:
    print("el número no termina en 4")