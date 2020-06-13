# Code 09/06/2020 by Anderson
import pandas as pd
import re
from alg_ci import validacion_ci_ecuatoriana
from alg_edad import comprobar_edad

cedulaslist = []
no_cedula = 0
ci_validas = 0
ci_sin_cero = []
ci_con_cero = []
n_cedulas_agregadas_cero = 0
ci_validas_con_cero_agregado = 0
no_direccion = 0
no_telefono = 0
telefono_no_valido = 0
edades_incorrectas = 0
calificaciones_incorrectas = 0
sin_calificaion = 0
sin_nombre = 0
nombres_con_caracteres_no_validos = 0
sin_apellido = 0
apellidos_con_caracteres_no_validos = 0
sin_correo = 0
correos_no_validos = 0


print("\n\t----Reporte de datos ---------")
fuente_datos = pd.read_excel('2020A_calidad_datos (1).xlsx',
                             dtype={
                                 "cedula_est": str,
                                 "direccion_est": str,
                                 "telefono_est": str,
                                 "fecha_nacimiento_est": str,
                                 "edad_est": str,
                                 "calificacion": str,
                                 "nombre_est": str,
                                 "apellido_est": str,
                                 "correo_est": str
                             }
                             )


cedulas = fuente_datos["cedula_est"]
direcciones = fuente_datos["direccion_est"]
telefonos = fuente_datos["telefono_est"]
edades = fuente_datos["edad_est"]
fechas_nacimiento = fuente_datos["fecha_nacimiento_est"]
calificaciones = fuente_datos["calificacion"]
nombres = fuente_datos["nombre_est"]
apellidos = fuente_datos["apellido_est"]
correos = fuente_datos["correo_est"]


# Validación de cédula, import alg_ci
print("\n------Campo cédulas de estudiantes------")
for cedula in cedulas:
    if(type(cedula) == str):
        cedulaslist.append(cedula)
    else:
        no_cedula += 1

print("Número de campos en los que no hay cédula del estudiante:  ", no_cedula)


for ci in cedulaslist:
    if len(ci) == 10:
        if validacion_ci_ecuatoriana(ci):
            ci_validas += 1
    else:
        ci_sin_cero.append(ci)


print("Número de cédulas ecuatorianas 10 dígitos válidas  :", ci_validas)


for i in ci_sin_cero:
    ci_con_cero.append('0'+i)
    n_cedulas_agregadas_cero += 1

print('Número de cédulas a las que se les agregó un cero al inicio  :',
      n_cedulas_agregadas_cero)

for x in ci_con_cero:
    if validacion_ci_ecuatoriana(x):
        ci_validas_con_cero_agregado += 1


print('Cédulas válidas al agregar cero al inicio:  ',
      ci_validas_con_cero_agregado)
total_ci_validas = ci_validas + ci_validas_con_cero_agregado
print('Total de cédulas válidas:  ', total_ci_validas)


# Validación direcciones
print('\n------Campo dirección de estudiantes------')
for direccion in direcciones:
    if(type(direccion) != str):
        no_direccion += 1
print('Registros en los que no se registra dirección:  ', no_direccion)


# Validación teléfono
print('\n-----Campo teléfono de estudiantes-------')
for telefono in telefonos:
    if(type(telefono) != str):
        no_telefono += 1
    elif len(telefono) != 7:
        telefono_no_valido += 1
print('Registros sin teléfono:  ', no_telefono)
print('Registros con número de teléfono no válido:   ', telefono_no_valido)


# Validación de edad, import alg_edad
print('\n-----Campo edad de estudiantes-------')

edades_reales = []
for x in fechas_nacimiento:
    edades_reales.append(comprobar_edad(x))

for x in range(len(edades)):
    if int(edades[x]) != edades_reales[x]:
        edades_incorrectas += 1

print('Registros con edades incorrectas:   ', edades_incorrectas)

# Validación calificaciones
print('\n-----Campo calificaciones de estudiantes-------')
for calificacion in calificaciones:
    if type(calificacion) == str:
        if int(calificacion) > 20:
            calificaciones_incorrectas += 1
    else:
        sin_calificaion += 1
print('Registros con calificaciones incorrectas:   ', calificaciones_incorrectas)
print('Registros sin calificaciones:   ', sin_calificaion)

print('\n-----Campo nombres de estudiantes-------')
patronnombre = re.compile(r"(?:[a-zA-Z]+)")
for nombre in nombres:
    if type(nombre) != str:
        sin_nombre += 1
    else:
        if patronnombre.match(nombre):
            pass
        else:
            nombres_con_caracteres_no_validos += 1

print('Registros sin nombre:   ', sin_nombre)
print('Registros con nombres no válidos:   ',
      nombres_con_caracteres_no_validos)


# VAlidacioón apellidos, import re
print('\n-----Campo apellido de estudiantes-------')
patronapellido = re.compile(r"(?:(?:[a-zA-Z]+(?: ){1}(?:[a-zA-Z]+)))")
for apellido in apellidos:
    if type(apellido) != str:
        sin_apellido += 1
    else:
        if patronapellido.fullmatch(apellido):
            pass
        else:
            apellidos_con_caracteres_no_validos += 1

print('Registros sin apellido:   ', sin_apellido)
print('Registros con apellidos no válidos:   ',
      apellidos_con_caracteres_no_validos)


# validación correo, import re
print('\n-----Campo correo de estudiantes-------')
patroncorreo = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
for correo in correos:
    if type(correo) != str:
        sin_correo += 1
    else:
        if patroncorreo.fullmatch(correo):
            pass
        else:
            correos_no_validos += 1
print('Registros sin correo:   ', sin_correo)
print('Registros con correos no válidos:   ', correos_no_validos)
