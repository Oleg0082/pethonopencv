import cv2
import numpy as np
import random
import time

ancho = 1024
alto = 1024
imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255

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


