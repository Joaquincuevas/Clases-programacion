d = int(input("Ingrese d: "))
e = int(input("Ingrese e: "))
f = int(input("Ingrese f: "))
#Solo numeros enteros

a = -d/2

b = -e/2

r = ((a**2 + b**2 - f))**(1/2)

radio = round(r, 2)
print("El radio es: ", radio)

print("La ecuacion de la circunferencia es: (X -", a, ")^2 + (Y -", b, ")^2 = ", radio, "^2")



#-------------------------------------------------------------------------------------------------------------


""" d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))
#Numeros enteros y decimales

a = -d/2

b = -e/2

r = ((a**2 + b**2 - f))**(1/2)

radio = round(r, 2)
print("El radio es: ", radio)

print("La ecuacion de la circunferencia es: (X -", a, ")^2 + (Y -", b, ")^2 = ", radio, "^2")

 """