#17. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y
#primeros múltiplos de 5 para valores de x y y leídos.

multiplos_2 = int(input("introduce un número: "))
multiplos_5 = int(input("introduce un número: "))

suma_2 = 0 
suma_5 = 0

for i in range(1,multiplos_2+1):
    suma_2+=i*2

for j in range(1,multiplos_5+1):
    suma_5+=j*5

promedio_2 = suma_2/multiplos_2
promedio_5 = suma_5/multiplos_5

if promedio_2 > promedio_5:
    print("el promedio de los multiplos de 2 es mayor al de los mutiplos de 5")
elif promedio_2 == promedio_5:
    print("los dos promedios son iguales")
else:
    print("el promedio de los multiplos de 5 es mayor al de los mutiplos de 2")