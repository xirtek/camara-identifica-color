# Código para identificar color por cámara web
 
Pequeño código tipo ejercicio realizado en python, que se tomó como base lo expuesto en el video de youtube titulado ["Python: Detección de objetos con OpenCV ( Object Tracking )"](https://youtu.be/CppgV8inf7g), al cual se le fueron agregando nuevas características como aprendizaje.

Consiste en reconocer objetos de determinado color (en este caso verde), el cual es destacado con un rectángulo verde con un punto rojo en su centro y un texto encima. También tiene la funcionalidad de guardar n cantidad de screenshots de manera manual en la misma ubicación del archivo py y las capturas se nombran según la cantidad de archivos en el directorio. 

## Tecnologías utilizadas
- Python 3.8.6 64-bit
- OpenCV 4.4.0
- Numpy 1.19.2
- DroidCamApp (aplicación de escritorio y móvil, utilizada para convertir en cámara web un smartphone)

## Recomendaciones
- Al instalar python asegurarse de marcar "Add Python 3.8 to PATH" y que esté marcado "pip" en "Customize installation".
- Instalar OpenCV mediante [pip](https://pypi.org/project/opencv-contrib-python/) por consola.
  ```
  pip install opencv-contrib-python
  ```
- Para probar código, utilizar el idle que viene por defecto junto a python.

## Instrucciones de uso (teclas)
- **s:** sacar captura
- **esc:** terminar ejecución



