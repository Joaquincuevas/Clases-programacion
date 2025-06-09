MONTHS = {
    1: {"Max": 31, "Name": "Enero"},
    2: {"Max": 28, "Name": "Febrero"},
    3: {"Max": 31, "Name": "Marzo"},
    4: {"Max": 30, "Name": "Abril"},
    5: {"Max": 31, "Name": "Mayo"},
    6: {"Max": 30, "Name": "Junio"},
    7: {"Max": 31, "Name": "Julio"},
    8: {"Max": 31, "Name": "Agosto"},
    9: {"Max": 30, "Name": "Septiembre"},
    10: {"Max": 31, "Name": "Octubre"},
    11: {"Max": 30, "Name": "Noviembre"},
    12: {"Max": 31, "Name": "Diciembre"}
}

events = {}

def menu():
    print("Bienvenido a calendapp")
    print("a) Revisar calendario de un mes")
    print("b) Agregar Evento")
    print("c) Remover Evento")
    print("d) Mover Evento")
    print("Enter para cerrar el programa")


def fill_year():
    # Crea una lista de listas, cada sublista representa los días de un mes
    year = []
    for m in range(1, 13):
        dias = []
        for d in range(1, MONTHS[m]["Max"] + 1):
            dias.append(d)
        year.append(dias)
    return year

def print_calendar_month(month, year):
    # Imprime el calendario del mes, marcando los días con eventos con *
    dias_semana = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"]
    print(MONTHS[month]["Name"])
    print(" ".join(dias_semana))
    # Calcular el primer día de la semana del mes
    # El 1 de enero es lunes, así que contamos los días hasta el mes actual
    dias_previos = sum(MONTHS[m]["Max"] for m in range(1, month))
    primer_dia_semana = (dias_previos) % 7  # 0: lunes, ..., 6: domingo
    # Imprimir espacios iniciales
    print("   " * primer_dia_semana, end="")
    for dia in range(1, MONTHS[month]["Max"] + 1):
        # Construir la fecha como texto, por ejemplo "05/03"
        if dia < 10:
            dia_str = "0" + str(dia)
        else:
            dia_str = str(dia)
        if month < 10:
            mes_str = "0" + str(month)
        else:
            mes_str = str(month)
        fecha = dia_str + "/" + mes_str
        if fecha in events and events[fecha]:
            print(f"{dia}*", end=" ")
        else:
            print(f"{dia}", end=" ")
        primer_dia_semana += 1
        if primer_dia_semana == 7:
            print()
            primer_dia_semana = 0
    print("\n")


def valid_date(day, month):
    # Verifica si el mes y el día son válidos
    if month not in MONTHS:
        return False
    if not (1 <= day <= MONTHS[month]["Max"]):
        return False
    return True

def add_event(day, month, event_name, year):
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False
    fecha = f"{day:02d}/{month:02d}"
    if fecha not in events:
        events[fecha] = []
    events[fecha].append(event_name)
    print(f"Evento agregado en {fecha}:")
    show_events(day, month)
    print_calendar_month(month, year)
    return True

def remove_event(day, month, index, year):
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False
    fecha = f"{day:02d}/{month:02d}"
    if fecha not in events or not events[fecha]:
        print("No hay eventos en esa fecha")
        return False
    if not (0 <= index < len(events[fecha])):
        print("Indice invalido")
        return False
    evento_eliminado = events[fecha].pop(index)
    print(f"Evento eliminado: {evento_eliminado}")
    if not events[fecha]:
        del events[fecha]
    show_events(day, month)
    print_calendar_month(month, year)
    return True

def show_events(day, month):
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False
    fecha = f"{day:02d}/{month:02d}"
    if fecha in events and events[fecha]:
        print(f"Eventos en {fecha}:")
        for i, ev in enumerate(events[fecha]):
            print(f"{i}: {ev}")
    else:
        print("No hay eventos en esa fecha.")

def move_event(day, month):
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False
    fecha = f"{day:02d}/{month:02d}"
    if fecha not in events or not events[fecha]:
        print("No hay eventos en esa fecha")
        return False
    show_events(day, month)
    idx_str = input("Ingrese el indice del evento a mover: ")
    if not es_entero_positivo(idx_str):
        print("Indice invalido")
        return False
    idx = int(idx_str)
    if not (0 <= idx < len(events[fecha])):
        print("Indice invalido")
        return False
    evento = events[fecha][idx]
    nuevo_dia_str = input("Ingrese el nuevo dia: ")
    nuevo_mes_str = input("Ingrese el nuevo mes: ")
    if not (es_entero_positivo(nuevo_dia_str) and es_entero_positivo(nuevo_mes_str)):
        print("Fecha invalida")
        return False
    nuevo_dia = int(nuevo_dia_str)
    nuevo_mes = int(nuevo_mes_str)
    if not valid_date(nuevo_dia, nuevo_mes):
        print("Fecha destino invalida")
        return False
    # Remover y agregar
    events[fecha].pop(idx)
    if not events[fecha]:
        del events[fecha]
    nueva_fecha = f"{nuevo_dia:02d}/{nuevo_mes:02d}"
    if nueva_fecha not in events:
        events[nueva_fecha] = []
    events[nueva_fecha].append(evento)
    print(f"Evento movido a {nueva_fecha}")
    print_calendar_month(nuevo_mes, year)
    return True


year= fill_year()


#  Funcion Auxiliar para validar si una cadena es un entero positivo
def es_entero_positivo(cadena):
    if len(cadena) == 0:
        return False
    for c in cadena:
        if c < "0" or c > "9":
            return False
    return True

#Deben completar el ciclo de uso
while(True):
    menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "a":
        mes_str = input("Ingrese el mes a mostrar: ")
        if es_entero_positivo(mes_str):
            mes = int(mes_str)
            if 1 <= mes <= 12:
                print("")
                print_calendar_month(mes, year)
            else:
                print("Mes invalido")
        else:
            print("Mes invalido")
    elif opcion == "b":
        dia_str = input("Ingrese el dia del evento: ")
        mes_str = input("Ingrese el mes del evento: ")
        if es_entero_positivo(dia_str) and es_entero_positivo(mes_str):
            dia = int(dia_str)
            mes = int(mes_str)
            evento = input("Ingrese el evento: ")
            add_event(dia, mes, evento, year)
        else:
            print("Datos invalidos")
    elif opcion == "c":
        dia_str = input("Ingrese el dia del evento a eliminar: ")
        mes_str = input("Ingrese el mes del evento a eliminar: ")
        if es_entero_positivo(dia_str) and es_entero_positivo(mes_str):
            dia = int(dia_str)
            mes = int(mes_str)
            show_events(dia, mes)
            idx_str = input("Ingrese el indice del evento a eliminar: ")
            if es_entero_positivo(idx_str):
                idx = int(idx_str)
                remove_event(dia, mes, idx, year)
            else:
                print("Indice invalido")
        else:
            print("Datos invalidos")
    elif opcion == "d":
        dia_str = input("Ingrese el dia del evento a mover: ")
        mes_str = input("Ingrese el mes del evento a mover: ")
        if es_entero_positivo(dia_str) and es_entero_positivo(mes_str):
            dia = int(dia_str)
            mes = int(mes_str)
            move_event(dia, mes)
        else:
            print("Datos invalidos")
    elif opcion == "":
        break
    else:
        print("Opcion invalida")





















