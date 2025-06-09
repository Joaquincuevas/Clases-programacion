#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

# Esta seria la version optimizada del programa anterior
if a > b: # ordenamos 'a' y 'b'
    aux = a
    a = b
    b = aux
if a > c: # ordenamos 'a' y 'c'
    aux = a
    a = c
    c = aux
# hasta aqui 'a' es el menor y hay que ver si 'b' y 'c' estan en desorden
if b > c: 
    aux = b
    b = c
    c = aux

print(a,b,c)
