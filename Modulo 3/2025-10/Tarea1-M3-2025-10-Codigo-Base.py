def menu_principal():
    historial_juegos = {}
    while True:
        print("\n=== Menú Principal ===")
        print("1. Iniciar nuevo juego")
        print("2. Revisar juego anterior")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            nombre = input("Nombre del juego: ")
            jugar_partida(nombre, historial_juegos)
        elif opcion == "2":
            revisar_partida(historial_juegos)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def jugar_partida(nombre_juego, historial_juegos):
    lista_posiciones = leer_posiciones_entrada()

    # Convertir lista a diccionario {1: 'a1', 2: 'h1', ...}
    posiciones = {}
    numero = 1
    for pos in lista_posiciones:
        posiciones[numero] = pos
        numero = numero + 1

    historial = []
    historial.append("=== Estado inicial del tablero ===")
    tablero_str = mostrar_tablero(posiciones)
    historial.append(tablero_str)

    simular_turnos(posiciones, historial)
    historial_juegos[nombre_juego] = historial


#--------------------------------------------------------------------------------------------------------------------

def leer_posiciones_entrada():
    while True:
        entrada = input("Ingresa las posiciones iniciales de las reinas (separadas por espacio): ")
        posiciones = entrada.strip().lower().split()

        posiciones_validas = []
        posiciones_invalidas = []
        posiciones_repetidas = []

        for pos in posiciones:
            if len(pos) != 2:
                posiciones_invalidas.append(pos)
                continue

            letra = pos[0]
            numero = pos[1]

            if not ('a' <= letra <= 'h'):
                posiciones_invalidas.append(pos)
                continue

            if not ('1' <= numero <= '8'):
                posiciones_invalidas.append(pos)
                continue

            if pos in posiciones_validas:
                posiciones_repetidas.append(pos)
                continue

            posiciones_validas.append(pos)

        if posiciones_invalidas:
            print("Posiciones inválidas:", ", ".join(posiciones_invalidas))
        if posiciones_repetidas:
            print("Posiciones repetidas:", ", ".join(posiciones_repetidas))

        if len(posiciones_validas) == len(posiciones) and len(posiciones_validas) > 0:
            return posiciones_validas
        else:
            print("Entrada inválida. Intenta nuevamente.")

#--------------------------------------------------------------------------------------------------------------------

def convertir_a_coordenadas(pos):
    letras = "abcdefgh"
    fila = int(pos[1]) - 1  # Convertir '1'-'8' a 0-7
    columna = letras.index(pos[0])  # Convertir 'a'-'h' a 0-7
    return [fila, columna]

#--------------------------------------------------------------------------------------------------------------------

def es_ataque_valido(origen, destino, posiciones_dict):
    o_coord = convertir_a_coordenadas(origen)
    d_coord = convertir_a_coordenadas(destino)

    fila_o, col_o = o_coord
    fila_d, col_d = d_coord

    delta_fila = fila_d - fila_o
    delta_col = col_d - col_o

    if delta_fila == 0 and delta_col == 0:
        return False

    es_valido = False
    if delta_fila == 0:  # Misma fila
        es_valido = True
        paso_col = 1 if delta_col > 0 else -1
    elif delta_col == 0:  # Misma columna
        es_valido = True
        paso_fila = 1 if delta_fila > 0 else -1
    elif abs(delta_fila) == abs(delta_col):  # Diagonal
        es_valido = True
        paso_fila = 1 if delta_fila > 0 else -1
        paso_col = 1 if delta_col > 0 else -1

    if not es_valido:
        return False

    if delta_fila == 0:
        col = col_o + paso_col
        while col != col_d:
            posicion_intermedia = chr(col + ord('a')) + str(fila_o + 1)
            for reina, pos in posiciones_dict.items():
                if pos == posicion_intermedia:
                    return False
            col += paso_col
    elif delta_col == 0:
        fila = fila_o + paso_fila
        while fila != fila_d:
            posicion_intermedia = chr(col_o + ord('a')) + str(fila + 1)
            for reina, pos in posiciones_dict.items():
                if pos == posicion_intermedia:
                    return False
            fila += paso_fila
    else:
        fila, col = fila_o + paso_fila, col_o + paso_col
        while fila != fila_d and col != col_d:
            posicion_intermedia = chr(col + ord('a')) + str(fila + 1)
            for reina, pos in posiciones_dict.items():
                if pos == posicion_intermedia:
                    return False
            fila += paso_fila
            col += paso_col

    return True

#--------------------------------------------------------------------------------------------------------------------

def mostrar_tablero(posiciones_dict):
    tablero = []
    for _ in range(8):
        fila = ['.'] * 8
        tablero.append(fila)

    for reina, pos in posiciones_dict.items():
        coord = convertir_a_coordenadas(pos)
        fila, col = coord
        fila_tablero = 7 - fila
        tablero[fila_tablero][col] = str(reina)

    tablero_str = ""
    for fila in tablero:
        tablero_str += " ".join(fila) + "\n"

    tablero_str = tablero_str.rstrip()

    print(tablero_str)
    return tablero_str

#--------------------------------------------------------------------------------------------------------------------

def simular_turnos(posiciones, historial):
    turno_actual = 1
    reinas_vivas = list(posiciones.keys())
    ciclo_sin_ataques = 0

    while ciclo_sin_ataques < len(reinas_vivas) and len(reinas_vivas) > 1:
        indice_reina = (turno_actual - 1) % len(reinas_vivas)
        reina_actual = reinas_vivas[indice_reina]
        pos_actual = posiciones[reina_actual]

        historial.append(f"Turno de la Reina {reina_actual} ({pos_actual})")

        ataque_realizado = False
        for reina_objetivo in reinas_vivas:
            if reina_objetivo == reina_actual:
                continue

            pos_objetivo = posiciones[reina_objetivo]

            if es_ataque_valido(pos_actual, pos_objetivo, posiciones):
                historial.append(f"Ataca a Reina {reina_objetivo} en {pos_objetivo}")

                posiciones[reina_actual] = pos_objetivo
                reinas_vivas.remove(reina_objetivo)
                del posiciones[reina_objetivo]

                tablero_actualizado = mostrar_tablero(posiciones)
                historial.append(tablero_actualizado)

                ataque_realizado = True
                ciclo_sin_ataques = 0
                break

        if not ataque_realizado:
            historial.append("No puede atacar a nadie. Pasa su turno.")
            ciclo_sin_ataques += 1

        turno_actual += 1

    historial.append("Fin del juego. Estado final:")
    tablero_final = mostrar_tablero(posiciones)
    historial.append(tablero_final)

    historial.append("Reinas sobrevivientes:")
    for reina in sorted(posiciones.keys()):
        historial.append(f"Reina {reina} en {posiciones[reina]}")


def revisar_partida(historial_juegos):
    nombre = input("Nombre del juego a revisar: ")
    if nombre in historial_juegos:
        print(f"=== Revisión de la partida '{nombre}' ===")
        for linea in historial_juegos[nombre]:
            print(linea)
    else:
        print("Juego no encontrado.")

# Código cliente
if __name__ == "__main__":
    menu_principal()