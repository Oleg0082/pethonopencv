import cv2
import numpy as np

ancho, alto = 500, 500  # Tamaño de la ventana
imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255

# creo una ventana
cv2.namedWindow('Mi ventana', cv2.WINDOW_NORMAL)
# Espero a que el usuario pulse una tecla
cv2.waitKey(0)
# Elimino las ventanas creadas
cv2.destroyAllWindows()