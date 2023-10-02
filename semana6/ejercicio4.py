def main():
  grades = []
  while True:
    try:
        while True:
          grade = float(input(f"Ingrese la nota {len(grades) + 1}: "))
          if 0 <= grade <= 20:
             break
          else:
             print("Ingrese una nota correcamente")
    except ValueError:
        print("Usted debe ingresar solo números")
    else:
        grades.append(grade)
        if len(grades) == 5:
          break
    
  categorize(grades)


def categorize(grades):
  grades.sort()
  grades[0] = grades[-1]

  average = sum(grades)/len(grades)

  if average < 10:
    print("La nota en letra será D")
  elif average < 14 :
    print("La nota en letra será C")
  elif average < 17 :
    print("La nota en letra será B")
  elif 17 < average :
    print("La nota en letra será A")


main()