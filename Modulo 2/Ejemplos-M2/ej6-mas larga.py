texto = input("Ingrese el texto: ")

# Eliminamos caracteres innecesarios
# como los string son inmutables debemos ir guardando el
# nuevo string en la misma variable
eliminar = ['.', ',', ';', ':']
for elim in eliminar:
    while texto.count(elim) > 0:
        texto = texto.replace(elim, '')

# Ahora dividimos las palabras
palabras = texto.split(" ")

# Las recorremos y vamos guardando la mas larga
mas_larga = None
for pal in palabras:
    if mas_larga is None or len(mas_larga) < len(pal):
        mas_larga = pal
        
print("La palabra mas larga es", mas_larga)

