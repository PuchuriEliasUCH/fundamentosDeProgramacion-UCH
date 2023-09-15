# Ejercicio 3 
# import math

cateto1 = float(input("Ingrese la medida del cateto 1: "))
cateto2 = float(input("Ingrese la medida del cateto 2: "))

suma_cuadrados = pow(cateto1, 2) + pow(cateto2, 2) 

# hipotenusa = math.sqrt(suma_cuadrados)
hipotenusa = pow(suma_cuadrados, 0.5)

print(f"El valor de la hipotenusa es: {hipotenusa:.2f}")

