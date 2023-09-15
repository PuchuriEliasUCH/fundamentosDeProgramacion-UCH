# Ejercicio 4

l1 = float(input("Ingrese el valor del lado 1: "))
l2 = float(input("Ingrese el valor del lado 2: "))
l3 = float(input("Ingrese el valor del lado 3: "))

notNegative = l1 > 0 and l2 > 0 and l3 > 0
existence = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1

equilateral = l1 == l2 and l1 == l3
isosceles = l1 == l2 or l1 == l3 or l2 == l3

if(notNegative and existence):
  if(equilateral):
    print('el triangulo es equilatero')
  else:
    if (isosceles):
      print('el triangulo es isosceles')
    else:
      print('el triangulo es escaleno')
else:
  print('el triangúlo no existe')


