# Code 09/06/2020 by Anderson
import pandas as pd
import re
import collections
from alg_ci import validacion_ci_ecuatoriana
from alg_edad import comprobar_edad

cedulaslist = []
no_cedula = 0
ci_validas = 0
ci_sin_cero = []
ci_con_cero = []
n_cedulas_agregadas_cero = 0
ci_validas_con_cero_agregado = 0
ci_no_validas_10_digitos=0
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


print("\n\t REPORTE DE DATOS")
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
print('----Campo cédula de estudiamtes')
for cedula in cedulas:
    if(type(cedula) == str):
        cedulaslist.append(cedula)
    else:
        no_cedula += 1

print("Número de registros en los no hay cédula del estudiante:  ", no_cedula)


for ci in cedulaslist:
    if len(ci) == 10:
        if validacion_ci_ecuatoriana(ci):
            ci_validas += 1
    else:
        ci_sin_cero.append(ci)


for i in ci_sin_cero:
    ci_con_cero.append('0'+i)
    n_cedulas_agregadas_cero += 1

print('Número de cédulas a las que se les agregó un cero al inicio  :',n_cedulas_agregadas_cero)

n_10_nv = len(cedulas) - no_cedula - ci_validas - len(ci_sin_cero)
print("Número de cédulas 10 dígitos no válidas  :", n_10_nv)


for x in ci_con_cero:
    if validacion_ci_ecuatoriana(x):
        ci_validas_con_cero_agregado += 1

no_validas_cero_agregado = len(ci_con_cero) - ci_validas_con_cero_agregado

print('Cédulas no válidas al agregar cero al inicio:  ',no_validas_cero_agregado)
n_ci_duplicadas=0
ci_duplicadas=[]

n_ci_duplicado = len([x for x, y in collections.Counter(cedulaslist).items() if y > 1])
print('Cédulas duplicadas:  ',n_ci_duplicado)

# Validación direcciones
print('\n----Campo dirección de estudiantes')
for direccion in direcciones:
    if(type(direccion) != str):
        no_direccion += 1
print('Registros en los que no se registra dirección:  ', no_direccion)
direcciones_list = list(direcciones)
n_direcciones_duplicadas = len([x for x, y in collections.Counter(direcciones_list).items() if y > 1])
print('Registros en los que se tiene dirección duplicada:  ', n_direcciones_duplicadas)


# Validación teléfono
print('\n----Campo teléfono de estudiantes')
for telefono in telefonos:
    if(type(telefono) != str):
        no_telefono += 1
    elif len(telefono) != 7:
        telefono_no_valido += 1
telefonoslist = list(telefonos)
n_telefonos_duplicados = len([x for x, y in collections.Counter(telefonoslist).items() if y > 1])
print('Registros sin teléfono:  ', no_telefono)
print('Registros con número de teléfono no válido:   ', telefono_no_valido)
print('Registros con número de teléfono duplicado:    ',n_telefonos_duplicados)


# Validación de edad, import alg_edad
print('\n----Campo edad de estudiantes')

edades_reales = []
for x in fechas_nacimiento:
    edades_reales.append(comprobar_edad(x))

for x in range(len(edades)):
    if int(edades[x]) != edades_reales[x]:
        edades_incorrectas += 1

print('Registros con edades incorrectas:   ', edades_incorrectas)

# Validación calificaciones
print('\n-----Campo calificaciones de estudiantes')
for calificacion in calificaciones:
    if type(calificacion) == str:
        if int(calificacion) > 20 or int(calificacion) < 0:
            calificaciones_incorrectas += 1
    else:
        sin_calificaion += 1
print('Registros con calificaciones incorrectas:   ', calificaciones_incorrectas)
print('Registros sin calificaciones:   ', sin_calificaion)

print('\n----Campo nombres de estudiantes')
nombres_inician_con_vacio = 0
patronnombre = re.compile(r"(?:[a-zA-Z]+)")
patronnombre2 = re.compile(r"(?:(?: ){1}(?:[a-zA-Z]+))")

for nombre in nombres:
    if type(nombre) != str:
        sin_nombre += 1
    else:
        if patronnombre.fullmatch(nombre):
            pass
        else:
            nombres_con_caracteres_no_validos += 1
        if patronnombre2.fullmatch(nombre):
            nombres_inician_con_vacio+=1


print('Registros sin nombre:   ', sin_nombre)
print('Registros de nombres con caracteres especiales:   ',nombres_con_caracteres_no_validos)
print('Registros de nombres que inician con caracter vacío:   ',nombres_inician_con_vacio)


# VAlidacioón apellidos, import re
apellidos_caracter_vacio_inicio=0
print('\n----Campo apellido de estudiantes')
patronapellido = re.compile(r"(?:(?:[a-zA-Z]+(?: ){1}(?:[a-zA-Z]+)))")
patronapellido2 = re.compile(r"(?:(?: ){1}(?:[a-zA-Z]+(?: ){1}(?:[a-zA-Z]+)))")
for apellido in apellidos:
    if type(apellido) != str:
        sin_apellido += 1
    else:
        if patronapellido.fullmatch(apellido):
            pass
        else:
           apellidos_con_caracteres_no_validos += 1

        if patronapellido2.fullmatch(apellido):
            apellidos_caracter_vacio_inicio+=1

print('Registros sin apellido:   ', sin_apellido)
print('Registros de apellidos con caracteres especiales:   ',apellidos_con_caracteres_no_validos)
print('Registros de apellidos que inician con caracater vacío:  ',apellidos_caracter_vacio_inicio)


# validación correo, import re
print('\n----Campo correo de estudiantes')
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
correoslist = list(correos)
n_correos_duplicados = len([x for x, y in collections.Counter(correoslist).items() if y > 1])


print('Registros sin correo:   ', sin_correo)
print('Registros de correos sin formato general o tienen caracteres especiales:   ', correos_no_validos)
print('Número de correos repetidos: ', n_correos_duplicados)

correos_sin_formato=0
for i in range(len(nombres)):
    

  if type(nombres[i])==str and type(apellidos[i])==str:

    aux = list(apellidos[i])
    aux2 = []
    for w in aux:
        if w == ' ':
            break
        else:
            aux2.append(w)
    apellido_esperado=''.join(aux2)

    correo_esperado = nombres[i]+"."+apellido_esperado+"@"+"universidad.edu.ec"
    if correo_esperado != correos[i]:
        correos_sin_formato+=1

print('Correos que no cumplen formato nombre.apellido@universidad.com:  ',correos_sin_formato)