# Ejercicio 1

lado = float(input("Cuál es el lado del cuadrado? "))

area = lado * lado
# area = lado ** 2
# area = pow(lado, 2)

# formateando para que solo nos devuelva 2 decimales
# print("el area del cuadrado es {:.2f}".format(area))
print(f"el area del cuadrado es {area:.2f} u²")
