# -*- coding: utf-8 -*-
lugar = input("Ingresa un lugar: ")
objeto = input("Ingresa un objeto: ")
consecuencia = "consecuencias desconocidas"

if lugar == "universidad":
    if objeto == "auto":
        consecuencia = "que sea dificil estacionar"
    elif objeto == "mochila":
        consecuencia = "dolor de espalda"
    else:
        consecuencia = "problemas con los profesores"
elif lugar == "casa":
    if objeto == "ladron":
        consecuencia = "mucho miedo"
    elif objeto == "perro":
        consecuencia = "mucha alegria"
    else:
        consecuencia = "problemas con tus padres"

result = "Venir a la " + lugar + " con " + objeto + " causa " + consecuencia
print(result)

# Descomentar las siguientes lineas para escuchar audio
# en un Mac
from subprocess import call
call(["say", result])

