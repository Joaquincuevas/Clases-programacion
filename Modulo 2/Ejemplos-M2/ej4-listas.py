from numpy import random

# Creamos la lista
lista = []
while len(lista) < 10000:
    lista.append(random.randint(0, 10))
    
secuencia = [1,3,8,1] # definimos la secuencia
cant = 0

i = 0
# Buscamos la secuencia a partir de los distintos elementos
# de la lista, pero terminamos antes del final segun
# el largo de la secuencia
while i < len(lista) - (len(secuencia) - 1):
    j = 0
    encontrada = True
    # Comparamos cada elemento de la secuencia desde la posicion
    # actual en la lista, si uno es distinto, entonces ahi no
    # se encuentra la secuencia
    while j < len(secuencia):
        if lista[i + j] != secuencia[j]:
            encontrada = False
            break
        j += 1

    if encontrada:
        cant += 1
        
    i += 1
    
print("Secuencia", secuencia, "encontrada", cant, "veces")
    
    
