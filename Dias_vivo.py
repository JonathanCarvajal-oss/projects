#Progrma que diga cuantos dias llevas vivo a partir de la fecha de nacimiengto

from datetime import datetime
 
 #devolver ese nuemero entero de años
def dias_vivo(fecha_nacimiento):
    hoy = datetime.now()
    nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    dias_vivo = (hoy-nacimiento).days
    return dias_vivo
 
tu_fecha = input("Introduce tu fecha denacimiento (DIAS-MES-AÑO): ")
dias = dias_vivo(tu_fecha)
print(f"Llevas {dias} dias vivo")


n = 2*3+3**2
print(n)