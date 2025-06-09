hora = 0
minuto = 0
seg = 0

# Avanzar 12 horas
while hora < 12:

    hora_analoga = hora
    if hora == 0:
        hora_analoga = 12

    # imprimir tiempo actual
    print(str(hora_analoga) + ":" + str(minuto) + ":" + str(seg))

    # pasamos al siguiente segundo dentro del minuto
    seg = seg + 1

    # Vemos si completamos 60 segundos (1 minuto)
    if seg == 60:
        # hay que pasar al minuto siguiente
        minuto += 1

        # volver a 0 los segundos, para contar los
        # segundos del minuto siguiente
        seg = 0

    # Revisar si completamos 60 minutos (1 hora)
    if minuto == 60:
        # Lo siguiente es analogo al caso anterior
        # de segundos y minutos
        hora += 1
        minuto = 0

