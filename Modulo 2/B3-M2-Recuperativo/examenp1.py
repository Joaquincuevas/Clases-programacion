import math

epsilon = float(input("Ingrese un valor positivo epsilon (> 0): "))

suma_anterior = 0
suma_actual = 1
n = 1
diferencia = abs(suma_actual - suma_anterior)

while diferencia >= epsilon:
    suma_anterior = suma_actual
    suma_actual += 1 / math.factorial(n)
    diferencia = abs(suma_actual - suma_anterior)
    n += 1

print("Se necesitaron", n, "términos para alcanzar una diferencia menor que", epsilon)
print("Aproximación de e:", suma_actual)