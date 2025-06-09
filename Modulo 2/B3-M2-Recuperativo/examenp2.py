# p2.py - Múltiples aproximaciones del número e
import math

# Lista para guardar los valores de epsilon
epsilons = []

# Pedir valores de epsilon hasta que el usuario ingrese 0
while True:
    epsilon = float(input("Ingrese epsilon (> 0): "))
    if epsilon == 0:
        break
    epsilons.append(epsilon)

# Para cada epsilon, calcular la aproximación de e
for epsilon in epsilons:
    # Inicializar variables para cada cálculo
    suma_anterior = 0
    suma_actual = 1  # Primer término: 1/0! = 1
    n = 1
    diferencia = abs(suma_actual - suma_anterior)

    # Sumar términos hasta que la diferencia sea menor que epsilon
    while diferencia >= epsilon:
        suma_anterior = suma_actual
        # Calcular 1/n! y sumarlo
        suma_actual += 1 / math.factorial(n)
        diferencia = abs(suma_actual - suma_anterior)
        n += 1

    # Imprimir resultados para este epsilon
    print(f"Para epsilon = {epsilon}, se necesitaron {n} términos. Aproximación: {suma_actual}")