#8. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se
#encuentran los números terminados en 4.

vector = [0]*10
posiciones = []
contador = 0 
 
for i in range(10):
    num = int(input("introduce un número: "))
    vector[i]=num

print(vector)

for j in vector:
    if j % 10 == 4:
        print(f"el número {j} termina en 4 y esta en la posición: {contador}") 
    contador+=1
    







        


        
       

