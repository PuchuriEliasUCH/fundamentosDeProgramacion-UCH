precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje del descuento: "))

print(f"El precio final del producto será {(precio * (100 - descuento)/100 * 1.18):.2f}")