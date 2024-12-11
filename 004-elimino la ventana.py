import cv2

# creo una ventana
cv2.namedWindow('Mi ventana', cv2.WINDOW_NORMAL)
# Espero a que el usuario pulse una tecla
cv2.waitKey(0)
# Elimino las ventanas creadas
cv2.destroyAllWindows()