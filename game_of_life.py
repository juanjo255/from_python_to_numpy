## PYTHON IMPLEMENTATION
Z =     [[0,0,0,0,0,0],
        [0,0,0,1,0,0],
        [0,1,0,1,0,0],
        [0,0,1,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]

def python_impl (Z) -> None:

    ## Contamos los vecinos de cada celda
    ## De esta forma sabemos si tiene vecinos vivos (1) o muertos
    ## Con el resultado de cada celda podemos luego actualizar su resultado
    ## Con las reglas del juego de la vida
    shape = len(Z), len(Z[0])
    def compute_neighbours(Z):
        N  = [[0,]*(shape[0]) for i in range(shape[1])]
        print(N)
        for x in range(1,shape[0]-1):
            for y in range(1,shape[1]-1):
                N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                        + Z[x-1][y]            +Z[x+1][y]   \
                        + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
        return N


    ## Ahora necesitamos actualizar la matriz resultante de la funcion anterior
    ## Con los nuevos 0s y 1s de acuerdo con las reglas del juego de la vida
    def iterate(Z):
        N = compute_neighbours(Z)
        for x in range(1,shape[0]-1):
            for y in range(1,shape[1]-1):
                # Se muere
                if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                    Z[x][y] = 0
                # Vive
                elif Z[x][y] == 0 and N[x][y] == 3:
                    Z[x][y] = 1
        return Z

## NUMPY IMPLEMENTATION
def numpy_impl (Z) -> None:
    
    import numpy as np
    Z = np.array(Z)
    N = np.zeros(Z.shape, dtype=int)
    # CONTAR VECINOS
    N[1:-1,1:-1] += (Z[ :-2, :-2] + Z[ :-2,1:-1] + Z[ :-2,2:] +
                    Z[1:-1, :-2]                + Z[1:-1,2:] +
                    Z[2: , :-2] + Z[2: ,1:-1] + Z[2: ,2:])
    # IMPLEMENTAR REGLAS DE JUEGO
    # Flatten arrays
    # Se aplanan por facilidad ya que solo nos interesa encontrar la celda especifica en Z y N
    N_ = N.ravel()
    Z_ = Z.ravel()

    # Apply rules
    # Esta funcion permite encontrar los indices de las celdas que cumplen con la condicion
    # Busca para N y Z simultaneamente los mismos indices, por ende deben ser arrays del mismo largo. 
    # # R1 = np.argwhere( (Z_==1) & (N_ < 2) )
    # # R2 = np.argwhere( (Z_==1) & (N_ > 3) )
    # # R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
    # # R4 = np.argwhere( (Z_==0) & (N_==3) )

    # Set new values according to rules
    # Any live cell with fewer than two live neighbours dies, as if by needs caused by underpopulation.
    # # Z_[R1] = 0
    # # # Any live cell with more than three live neighbours dies, as if by overcrowding.
    # # Z_[R2] = 0
    # # # Any live cell with two or three live neighbours lives, unchanged, to the next generation.
    # # Z_[R3] = Z_[R3]
    # # # Any dead cell with exactly three live neighbours becomes a live cell.
    # # Z_[R4] = 1

    # Make sure borders stay null
    Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0
    
    # Replacement of arg.where function for a simpler and faster one
    ## Cells that change from 0 to 1
    birth = (N==3)[1:-1,1:-1] & (Z[1:-1,1:-1]==0)
    ## Cells that stay at 1
    ### Can be reduce to N>=2
    survive = ((N==2) | (N==3))[1:-1,1:-1] & (Z[1:-1,1:-1]==1)
    ## Initicialize all in zero
    Z[...] = 0
    ## Add 1 to the ones that gonna change from 0 to 1 or gonna stay at 1
    Z[1:-1,1:-1][birth | survive] = 1
    
    
numpy_impl(Z)