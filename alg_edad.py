from datetime import datetime

hoy = datetime.now()

def comprobar_edad(fecha):
    fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
    edad = int(hoy.year - fecha.year - ((hoy.month, hoy.day) < (fecha.month, fecha.day)))
    return edad

