# Ejercicio 6

monto_ingresado = float(input("Ingrese el monto de dinero a cambiar: "))
cambio = 3.7

esDolar = int(input(
"""
El monto ingresado está en dolares?
si = 1
no = 0
"""))

if bool(esDolar):
  monto_devuelto = monto_ingresado * cambio
  print(f"el monto que recibirá es: S/{monto_devuelto:.2f}")
else :
  monto_devuelto = monto_ingresado / cambio
  print(f"el monto que recibirá es: ${monto_devuelto:.2f}")
