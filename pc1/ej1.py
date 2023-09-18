# strip -> elimina espacios en blanco antes y despues del
#          primer caracter

# capitalize -> formatea el texto para que el primer caracter
#               de la cadena sea mayúscula 
name = input("Cuál es tu nombre? ").strip().capitalize()
edad = int(input("Cuántos años tienes? "))
talla = float(input("Cuánto mides? "))

# f-String -> "abreviación" de str.format(), permite dar 
#             dar formato al texto con variables
print(f"Hola {name}, tu edad es {edad} y tu talla es {talla}")