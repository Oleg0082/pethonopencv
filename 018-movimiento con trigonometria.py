import cv2
import numpy as np
import random
import time
import os
import math

# Configuración del video
ancho = 1280
alto = 720
fps = 30
segundos = 60

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
angulo = random.randint(0, 360)
velocidad = random.randint(1, 5)

# Generar imágenes y escribirlas en el video
total_frames = fps * segundos
for frame in range(total_frames):
    # Crear una imagen blanca
    imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255

    angulo += random.uniform(-1, 1)

    centrox += math.cos(angulo)*velocidad
    centroy += math.sin(angulo)*velocidad

    # Dibujar el círculo en la imagen
    cv2.circle(
        imagen_blanca, 
        (int(centrox), int(centroy)), 
        radio, 
        (rojo, verde, azul), 
        -1,  # Rellenar el círculo
        lineType=cv2.LINE_AA
    )

    # Guardar la imagen como archivo individual (opcional)
    image_path = os.path.join(output_folder, f"frame_{frame:04d}.png")
    #cv2.imwrite(image_path, imagen_blanca)

    # Escribir el frame en el video
    video_writer.write(imagen_blanca)

# Liberar el escritor de video
video_writer.release()

print(f"Video guardado como {video_filename}")