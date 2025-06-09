def fibonacci(n, filas, columnas):
 l = [0,1]
 m = []
 count = 0
 for i in range(filas):
    if i == 0:
        fila = [0,1]
        count += 2
    else:
        fila = []
    for j in range(columnas-len(fila)):
        l.append(l[-2:-1][0] + l[-1:][0])
        if count < n:
            fila.append(l[-1])
            count += 1
        else:
            fila.append(0)
    m.append(fila)
 return m

n = int(input("n>"))
filas = int(input("filas>"))
columnas = int(input("columnas>"))

lf = fibonacci(n, filas, columnas)
suma = 0
for i in range(len(lf)):
    for j in range(len(lf[0])):
        suma += lf[i][j]

print(lf)
print(suma)