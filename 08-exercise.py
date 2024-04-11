'''
Considera a un muchacho que se deleita pintando su tablero de ajedrez.
Su objetivo es saturar cada celda con tonos rojos o azules. En busca de darle una identidad propia,
procura tener un equilibrio entre los espacios rojos y azules, previniendo que dos filas o columnas
contengan el mismo número de celdas rojas. ¿Lograría pintar el tablero de ajedrez siguiendo estas pautas?
¿Qué acontecería si, en vez de un tablero de ajedrez común de 8x8, tuviera uno monumental de 1000x1000? 

'''

# Primero importé numpy para poder usar matrices que van a simbolizar a nuestro tablero de ajedrez.
import numpy as np

# Creé una función que recibe el número total de casilleros. Ej: tablero 8x8 ingresamos 64.
def board(size):
    
    # Dentro inicio una lista vacía que posteriormente se convertirá en una matriz.
    x = []
    
    # Mediante un ciclo while repito un bucle en relación a la cantidad de casilleros que recibe la función.
    # Utilizo el menos uno (-1) para que al llegar al número ingresado el bucle se rompa y no antes.
    while len(x) <= size - 1:

        # Dentro inicio un bucle for que cree la primer línea de 1 y 0, donde 1 = casilla pintada.
        for a in range(int((size ** 0.5) / 2)):
            # Añado a la lista "x" la primer fila de 0 y 1.
            x.append(0)
            x.append(1)

        # Utiliizo "if" para chequear que la siguiente fila no sea igual a la primera.
        # De este modo logro el objetivo de que no se junten por fila o columna casilla pintada.
        if x[-1] == 1:
        
            for b in range(int((size ** 0.5) / 2)):
                # Añado a la lista la segunda fila a la inversa: 1 y 0
                x.append(1)
                x.append(0)
        else:
            pass

    # Convierto la lista python a una matriz de numpy
    array = np.array(x)

    # Creo una variable equivalente a la raiz cuadrada del tamaño ingresado. Ej: 64 = 8
    shape = int(size ** 0.5)

    # Utilizo dicha variable para darle forma a la matriz como sería un casillero de ajedrez.
    return(array.reshape(shape, shape))

# Resultado: Una función que recrea lo que pide el enunciado.
print(board(64))