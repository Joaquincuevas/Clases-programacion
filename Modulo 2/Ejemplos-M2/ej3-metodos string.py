linea = 'La casa es roja'
print(linea.find('a')) # Imprime 1
print(linea.find('a', 7)) # Imprime 14

linea2 = linea.upper()
print(linea2) # LA CASA ES ROJA

linea3 = linea.replace('a', 'er')
print(linea3) # Ler cerser es rojer

lista1 = linea.split() 
print(lista1) # ['La', 'casa', 'es', 'roja']

lista2 = linea.split('a')
print(lista2) # ['L', ' c', 's', ' es roj', '']


