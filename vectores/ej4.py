#4. Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y
#mostrarlo en pantalla.
vector = [0]*10

a,b = 0,1

for i in range(10):
    vector[i] = a
    a , b = b , a + b
print(vector)