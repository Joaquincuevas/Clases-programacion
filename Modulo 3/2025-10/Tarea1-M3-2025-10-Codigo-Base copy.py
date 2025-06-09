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
#(0.5 P)

def leer_posiciones_entrada():
    while True:
        entrada = input("Ingresa las posiciones iniciales de las reinas (separadas por espacio): ")
        posiciones = entrada.strip().lower().split()

        # Verificar que se haya ingresado al menos una posición
        if not posiciones:
            print("Error: Debes ingresar al menos una posición.")
            continue

        posiciones_invalidas = []
        posiciones_duplicadas = []
        posiciones_vistas = set()

        for pos in posiciones:
            # Verificar formato correcto (dos caracteres: letra a-h + número 1-8)
            if len(pos) != 2 or not ('a' <= pos[0] <= 'h') or not ('1' <= pos[1] <= '8'):
                posiciones_invalidas.append(pos)
            # Verificar unicidad
            elif pos in posiciones_vistas:
                posiciones_duplicadas.append(pos)
            else:
                posiciones_vistas.add(pos)

        # Mostrar errores si hay posiciones inválidas o duplicadas
        if posiciones_invalidas or posiciones_duplicadas:
            if posiciones_invalidas:
                print("")
                print(f"Error: Posiciones inválidas: {', '.join(posiciones_invalidas)}")
                print("Cada posición debe tener formato: letra(a-h) + número(1-8), como 'a1' o 'h8'.")
            if posiciones_duplicadas:
                print("")
                print(f"Error: Posiciones duplicadas: {', '.join(posiciones_duplicadas)}")
            print("Por favor, intenta nuevamente.")
            continue
        return posiciones

#--------------------------------------------------------------------------------------------------------------------
#(0.5 P)

def convertir_a_coordenadas(pos):
    # Ejemplo: "d4" -> (4, 3)
    columna = 4
    fila = 3
    return [fila, columna]

#--------------------------------------------------------------------------------------------------------------------
#(1.0 P)

def es_ataque_valido(origen, destino, posiciones_dict):
    # Verifica si hay línea recta sin obstrucciones entre origen y destino
    # (Diagonal, fila o columna)
    pass  # A implementar

#--------------------------------------------------------------------------------------------------------------------
#(1.0 P)

def mostrar_tablero(posiciones_dict):
    tablero_str = "COMPLETAR ESTA FUNCIÓN"
    return tablero_str

#--------------------------------------------------------------------------------------------------------------------
#(3.0 P)

def simular_turnos(posiciones_iniciales, historial):
    # Simula los turnos del juego y actualiza historial con cada evento
    pass  # A implementar

#--------------------------------------------------------------------------------------------------------------------

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
