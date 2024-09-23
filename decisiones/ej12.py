#12. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.

num = int(input("introduce un número: "))
num2 = int(input("introduce un número: "))

if num > 9 and num < 100 and num2 > 9 and num2 < 100:
    d1 = num//10
    u1 = num%10
    d2 = num2//10
    u2 = num2%10

    if d1==d2 or d1==u2 or u1==u2 or u1==d2:
        print("tienen números en común")
    else:
        print("no tienen números en común")

else:
    print(" algun número  es invalido")


