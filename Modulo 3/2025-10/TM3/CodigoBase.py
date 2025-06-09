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
    #Deben rellenar una lista de lista que contenga
    #Todos los dias del anho partiendo del primero de enero
    return year

def print_calendar_month(month, year):
    #Deben mostrar al usuario un mes especifico
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


year = fill_year()

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





















