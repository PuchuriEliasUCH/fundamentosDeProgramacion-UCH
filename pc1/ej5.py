prod = {"a": 15, "b": 15, "c": 62}
res = "el tiempo de producción es: "
tipo_prod = input("Que tipo de balde va se va a fabricar?\na - b - c\n")
cantidad = int(input("Qué cantidad se va a fabricar?"))
tiempo = prod[tipo_prod] * cantidad

if tiempo > 3600:
    res += f"{tiempo // 3600}h "
    tiempo = tiempo % 3600  

if tiempo > 60:
    res += f"{tiempo // 60}m "
    tiempo = tiempo % 60

res += f" {tiempo}s"
print(res)

