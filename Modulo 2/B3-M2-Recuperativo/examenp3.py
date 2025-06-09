# p3.py - Validador de correo electrónico

# Solicitar correo al usuario
correo = input("Ingrese su correo: ")

# Lista para almacenar los errores encontrados
errores = []

# Verificar que tenga exactamente una arroba
if correo.count('@') != 1:
    if correo.count('@') == 0:
        errores.append("- Falta el símbolo @")
    else:
        errores.append("- Tiene más de un símbolo @")

# Verificar que no tenga espacios
if ' ' in correo:
    errores.append("- No debe contener espacios")

# Si tiene exactamente una arroba, hacer más validaciones
if correo.count('@') == 1:
    # Dividir el correo en partes antes y después de @
    partes = correo.split('@')
    parte_antes = partes[0]
    parte_despues = partes[1]

    # Verificar que haya texto antes de @
    if len(parte_antes) == 0:
        errores.append("- Falta texto antes de la arroba")

    # Verificar que haya texto después de @
    if len(parte_despues) == 0:
        errores.append("- Falta texto después de la arroba")

    # Verificar que haya al menos un punto después de @
    if '.' not in parte_despues:
        errores.append("- Falta un punto (.) después de la arroba")

# Mostrar resultado
if len(errores) == 0:
    print("Correo válido.")
else:
    print("Correo inválido. Faltan:")
    for error in errores:
        print(error)