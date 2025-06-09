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
    year = []
    for i in MONTHS.keys():
        max_days = MONTHS[i]["Max"]
        dias_del_mes = list(range(1, max_days + 1))
        year.append(dias_del_mes)

    return year

def print_calendar_month(month, year):
    if month not in MONTHS:
        print("Mes invalido")
        return
    nombre_mes = MONTHS[month]["Name"]
    dias_del_mes = year[month - 1]

    comienzo_semana = 0
    for mes in range(1, month):
        comienzo_semana += MONTHS[mes]["Max"] % 7

    print(f"{nombre_mes}")
    print("Lu Ma Mi Ju Vi Sa Do")
    print("   " * comienzo_semana, end="")
    for dia in dias_del_mes:
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
        comienzo_semana += 1
        if comienzo_semana % 7 == 0:
            print()
    print()


def valid_date(day, month):
    #Deben validar las fechas basandose en el diccionario entregado
    return True

def add_event(day, month, event_name, year):
    #Aca agregan eventos al calendario mediante el uso de diccionarios
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False

def remove_event(day, month, index, year):
    #Eliminan un evento del diccionario
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False

def show_events(day, month):
    #Mostrar los eventos en una fecha especificada
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False

def move_event(day, month):
    #Pasar un evento de una fecha a otra
    if not valid_date(day, month):
        print("Fecha ingresada invalida")
        return False


year= fill_year()

#Deben completar el ciclo de uso
while(True):
    menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "a":
        pass
    if opcion == "b":
        pass
    if opcion == "c":
        pass
    if opcion == "d":
        pass
    if opcion == "":
        break
    else:
        print("Opcion invalida")





















