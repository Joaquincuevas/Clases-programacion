from numpy import random
#Ejercicio 2
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))
#Numeros enteros y decimales

a = -d/2

b = -e/2

r = ((a**2 + b**2 - f))**(1/2)

radio = round(r, 2)
print("El radio es: ", radio)

print("La ecuacion de la circunferencia es: (X -", a, ")^2 + (Y -", b, ")^2 = ", radio, "^2")

n = float(input("Ingrese n: "))
s = float(input("Ingrese s: "))
t = float(input("Ingrese t: "))
v = float(input("Ingrese v: "))
w = float(input("Ingrese w: "))

i = 0
lista_in = []
lista_out = []

while i < n:
    x = round(random.uniform(s, t), 2)
    y = round(random.uniform(v, w), 2)
    if ((x - a)**2 + (y - b)**2) <= radio**2:
        lista_in.append((x, y))
    else:
        lista_out.append((x, y))
    i += 1

print("Puntos dentro de la circunferencia: ", lista_in)
print("Puntos fuera de la circunferencia: ", lista_out)