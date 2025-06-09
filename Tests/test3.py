# Diccionario sin datos (vacío)
diccionario_vacio = {}
print("Diccionario vacío:", diccionario_vacio)
print("Longitud:", len(diccionario_vacio))

# Diccionario con datos (clave-valor)
estudiante = {
    "nombre": "Ana",
    1: 22,
    "carrera": "Informática",
    "promedio": 6.8,
    "cursos_aprobados": ["Programación", "Matemáticas", "Bases de Datos"]
}

print("\nDiccionario con datos:", estudiante)
print("Nombre del estudiante:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Primer curso aprobado:", estudiante["cursos_aprobados"][0])

promedio = 1+1.7546+1.656478+ 1.5345364

u = round(promedio,2)
print("Promedio:", u)
print("La division de 23/5 es: ", 23/5)

print(type(estudiante))


n = float(input("Número: "))
if n > 0:
 print("Positivo")
elif n < 0:
 print("Negativo")
else:
 print("Cero")


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n = int(input("Número: "))
print(es_primo(n))