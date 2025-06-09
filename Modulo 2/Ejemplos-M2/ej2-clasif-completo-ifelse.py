num = int(input("Ingrese un número: "))
if 0 <= num <= 100:
    if num <= 20:
        print("bajo")
    else:
        if num <= 40:
            print("medio bajo")
        else:
            if num <= 60:
                print("medio")
            else:
                if num <= 80:
                    print("medio alto")
                else:
                    print("alto")
else:
    print("El número ingresado no es válido.")



