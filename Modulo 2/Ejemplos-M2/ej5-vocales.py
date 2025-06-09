texto = input("Ingrese el texto: ")

vocales = 0
for letra in texto:
    if letra.lower() in ['a','e','i','o','u']:
        vocales += 1
        
print("El texto tiene", 100*vocales/len(texto), "% de vocales")


