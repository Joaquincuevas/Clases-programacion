# -*- coding: utf-8 -*-
objeto = input("Ingresa un objeto: ")
color = "desconocido"

if objeto == "cielo":
    color = "azul"
elif objeto == "pasto":
    color = "verde"
elif objeto == "conejo":
    color = "blanco"

if objeto == "cielo":
    color = "blanco"
    
print("El color del", objeto, "es", color)

