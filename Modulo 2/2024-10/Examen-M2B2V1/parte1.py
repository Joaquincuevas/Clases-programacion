c = int(input("Ingrese capital: "))
r = float(input("Ingrese rentabilidad: "))
n = int(input("Ingrese períodos: "))
a = int(input("Ingrese ahorro mensual: "))

simulacion = [c]
simulacion_ahorro = [c]

i = 0

while i <= n:
    simulacion.append((simulacion[i])*(1+r))
    simulacion_ahorro.append((simulacion_ahorro[i]+a)*(1+r))
    i += 1

i = 0

print("-"*28)
print(f"C: {c}, r: {r}, n: {n}, a: {a}")
print("-"*28)
print("S\tSA")
print("-"*28)

while i <= n:
    print(f"{round(simulacion[i], 1):5.1f}\t{round(simulacion_ahorro[i], 1)}")
    i += 1

print("-"*28)
print("S: Simulación, SA: Simulación con ahorro periódico")