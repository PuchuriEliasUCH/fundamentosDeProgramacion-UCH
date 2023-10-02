numbers = {'1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco', '6': 'seis', '7': 'siete', '8': 'ocho', '9': 'nueve','0': 'cero'}

try:
  while True:
    num = int(input('Ingresar número: '))
    if num < 0:
      print("Debe escribir números positivos")
    else:
      break
except ValueError:
  print("Debe escribir solo números")
else:
  print(numbers[str(num)[-1]])