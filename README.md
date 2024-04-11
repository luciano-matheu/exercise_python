# exercise_python

El ejercicio cita lo siguiente:

Considera a un muchacho que se deleita pintando su tablero de ajedrez. Su objetivo es saturar cada celda con tonos rojos o azules. En busca de darle una identidad propia, procura tener un equilibrio entre los espacios rojos y azules, previniendo que dos filas o columnas contengan el mismo número de celdas rojas. ¿Lograría pintar el tablero de ajedrez siguiendo estas pautas? ¿Qué acontecería si, en vez de un tablero de ajedrez común de 8x8, tuviera uno monumental de 1000x1000?

Cabe aclarar que el ejercicio ya esta exageradamente comentado, pero acá va mi resolución:

La forma en la que decidí resolverlo fué a traves de la librería numpy, dado que podemos comparar una matriz de 8x8 con un tablero original de ajedrez y con el de cualquier otro tipo.
Inicié por supuesto importando a numpy y luego pasé a crear una función llamada board, la cual nos va a permitir ingresar el número total de casillas que va a tener el tablero en cuestión, de modo que, si ingresamos uno de 64, será de 8x8 y si ingresamos uno de un millón, será de mil por mil.
Dentro de la función creo una lista vacía que almacenará "1" y "0" donde 1 = casilla pintada.
Mediante un bucle while repito el número de veces que se va repetir dicho bucle, utilizando para ello el número que se ingresa a la funcíon - 1, para que una vez superado el mismo, el bucle se rompa.
Dentro del while inicio un bucle for y atentos acá (porque es lo que más me costó), el ejercicio pide dos cosas importantes que me tuvieron rato largo pensando: 1) Las casillas pintadas no deben tocarse de manera directa, es decir no puede haber en fila o columna dos casillas pintadas y 2) esto debe funcionar tanto en un tablero normal como en uno de tamaño masivo... entonces uso el bucle para crear la primer fila de 0 y 1, y el largo va a ser la raiz cuadrada del número ingresado dividido 2, lo cual va a permitir que dicha fila (y sus columnas) sean proporcionales a un tablero de ajedrez donde el largo y el ancho es el mismo. De este modo, si se ingresa 64, la raiz da 8 y dividido 2 = 4. En ese primer bucle añado la primer fila.
Para la segunda fila tenía que lograr que los 0 y 1 se inviertan de modo que no se toquen las casillas pintadas. Así que decidí usar un condicional (if - else) en donde hago que consulte si el último número en la fila recién creada termina en "1" (lo cual, sabemos que así será). Esto me permitió invertir la fila e ir intercalando una fila en una dirección y luego en otra, logrando el objetivo del ejercicio.
Cabe aclarar que podría haber importado el módulo "math" y usar la función "sqrt()", pero me pareció más prolijo hacerlo con una simple potencia ** 0.5.
Finalmente creo una matriz en base a la lista que cree con la ayuda de los bucles y condicionales y para que la forma que brinda mismo largo y ancho no deba ingresarla el usuario, simplemente repetí un proceso similar al de los bucles: usé la raiz cuadrada del número ingresado por el usuario pero esta vez no la dividí en dos, de modo que, si ingresa 64, el resultado es 8. Paso ese número por la función reshape() de numpy y ¡listo!

¿Había mejores formas de hacerlo?
- Seguramente

¿Mucho texto?
- Si :(

Pero es mi primer ejercicio resuelto en python y estoy orgulloso de ello :D
Saludos!
