while True:
    rut = input("Ingrese su rut (sin puntos ni guion): ")
    if len(rut) != 8:
        print("Invalido")
    elif "-" in rut or "." in rut:
        print("Invalido")
    else:
        break

print("El rut es: ", rut)

digitos = []
for d in rut:
    digitos.append(int(d))

serie = [2, 3, 4, 5, 6, 7]

suma = 0
for i in range(8):
    multiplicador = serie[i % len(serie)]
    suma += digitos[-(i+1)] * multiplicador

print("La suma de los productos es:", suma)