import cv2
import numpy as np
import random
import time

ancho = 500
alto = 500
imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
for _ in range(0,1000):
    centrox = random.randint(0,500)
    centroy = random.randint(0,500)
    radio = random.randint(0,500)
    rojo = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)
    cv2.circle(
        imagen_blanca, 
        (centrox,centroy), 
        radio, 
        (rojo,verde,azul), 
        4)
cv2.imwrite("imagenes/"+str(time.time())+'.png', imagen_blanca)
# creo una ventana
##cv2.namedWindow('Mi ventana', cv2.WINDOW_NORMAL)

# cv2.imshow('Mi ventana', imagen_blanca)
# Espero a que el usuario pulse una tecla
# cv2.waitKey(0)
# Elimino las ventanas creadas
# cv2.destroyAllWindows()