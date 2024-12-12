import cv2
import numpy as np
import random
import os
import math

# Configuración del video
ancho = 1280
alto = 720
fps = 30
segundos = 60  # Para pruebas, se reduce el tiempo

# Crear carpeta para guardar las imágenes si no existe
output_folder = "imagenes"
os.makedirs(output_folder, exist_ok=True)

# Nombre del archivo de video
video_filename = "output_video.mp4"

# Crear el escritor de video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (ancho, alto))

# Generar parámetros aleatorios para el círculo
centrox = random.randint(0, ancho)
centroy = random.randint(0, alto)
radio = random.randint(10, 20)  # Limitar el radio para que encaje en la imagen
rojo = random.randint(0, 255)
verde = random.randint(0, 255)
azul = random.randint(0, 255)
angulo = random.uniform(0, 360)  # Ángulo inicial en grados
velocidad = random.randint(1, 5)

# Generar imágenes y escribirlas en el video
total_frames = fps * segundos
for frame in range(total_frames):
    # Crear una imagen blanca
    imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255

    # Actualizar posición del círculo
    angulo += random.uniform(-5, 5)  # Pequeña variación aleatoria del ángulo
    radianes = math.radians(angulo)

    centrox += math.cos(radianes) * velocidad
    centroy += math.sin(radianes) * velocidad

    # Verificar colisión con los bordes
    if centrox - radio < 0 or centrox + radio > ancho:
        angulo += 180
        centrox = max(radio, min(centrox, ancho - radio))
    if centroy - radio < 0 or centroy + radio > alto:
        angulo += 180
        centroy = max(radio, min(centroy, alto - radio))

    # Dibujar el círculo en la imagen
    cv2.circle(
        imagen_blanca,
        (int(centrox), int(centroy)),
        radio,
        (rojo, verde, azul),
        -1,  # Rellenar el círculo
        lineType=cv2.LINE_AA
    )

    # Mostrar el framebuffer
    cv2.imshow("Framebuffer", imagen_blanca)

    # Escribir el frame en el video
    video_writer.write(imagen_blanca)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el escritor de video y cerrar la ventana
video_writer.release()
cv2.destroyAllWindows()

print(f"Video guardado como {video_filename}")
