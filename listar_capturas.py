# se obtiene el número de última captura realizada y lo retorna a camara_captura_color.py
# funciona para capturas entre 0 - 999

import glob

#función retorna valor que tendrá la nueva captura
def listar():

    a,b,c,d = 0,0,0,0

    #contar captura_objeto100 al captura_objeto999
    for name in sorted(glob.glob('captura_objeto???.jpg')):
        d+=1
    #contar captura_objeto10 al captura_objeto99
    for name in sorted(glob.glob('captura_objeto??.jpg')):
        c+=1
    #contar captura_objeto1 al captura_objeto9
    for name in sorted(glob.glob('captura_objeto?.jpg')):
        b+=1
    #contar captura_objeto
    for name in sorted(glob.glob('captura_objeto.jpg')):
        a+=1

    if d > 0:
        final = obtener_numero_final('???') + 1
    elif c > 0:
        final = obtener_numero_final('??') + 1
    elif b > 0:
        final = obtener_numero_final('?') + 1
    elif a > 0:
        final = 1
    else: #no encuentra archivo creado (casos de números > 999 no están contemplados para su existencia)
        final = 0

    #print(final)
    return final

#función retorna número de la última captura realizada
def obtener_numero_final(decimales):
    mayor = 0
    texto = 'captura_objeto{}.jpg'.format(decimales)
    for name in sorted(glob.glob(texto)):
        numero = int(search_number_string(name))
        if numero > mayor:
            mayor = numero
    return mayor

#función extrae los números dentro del nombre de la captura  ejemplo: captura_objeto21 => 21
def search_number_string(String):
       index_list = []
       del index_list[:]
       for i, x in enumerate(String):
           if x.isdigit() == True:
               index_list.append(i)
       start = index_list[0]
       end = index_list[-1] + 1
       number = String[start:end]
       return number

# --------------------------------------------------------------------------------------------------------------

#para probar el script actual quitar comentario de línea 35, 63 y comentar línea 36
#listar()
