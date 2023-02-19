import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# DIBUJAR GRAFICO
height=10
width=10
fig, ax = plt.subplots()
ax.set_xlim([0, width])
ax.set_ylim([0, height])

# PROPIEDADES DEL ARRAY DE BOIDS
# PRIMERAS POSICIONES ALEATORIAS DE LOS BOIDS
boids_positions=np.random.uniform(0,10,(10,2))
# VELOCIDAD: NOS DETERMINA LA DIRECCION DE LOS BOIDS.
# CAMBIO EN LA POSICION. A DONDE SE MOVERAN LOS BOIDS?
boids_velocity = np.zeros((0,10))
# ACELERACION: NOS DIRA EN QUE MEDIDA SERA EL CAMBIO DE POSICION DEL BOID
# CAMBIO EN LA VELOCIDAD.
boids_accelaration = np.random.uniform(0.1,0.5,(0,10))

# TANTO VELOCIDAD COMO ACELERACION SE DEBEN LIMITAR 
# DE MODO QUE LOS BOIDS NO ALCANCEN LUGARES MUY RAPIDO 
# O HAYA MUCHA DIFERENCIA EN LA VELOCIDAD QUE ALCANZAN

# SCATTER ARTIST
scat2 = ax.scatter(boids_positions[:,0], boids_positions[:,1])

velocity=0.1

# FUNCION QUE SE LLAMARA REPETIDAMENTE PARA CREAR LA ANIMACION
def animate(i):
    global boids_positions
    boids_positions += (width, height)
    boids_positions %= (width, height)
    #scat.set_offsets([[x[i], 0],[1+x[i],0]])
    boids_positions+=velocity
    scat2.set_offsets(boids_positions)
    return scat2

ani = animation.FuncAnimation(fig, animate, repeat=True,frames=100, interval=50)
#len(x) - 1

plt.show()