#5. Almacenar en un vector de 10 posiciones los 10 números primos comprendidos entre 100 y 300.
#Luego mostrarlos en pantalla.

vector = [0]*10
contador = 0

def es_primo(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for j in range(100,300):
    if es_primo(j) is True:
        vector[contador]=j
        contador += 1
        if contador == 10:
            break

print(vector)


    




