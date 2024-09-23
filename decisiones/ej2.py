#2. Leer un número entero y determinar si tiene 3 dígitos.

num = int(input("introduce un número: "))

if num > 99 and num < 1000:
    print("el número tiene 3 digitos")
else:
    print("el número no tiene 3 digitos")