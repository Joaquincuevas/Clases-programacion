i = 1

# Queremos imprimir lista de numeros que no son
# divisibles por 2 o por 3.
while i < 100:
    if i%2 == 0 or i%3 == 0:
        i += 1
        continue    # no se ejecutan las lineas 10 y 11
                    # vuelve a linea 5
    print(i, "no es divisible por 2 o 3")
    i += 1


