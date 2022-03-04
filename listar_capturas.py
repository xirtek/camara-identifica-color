# se obtiene el número de última captura realizada y lo retorna a camara_captura_color.py
# funciona para capturas entre 0 - n 

import glob

#función retorna valor que tendrá la nueva captura
def listar():

    try:
        final = obtener_numero_final('*?') + 1
    except:
        #si no existe archivo captura_objeto habrá error, pero con el except se sigue trabajando y se le asigna un 0
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

#para probar el script actual, quitar comentario de línea 15, 43 y comentar línea 16
#listar()
