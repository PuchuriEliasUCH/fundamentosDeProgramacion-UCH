def main():
    while True:
        try:
            num = int(input("Ingresar número: ").strip())
        except ValueError:
            print("Usted debe ingresar solo números")
        else:
            validate(num)
            break


def validate(num):
    if num < 0:
        return print("Número negativo")
    elif num > 0:
        return print("Número positivo")

    return print("Número cero")


main()