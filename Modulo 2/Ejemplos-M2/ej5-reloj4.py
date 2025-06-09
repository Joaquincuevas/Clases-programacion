#!/usr/bin/env python3
from time import sleep
# -*- coding: utf-8 -*-

hora = int(input("Ingresa la hora actual: "))
minuto = int(input("Ingresa el minuto actual: "))
seg = int(input("Ingresa el segundo actual: "))

while hora < 12:
    # imprimimos el tiempo actual
    hora_analoga = hora
    if hora == 0:
        hora_analoga = 12
        
    print("%02d:%02d:%02d" % (hora_analoga, minuto, seg))
    sleep(1)
    
    # pasamos al siguiente segundo dentro del minuto
    seg = seg + 1
    
    # Vemos si completamos 60 segundos (1 minuto)
    if seg == 60:
        # hay que pasar al minuto siguiente
        minuto += 1

        # para contar los segundos del minuto siguiente
        seg = 0 
    
    # igual que lo que tenemos arriba, pero con minutos
    # y horas
    if minuto == 60:
        hora += 1
        minuto = 0
        
