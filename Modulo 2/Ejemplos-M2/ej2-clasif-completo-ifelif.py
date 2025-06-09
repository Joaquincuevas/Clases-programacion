#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = int(input("Ingrese un número: "))
if 0 <= num <= 100:
    if num <= 20:
        print("bajo")
    elif num <= 40:
        print("medio bajo")
    elif num <= 60:
        print("medio")
    elif num <= 80:
        print("medio alto")
    else:
        print("alto")
else:
    print("El número ingresado no es válido.")


