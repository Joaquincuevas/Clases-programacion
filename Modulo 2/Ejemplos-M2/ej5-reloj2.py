#!/usr/bin/env python3
# -*- coding: utf-8 -*-

minuto = 0
seg = 0

# Avanzar 60 minutos
while minuto < 60:
        
    # imprimir tiempo actual
    print(minuto + ":" + seg)
    
    # pasamos al siguiente segundo dentro del minuto
    seg = seg + 1
    
    # Vemos si completamos 60 segundos (1 minuto)
    if seg == 60:
        # hay que pasar al minuto siguiente
        minuto += 1

        # volver a 0 los segundos, para contar los 
        # segundos del minuto siguiente
        seg = 0 

