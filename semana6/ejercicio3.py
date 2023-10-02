def main():
  while True:
    try:
      grade = float(input("Ingrese la nota: "))
      if 0 <= grade <= 20 :
        break
      else:
        print("Ingrese una nota correcta")
    except ValueError:
      print("Usted debe ingresar solo números")
    
  categorize(grade)


def categorize(grade):
  if grade <= 5:
    print("La nota en letra será E")
  elif grade <= 10.5:
    print("La nota en letra será D")
  elif grade <= 13 :
    print("La nota en letra será C")
  elif grade <= 17 :
    print("La nota en letra será B")
  elif 17 < grade :
    print("La nota en letra será A")



main()