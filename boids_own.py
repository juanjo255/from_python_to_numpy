import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# PROPIEDADES DEL GRAFICO
height = 10
width = 10
fig, ax = plt.subplots()
ax.set_xlim([0, width])
ax.set_ylim([0, height])

# PROPIEDADES DEL ARRAY DE BOIDS
# NUMERO DE BOIDS
n_boids = 5

# PRIMERAS POSICIONES ALEATORIAS DE LOS BOIDS
boids_positions = np.random.uniform(0, 10, (n_boids, 2))

# VELOCIDAD: NOS DETERMINA LA DIRECCION DE LOS BOIDS.
# CAMBIO EN LA POSICION. A DONDE SE MOVERAN LOS BOIDS?
boids_velocity = np.zeros((n_boids, 2))

# ACELERACION: NOS DIRA EN QUE MEDIDA SERA EL CAMBIO DE POSICION DEL BOID
# CAMBIO EN LA VELOCIDAD.
boids_accelaration = np.random.uniform(0.01, 0.02, (n_boids, 2))

# SCATTER ARTIST
scat = ax.scatter(boids_positions[:, 0], boids_positions[:, 1])

## DISTANCIA DE UN BOID CON LOS DEMAS ##
# I need to compute the distance from one boid to another in order to modify acceleration
# using the rules with those that too close.


def distance():
    '''
    I need to calculate vector diferences with each vector, that is,
    if I have a matrix of 5x2, distances will return a matrix of 5x5, 
    each row will be a boid with distances to the other boids including itself
    '''
    print("boids position \n", boids_positions)
    
    # print("norm", np.linalg.norm(boids_positions) )


# TANTO VELOCIDAD COMO ACELERACION SE DEBEN LIMITAR
# DE MODO QUE LOS BOIDS NO ALCANCEN LUGARES MUY RAPIDO
# O HAYA MUCHA DIFERENCIA EN LA VELOCIDAD QUE ALCANZAN
max_speed = 2
max_acceleration = 0.03


# ESTA FUNCION ACUMULARA LAS FUERZAS QUE AFECTARAN EL MOVIMIENTO (VELOCIDAD) DE CADA VECTOR
# A TRAVES DE LA ACELERACION
# SIN EMBARGO INMEDIATAMENTE LIMITARA LA VELOCIDAD
def force(boids_velocity) -> None:
    boids_velocity += boids_accelaration
    boids_velocity.clip(0, max_speed)


# FUNCION QUE SE LLAMARA REPETIDAMENTE PARA CREAR LA ANIMACION
def animate(frame) -> None:
    global boids_positions, boids_velocity

    # Calculamos cuanto se estara moviendo cada boid
    force(boids_velocity)

    # Modificamos la posicion de los boids de acuerdo a las fuerzas calculadas
    # Aceleration -> Velocity -> Position
    boids_positions += boids_velocity

    # Wrap around
    boids_positions += (width, height)
    boids_positions %= (width, height)

    # Actualizar scatter plot con nuevas posiciones
    scat.set_offsets(boids_positions)


ani = animation.FuncAnimation(
    fig, animate, repeat=True, frames=1000, interval=100)
#plt.show()
