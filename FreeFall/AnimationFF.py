import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Leer datos del archivo
x_data = []
y_data = []

with open("caida.dat", "r") as file:
    for line in file:
        if line.strip():  # Ignorar líneas vacías
            x, y = map(float, line.split())
            x_data.append(x)
            y_data.append(y)

# Configurar el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], 'b-')
ax.set_xlim(min(x_data), max(x_data))
ax.set_ylim(min(y_data), max(y_data))
ax.set_xlabel('Distancia horizontal (m)')
ax.set_ylabel('Altura (m)')
ax.set_title('Animación de la Caída Libre')

# Inicialización de la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización para la animación
def update(frame):
    line.set_data(x_data[:frame], y_data[:frame])
    return line,

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True, interval=50)

plt.show()
