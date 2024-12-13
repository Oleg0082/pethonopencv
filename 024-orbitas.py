import cv2
import numpy as np
import random
import os
import math
import time

class Particle:
    def __init__(self, x, y, radius, color, orbit_center=None, orbit_radius=0, orbit_speed=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.orbit_center = orbit_center
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.angle = random.uniform(0, 360)
        self.trajectory = []

    def update_orbit(self):
        if self.orbit_center:
            self.angle += self.orbit_speed
            self.angle %= 360  # Keep the angle in the range [0, 360)
            rad = math.radians(self.angle)
            self.x = self.orbit_center.x + self.orbit_radius * math.cos(rad)
            self.y = self.orbit_center.y + self.orbit_radius * math.sin(rad)
            self.trajectory.append((self.x, self.y))  # Save trajectory point

# Configuration
width = 1280
height = 720
fps = 30
seconds = 2220  # Simulation duration
show_trajectories = False  # Parameter to toggle trajectory drawing

# Output folder and video file setup
output_folder = "imagenes"
os.makedirs(output_folder, exist_ok=True)
video_filename = f"videos/{round(time.time())}.mp4"

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

# Create the central particle (the star)
center_particle = Particle(
    x=width // 2,
    y=height // 2,
    radius=30,
    color=(0, 255, 255)  # Yellow color for the central particle
)

# Create planets orbiting the central particle
num_planets = random.randint(3, 6)
planets = []
for _ in range(num_planets):
    orbit_radius = random.randint(100, 300)
    orbit_speed = random.uniform(0.5, 2.0)
    planet_radius = random.randint(10, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    planet = Particle(
        x=center_particle.x,
        y=center_particle.y,
        radius=planet_radius,
        color=color,
        orbit_center=center_particle,
        orbit_radius=orbit_radius,
        orbit_speed=orbit_speed
    )
    planets.append(planet)

# Create moons orbiting each planet
moons = []
submoons = []
for planet in planets:
    num_moons = random.randint(1, 4)
    for _ in range(num_moons):
        orbit_radius = random.randint(30, 70)
        orbit_speed = random.uniform(1.0, 3.0)
        moon_radius = random.randint(5, 10)
        color = planet.color  # Inherit color from planet
        moon = Particle(
            x=planet.x,
            y=planet.y,
            radius=moon_radius,
            color=color,
            orbit_center=planet,
            orbit_radius=orbit_radius,
            orbit_speed=orbit_speed
        )
        moons.append(moon)

        # Create sub-moons orbiting each moon
        num_submoons = random.randint(1, 3)
        for _ in range(num_submoons):
            sub_orbit_radius = random.randint(15, 30)
            sub_orbit_speed = random.uniform(2.0, 5.0)
            submoon_radius = random.randint(2, 5)
            sub_color = moon.color  # Inherit color from moon
            submoon = Particle(
                x=moon.x,
                y=moon.y,
                radius=submoon_radius,
                color=sub_color,
                orbit_center=moon,
                orbit_radius=sub_orbit_radius,
                orbit_speed=sub_orbit_speed
            )
            submoons.append(submoon)

# Generate frames
total_frames = fps * seconds
for frame in range(total_frames):
    # Create a blank white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw the central particle
    cv2.circle(
        image,
        (int(center_particle.x), int(center_particle.y)),
        center_particle.radius,
        center_particle.color,
        -1,
        lineType=cv2.LINE_AA
    )

    # Update and draw planets
    for planet in planets:
        planet.update_orbit()
        if show_trajectories:
            for i in range(1, len(planet.trajectory)):
                cv2.line(
                    image,
                    (int(planet.trajectory[i-1][0]), int(planet.trajectory[i-1][1])),
                    (int(planet.trajectory[i][0]), int(planet.trajectory[i][1])),
                    planet.color,
                    1,
                    lineType=cv2.LINE_AA
                )
        cv2.circle(
            image,
            (int(planet.x), int(planet.y)),
            planet.radius,
            planet.color,
            -1,
            lineType=cv2.LINE_AA
        )

    # Update and draw moons
    for moon in moons:
        moon.update_orbit()
        if show_trajectories:
            for i in range(1, len(moon.trajectory)):
                cv2.line(
                    image,
                    (int(moon.trajectory[i-1][0]), int(moon.trajectory[i-1][1])),
                    (int(moon.trajectory[i][0]), int(moon.trajectory[i][1])),
                    moon.color,
                    1,
                    lineType=cv2.LINE_AA
                )
        cv2.circle(
            image,
            (int(moon.x), int(moon.y)),
            moon.radius,
            moon.color,
            -1,
            lineType=cv2.LINE_AA
        )

    # Update and draw sub-moons
    for submoon in submoons:
        submoon.update_orbit()
        if show_trajectories:
            for i in range(1, len(submoon.trajectory)):
                cv2.line(
                    image,
                    (int(submoon.trajectory[i-1][0]), int(submoon.trajectory[i-1][1])),
                    (int(submoon.trajectory[i][0]), int(submoon.trajectory[i][1])),
                    submoon.color,
                    1,
                    lineType=cv2.LINE_AA
                )
        cv2.circle(
            image,
            (int(submoon.x), int(submoon.y)),
            submoon.radius,
            submoon.color,
            -1,
            lineType=cv2.LINE_AA
        )

    # Display the frame
    cv2.imshow("Simulation", image)

    # Write the frame to the video
    video_writer.write(image)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_writer.release()
cv2.destroyAllWindows()

print(f"Video saved as {video_filename}")
