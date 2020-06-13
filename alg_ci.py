
def validacion_ci_ecuatoriana(cedula):

    aux_cont = 0
    digitos_multiplicados = []
    suma_digitos_multiplicados = 0
    decena_superior=0
    digito_verificador=0
    flag=False
    while aux_cont < 9:
            if aux_cont%2==0:
                digito_duplicado = int(cedula[aux_cont])*2

                if digito_duplicado>=10:
                    aux_digito_duplicado = str(digito_duplicado)
                    digito_duplicado = int(aux_digito_duplicado[0])+int(aux_digito_duplicado[1])

                digitos_multiplicados.append(digito_duplicado)

                aux_cont+=1
            else:
                digitos_multiplicados.append(int(cedula[aux_cont])*1)
                aux_cont+=1
                
    for i in digitos_multiplicados:
        suma_digitos_multiplicados+=i
        

    decena_superior=suma_digitos_multiplicados
    if decena_superior%10 == 0:
        pass
    else:
        while decena_superior%10 != 0:
            decena_superior+=1
        
    digito_verificador=decena_superior-suma_digitos_multiplicados

    if digito_verificador==int(cedula[9]):
     flag=True
 
    return flag
  