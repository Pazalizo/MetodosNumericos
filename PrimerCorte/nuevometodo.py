import numpy as np
import matplotlib.pyplot as plt

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar el tallo de la flor
ax.plot([0, 0], [-1, 1], color='green')

# Configurar el aspecto de la figura
ax.set_aspect('equal')
ax.axis('off')

# Crear varias flores
num_flowers = 5  # Number of flowers to create
for i in range(num_flowers):
    # Crear los datos para la flor
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sin((5+i)*theta) * np.cos((4+i)*theta)

    # Graficar la flor
    ax.plot(r * np.cos(theta), r * np.sin(theta), color='red')
    ax.fill(r * np.cos(theta), r * np.sin(theta), color='yellow')

# Mostrar la figura
plt.show()