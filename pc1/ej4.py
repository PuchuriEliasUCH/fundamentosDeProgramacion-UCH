horas = int(input('Cuántas horas pasaron? '))
minutos = int(input('Cuántas minutos pasaron? '))
segundos = int(input('Cuántas segundos pasaron? '))

tiempo_pasado = horas * 3600 + minutos * 60 + segundos

tiempo_total = 60*60*60 

tiempo_restante = tiempo_total - tiempo_pasado

horas = tiempo_restante // 3600

tiempo_restante -= horas * 3600

minutos = tiempo_restante // 60

tiempo_restante -= minutos * 60

print(f"falta {horas}h {minutos}m {tiempo_restante}s para el próximo viernes")