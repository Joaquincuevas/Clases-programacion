#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

# Idea: asegurar que 'a' tenga el menor valor
if a > b: # si 'a' es mayor que 'b'
    aux = a # hay que intercambiar 'a' con 'b'
    a = b
    b = aux # aqui sabemos que 'a' es ahora menor o igual que 'b'
    if a > c: # luego vemos si 'a' es mayor que 'c'
        aux = a # itercambiamos 'a' y 'c' si se da el caso
        a = c
        c = aux
    if b > c: # finalmente, vemos si b y c estan en orden
        aux = b # intercambiamos si hay desorden
        b = c
        c = aux
else: # sabemos aqui que a <= b
    if a > c: # es el mismo flujo de la linea 12 en adelante
        aux = a
        a = c
        c = aux
    if b > c:
        aux = b
        b = c
        c = aux

print(a,b,c)

# El programa es correcto pero redundante, pues las lineas 12 a 19
# o 21 a 28 son iguales y siempre ejecutan. Se puede "factorizar" 
# este codigo y ponerlo debajo del primer if de las lineas 8 a 11.
# Ver programa "ordenar-2.py"
