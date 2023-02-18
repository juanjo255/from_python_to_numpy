import matplotlib.pyplot as plt
import numpy as np

## HACEMOS GRAFICO EN EL QUE SE MOSTRARAN LOS BOIDS
fig = plt.figure(facecolor="white")
ax = fig.add_subplot()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)


class boid ():
    def __init__(self) -> None:
        self.position = [np.random.randint(0,100), np.random.randint(0,100)]

boids = [boid() for _ in range (100)]
ypoints = np.array([[boid.position[1]] for boid in boids])
xpoints = np.array([[boid.position[0]] for boid in boids])


def update_plot() -> None:
    

plt.plot(xpoints,ypoints,"o")
plt.show()
