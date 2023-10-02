def main():
  while True:
    try:
        consumo = int(input("Ingresar el consumo: ").strip())
    except ValueError:
        print("Usted debe ingresar solo números")
    else:
        amount(consumo)
        break



def amount(consumo):
  res = "el importe a pagar es de S/"

  if consumo <= 0:
     return print("No se puedo calcular el importe")

  if consumo >= 500:
    return print(res, consumo * 2, sep="")
  elif consumo >= 100:
    return print(res, consumo * 1.5, sep="")
  
  return print(res, consumo, sep="");
    


main()