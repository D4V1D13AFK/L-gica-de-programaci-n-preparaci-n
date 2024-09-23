#Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.
num = int(input("Ingresa el primer número: "))
mayor = num

num = int(input("Ingresa el segundo número: "))
if num > mayor:
    mayor = num

num = int(input("Ingresa el tercer número: "))
if num > mayor:
    mayor = num

print("El número mayor es:", mayor)
