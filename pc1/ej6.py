# sueldo_bruto = float(input("Ingrese su sueldo neto: "))

# print(f"""
# Descuento: {(sueldo_bruto * 0.12):.2f}
# Tu Sueldo neto es: {(sueldo_bruto * 0.88):.2f}
# En quincena recibes: {(sueldo_bruto * 0.88 * 0.4):.2f} 
# A fin de mes recibes: {(sueldo_bruto * 0.88 * 0.6):.2f}
# """)

sueldo_bruto = float(input("Ingrese su sueldo neto: "))

descuento = sueldo_bruto * 0.12

sueldo_neto = sueldo_bruto - descuento

quincena = sueldo_neto * 0.4

print(f"""
Descuento: {descuento:.2f}
Tu Sueldo neto es: {sueldo_neto:.2f}
En quincena recibes: {quincena:.2f} 
A fin de mes recibes: {(sueldo_neto - quincena):.2f}
""")

