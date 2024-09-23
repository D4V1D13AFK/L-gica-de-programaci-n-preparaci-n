#20. Leer tres números enteros y mostrarlos ascendentemente.
num = int(input("introduce un número: "))
num2 = int(input("introduce otro número: "))
num3 = int(input("introduce otro número: "))

#caso1
if num < num2 and num < num3:
    if num2 < num3:
        print(num)
        print(num2)
        print(num3)
    else:
        print(num)
        print(num3)
        print(num2)
#caso2
if num2 < num and num2 < num3:
    if num < num3:
        print(num2)
        print(num)
        print(num3)
    else:
        print(num2)
        print(num3)
        print(num)

#caso3
if num3 < num2 and num3 < num:
    if num2 < num:
        print(num3)
        print(num2)
        print(num)
    else:
        print(num3)
        print(num)
        print(num2)

    
