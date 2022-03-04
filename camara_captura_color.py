# << Descripción >> 
# Al pasar objetos de color verde frente a una cámara web, se le asigna un rectángulo para destacarlo.

# << Instrucciones >> 
# s: sacar captura | esc: terminar ejecución

# << Requisitos >>
# - Python 3.8.6 64-bit
# - OpenCV 4.4.0

# --------------------------------------------------------------------------------------------------------------

#Se importa biblioteca OpenCV
import cv2

#Importar archivo para contar archivos
import listar_capturas

#Variable
text = 'Color detectado'

#Extensión en python para trabajar con matrices, vectores, etc
import numpy as np #alias np

cam = cv2.VideoCapture(0) #se crea objeto cam
kernel = np.ones((5,5),np.uint8) 

#ciclo infinito para lectura de imagen
while(True):
    ret,frame = cam.read() #ret:detecta si se está recibiendo o no imagen (true,false)  frame:imagen leia en frames

    #rango valores para detectar objeto
    rangomax = np.array([50,255,50])# RGB: color verde
    rangomin = np.array([0,51,0])

    mascara = cv2.inRange(frame,rangomin,rangomax) #si pixel se encuentre en rango será pto blanco, si está fuera es pto negro
    opening = cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)
    x,y,w,h = cv2.boundingRect(opening)

    cv2.putText(frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1 , cv2.COLOR_BGR2GRAY, 2) #texto mostrado por encima del rectángulo

    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3) #rectangulo dibujado
    cv2.circle(frame,(int(x+w/2),int(y+h/2)),5,(0,0,255),-1) #círculo en el centro del rectángulo
    cv2.imshow('Detectar objeto color verde en camara web | s: pantallazo - esc: Salir',frame)

    #Espera a que se pulse una tecla
    k=cv2.waitKey(1) & 0xFF 
    if k==27: #tecla esc para salir del programa
        break
    elif k==ord('s'):
        # asigna valor a variable i según las imágenes captura_objeto.jpg encontradas a tiempo real en la carpeta.
        # en caso de borrar archivos, editar números va actualizando su número al último creado

        i = listar_capturas.listar()
        
        if i==0:
            foto = ('captura_objeto.jpg')
        else:
            foto = ('captura_objeto'+str(i)+'.jpg')
        cv2.imwrite(foto, frame) #guarda una captura del objeto detectado
        
# Para terminar con proceso al apretar escape
cam.release()
cv2.destroyAllWindows()