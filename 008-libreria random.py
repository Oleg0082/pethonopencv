import cv2
import numpy as np
import random

ancho = 500
alto = 500
imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
cv2.circle(
    imagen_blanca, 
    (random.randint(0,500),random.randint(0,500)), 
    random.randint(0,500), 
    (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 
    4)
# creo una ventana
cv2.namedWindow('Mi ventana', cv2.WINDOW_NORMAL)
cv2.imshow('Mi ventana', imagen_blanca)
# Espero a que el usuario pulse una tecla
cv2.waitKey(0)
# Elimino las ventanas creadas
cv2.destroyAllWindows()