import cv2
import numpy as np
import random
import os
import math
import time

class Particula:
    def __init__(self):
        # Generar parámetros aleatorios para el círculo
        self.centrox = random.randint(0, ancho)
        self.centroy = random.randint(0, alto)
        self.radio = random.randint(10, 20)  # Limitar el radio para que encaje en la imagen
        self.rojo = random.randint(0, 255)
        self.verde = random.randint(0, 255)
        self.azul = random.randint(0, 255)
        self.angulo = random.uniform(0, 360)  # Ángulo inicial en grados
        self.velocidad = random.randint(1, 5)
        self.radianes = 0
    def mueve(self):
        self.centrox += math.cos(self.radianes) * self.velocidad
        self.centroy += math.sin(self.radianes) * self.velocidad
    def gira(self):
        # Actualizar posición del círculo
        self.angulo += random.uniform(-5, 5)  # Pequeña variación aleatoria del ángulo
        self.radianes = math.radians(self.angulo)
    def colisiona(self):
        # Verificar colisión con los bordes horizontales
        if self.centrox - self.radio < 0 or self.centrox + self.radio > ancho:
            self.angulo = (180 - self.angulo) % 360  # Rebote horizontal
            self.radianes = math.radians(self.angulo)
            # Ajustar posición para evitar quedarse atascado en el borde
            self.centrox = max(self.radio, min(self.centrox, ancho - self.radio))

        # Verificar colisión con los bordes verticales
        if self.centroy - self.radio < 0 or self.centroy + self.radio > alto:
            self.angulo = (-self.angulo) % 360  # Rebote vertical
            self.radianes = math.radians(self.angulo)
            # Ajustar posición para evitar quedarse atascado en el borde
            self.centroy = max(self.radio, min(self.centroy, alto - self.radio)) 
      

# Configuración del video
ancho = 1280
alto = 720
fps = 30
segundos = 60  # Para pruebas, se reduce el tiempo

# Crear carpeta para guardar las imágenes si no existe
output_folder = "imagenes"
os.makedirs(output_folder, exist_ok=True)

# Nombre del archivo de video
video_filename = "videos/"+str(round(time.time()))+".mp4"

# Crear el escritor de video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (ancho, alto))

# Ahora creo muchas particulas
particulas = []

for _ in range(0,50):
    particulas.append(Particula())

# Generar imágenes y escribirlas en el video
total_frames = fps * segundos
for frame in range(total_frames):
    # Crear una imagen blanca
    imagen_blanca = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
    
    for particula in particulas:
        # Dibujar el círculo en la imagen
        particula.colisiona()
        particula.mueve()
        particula.gira()
        
        cv2.circle(
            imagen_blanca,
            (int(particula.centrox), int(particula.centroy)),
            particula.radio,
            (particula.rojo, particula.verde, particula.azul),
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
