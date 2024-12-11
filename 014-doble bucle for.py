import cv2
import numpy as np
import random
import time
for _ in range(0,20):
    ancho = 4096
    alto = 4096
    imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
    for _ in range(0,1000):
        centrox = random.randint(0,ancho)
        centroy = random.randint(0,alto)
        radio = random.randint(0,ancho)
        rojo = random.randint(0,255)
        verde = random.randint(0,255)
        azul = random.randint(0,255)
        cv2.circle(
            imagen_blanca, 
            (centrox,centroy), 
            radio, 
            (rojo,verde,azul), 
            4,
            lineType=cv2.LINE_AA)
    cv2.imwrite("imagenes/"+str(time.time())+'.png', imagen_blanca)
# creo una ventana
##cv2.namedWindow('Mi ventana', cv2.WINDOW_NORMAL)

# cv2.imshow('Mi ventana', imagen_blanca)
# Espero a que el usuario pulse una tecla
# cv2.waitKey(0)
# Elimino las ventanas creadas
# cv2.destroyAllWindows()