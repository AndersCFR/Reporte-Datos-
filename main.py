# Code 09/06/2020 by Anderson
import pandas as pd
from alg_ci import validacion_ci_ecuatoriana
from alg_edad import comprobar_edad

cedulaslist = []
no_cedula=0
ci_validas=0
ci_sin_cero = []
ci_con_cero = []
n_cedulas_agregadas_cero=0
ci_validas_con_cero_agregado=0
no_direccion=0
no_telefono=0
telefono_no_valido=0
edades_incorrectas=0
calificaciones_incorrectas=0
sin_calificaion=0


print("----Reporte de datos ---------")
fuente_datos = pd.read_excel('2020A_calidad_datos (1).xlsx', 
dtype={
    "cedula_est":str,
    "direccion_est":str,
    "telefono_est":str, 
    "fecha_nacimiento_est":str,
    "edad_est":str,
    "calificacion":str
    }
)


cedulas = fuente_datos["cedula_est"]
direcciones = fuente_datos["direccion_est"]
telefonos = fuente_datos["telefono_est"]
edades = fuente_datos["edad_est"]
fechas_nacimiento = fuente_datos["fecha_nacimiento_est"]
calificaciones = fuente_datos["calificacion"]


print("\n------Campo cédulas de estudiantes------")
for cedula in cedulas:
    if(type(cedula)==str):
        cedulaslist.append(cedula)
    else:
        no_cedula+=1

print("Número de campos en los que no hay cédula del estudiante:  ", no_cedula)


for ci in cedulaslist:
    if len(ci) == 10:
        if validacion_ci_ecuatoriana(ci):
            ci_validas+=1
    else:
        ci_sin_cero.append(ci)


print("Número de cédulas ecuatorianas 10 dígitos válidas  :", ci_validas)


for i in ci_sin_cero:
    ci_con_cero.append('0'+i)
    n_cedulas_agregadas_cero+=1

print('Número de cédulas a las que se les agregó un cero al inicio  :',n_cedulas_agregadas_cero)

for x in ci_con_cero:
    if validacion_ci_ecuatoriana(x):
        ci_validas_con_cero_agregado+=1

    
print('Cédulas válidas al agregar cero al inicio:  ',ci_validas_con_cero_agregado)
total_ci_validas = ci_validas + ci_validas_con_cero_agregado
print('Total de cédulas válidas:  ',total_ci_validas)

print('\n------Campo dirección de estudiantes------')
for direccion in direcciones:
    if(type(direccion)!=str):
        no_direccion+=1
print('Registros en los que no se registra dirección:  ',no_direccion)

print('\n-----Campo teléfono de estudiantes-------')
for telefono in telefonos:
    if(type(telefono)!=str):
        no_telefono+=1
    elif len(telefono) != 7:
        telefono_no_valido+=1
print('Registros sin teléfono:  ', no_telefono)
print('Registros con número de teléfono no válido:   ',telefono_no_valido)

print('\n-----Campo edad de estudiantes-------')

edades_reales = []
for x in fechas_nacimiento:
    edades_reales.append(comprobar_edad(x))

for x in range(len(edades)):
    if int(edades[x]) != edades_reales[x]:
        edades_incorrectas+=1

print('Registros con edades incorrectas:   ',edades_incorrectas)

print('\n-----Campo calificaciones de estudiantes-------')
for calificacion in calificaciones:
    if type(calificacion) == str:
        if int(calificacion) > 20:
            calificaciones_incorrectas+=1
    else:
        sin_calificaion+=1
print('Registros con calificaciones incorrectas:   ',calificaciones_incorrectas)
print('Registros sin calificaciones:   ',sin_calificaion)
