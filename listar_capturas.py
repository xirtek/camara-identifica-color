# se obtiene la cantidad de capturas en el directorio y lo retorna a camara_captura_color.py

import glob

def listar():
    a = 0 
    b = 0
    c = 0
    d = 0

    #contar captura_objeto
    for name in sorted(glob.glob('captura_objeto.jpg')):
        a+=1

    #contar captura_objeto1 al captura_objeto9
    for name in sorted(glob.glob('captura_objeto?.jpg')):
        b+=1
        
    #contar captura_objeto10 al captura_objeto99
    for name in sorted(glob.glob('captura_objeto??.jpg')):
        c+=1

    #contar captura_objeto100 al captura_objeto999
    for name in sorted(glob.glob('captura_objeto???.jpg')):
        d+=1

    total = a+b+c+d

    return total
