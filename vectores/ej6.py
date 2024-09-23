#6. Leer dos números enteros y almacenar en un vector los 10 primeros números primos
#comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla.

vector = [0]*10
num1 = int(input("introduce el primer número: "))
num2 = int(input("introduce el segundo número: "))
contador = 0 

def es_primo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

if num1 > num2:
    for j in range(num2,num1+1):
        if es_primo(j) is True:
            vector[contador] = j
            contador+=1
        if contador == 10:
            break 

if num2 > num1:
    for j in range(num1,num2+1):
        if es_primo(j) is True:
            vector[contador] = j
            contador+=1
        if contador == 10:
            break 

print(vector)