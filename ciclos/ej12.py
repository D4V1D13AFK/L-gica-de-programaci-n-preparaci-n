# Solicitar al usuario que ingrese un número entero de 3 dígitos
numero = int(input("Ingresa un número entero de 3 dígitos: "))

# Inicializamos una variable para indicar si hemos encontrado el dígito 1
tiene_uno = False

# Iteramos sobre los dígitos del número usando operaciones aritméticas
for i in range(3):
    digito = numero % 10  # Obtenemos el último dígito del número
    if digito == 1:
        tiene_uno = True
        break
    numero = numero // 10  # Eliminamos el último dígito del número

# Mostramos el resultado
if tiene_uno:
    print("El número tiene el dígito 1.")
else:
    print("El número no tiene el dígito 1.")




