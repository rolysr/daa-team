# Informe sobre solución al problema: ¿Jenga?
## Integrantes:
 - Andry Rosquet Rodríguez - C411
 - Rolando Sánchez Ramos - C411

## **1) Introducción al problema:**
En el archivo [¿Jenga?]() nos definen un problema donde a partir de una lista de números enteros que representan alturas de columnas formadas por palitos y la definición de costos de operaciones como colocar o quitar un palito encima de una columna o mover un palito encima de una columna hacia la parte superior de otra, debemos dar como respuesta el menor costo posible que sería necesario para igualar la altura de cada una de las columnas utilizando solamente dichas acciones definidas.

Nótese que el problema sería equivalente a, dado un array $hi$ de $n$ enteros y unos valores de costo de realizar cada operación definida anteriormente, $c$ (costo de colocar), $e$ (costo de quitar) y $m$ (costo de mover), se desea computar el mínimo costo total con el cual se podrían igualar los valores de dicho $array$. Por lo que el objetivo del problema se reduce a hallar el valor $min(c*n_c + e*n_e + m*n_m)$ donde $n_c, n_e$ y $n_m$ representan la cantidad de veces que se utilizó cada tipo de operación, se asume que $n_c, n_e, n_m \geq 0$ y se cumple que después de realizadas dichas operaciones $h_i = h_j ,\forall i, j$, donde $h_i$ representa la altura de la i-ésima columna. De esta forma se tiene bien definida la entrada y salida del algoritmo esperado.

## **2) Soluciones:**
El desarrollo de la mejor solución encontrada al problema se expone de manera iterativa, es decir, inicialmente se demostrará la correctitud de una solución intuitiva, la cual se irá mejorando a medida que probemos la correctitud de una serie de proposiciones que nos permitirán optimizar la complejidad temporal de cada algoritmo implementado.

### **2.1) Solución greedy #1:**
Inicialmente se pensó en la implementación de una solución utilizando un algoritmo de Backtracking, donde recursivamente se iterara por cada posición del array $hi$ de entrada y se decidiera si aumentar su altura por cierta cantidad, disminuir esta o en otro caso ver si es posible mover un palito de dicha columna hacia otra. Además, se debe notar que es necesario iterar por cada una de las posibles cantidades de veces que se pueden realizar dichas operaciones para cada posición de $hi$, esto con el objetivo de estar iterando realmente por todas las soluciones posibles. Finalmente, el caso base del Backtracking sería, un vez analizadas todas las posiciones del array de alturas y realizando un conjunto de operaciones válidas, se verifica que se calcularía el valor $c*n_c + e*n_e + m*n_m$ y se compararía con la mejor solución global que se tuviere hasta este momento.

La solución anteriormente explicada no aprovecha una serie de cuestiones intuitivas que vienen a la mente una vez nos sentamos a programarla. Primeramente, se puede notar que en cada iteración del Backtacking se puede dejar a una columna de un tamaño específico a partir de conjunto arbitrario de operaciones y posteriormente hacer lo mismo con otra columna, de tal forma que sea posible que después de dichas operaciones estas hayan quedado con distinto tamaño y por lo tanto, se estén generando casos que no son posible solución del problema, por lo que primeramente se propone, para cada altura posible, realizar el proceso de backtracking de tal forma que se tenga en cuenta a qué altura llevar una columna en un llamado determinado del Backtracking. Evidentemente, esto nos asegura que la solución generada recursivamente sea posible candidata en el caso base, aunque no necesariamente optimal, lo cual nos reduce el espacio de búsqueda general y la complejidad temporal al tener que preguntar solamente si el valor $c*n_c + e*n_e + m*n_m$ es menor que lo mínimo encontrado en anteriores casos bases analizados. Finalmente, dicho resultado es transitivo al algoritmo general, dado que se logra optimizar un subprocedimeinto del procedimiento general.

Por otro lado, vemos que al analizar las operaciones posibles para llevar la columna $hi_i$ a una altura prefijada $k$, si esta está debajo de dicha altura solo tiene sentido subirla, ya que bajarla la aleja más del formato de la solución deseada y le añade al costo global del algoritmo un valor no negativo, lo cual es posible que empeore la solución general. Esto ocurre análogamente para las columnas cuya altura inicial $hi_i$ está por encima del umbral que define una altura a la cual se quieren llevar todas las alturas iniciales de las columnas. También intuitivamente vemos que no tiene sentido variar la altura de una columna cuyo tamaño coincide con la altura objetivo, ya que se estaría añadiendo un costo no negativo que igualmente puede empeorar la solución general. Por lo tanto queremos demostrar la siguiente proposición:

#### **Proposición 2.1.1)** Sea $k$ una altura a la cual se desea llevar cada una de las columnas dadas inicialmente, se cumple que para cada altura $hi_i$, solo tiene sentido que esta aumente en caso de que $hi_i < k$, que disminuya si $hi_i > k$ y se mantenga igual si ocurre que $hi_i = k$.

Demostración: (Rellenar demostrando con un absurdo separando por casos posibles.)

Ahora, una vez que sabemos que para una altura específica $k$ a la cual se quiere igualar todas las columnas, solo es necesario subir las columnas con alturas debajo de dicho umbral, bajar las que queden por encima y mantener invariante aquellas cuya altura sea igual al umbral, entonces nos surge una idea que nos ayuda a evitar el Backtracking: En vez de probar con las posibles combinaciones entre todas las acciones admitidas para una columna en un momento dado, podemos para cada columna solo dedicidr cuánto bajar o subir en correspondencia a su relación con la altura pivote ($k$).

Analicemos ahora las situaciones posibles que se presentan cuando tiene sentido variar la altura de una columna. Supongamos que nos toca modificar una columna cuya altura $hi_i$ es menor estricta que la altura pivote $k$. Es evidente que las operaciones posibles para subirla son solamente combinaciones entre colocar con costo $c$ o mover con costo $m$ de otra columna $hi_j$. Es entonces que nos surge la idea de que, en el caso de que se vaya a mover un palito de $hi_j$ hacia $hi_i$, no tiene sentido que estos movimientos se hagan si $hi_j \leq hi_i$, o de forma más general, no tiene sentido que $hi_j \leq k$ con $i \neq j$. Esta idea se puede resumir en la siguiente proposición:

#### **Proposición 2.1.2)** Sea una columna con altura $hi_i < k$, donde $k$ es una altura pivote a la cual se quiere igualar. Dado que solo tiene sentido que $hi_i$ aumente, entonces si se decide aumentar con un movimiento de un palito de otra altura $hi_j$ con $i \neq j$ se debe cumplir que $hi_j > k$.

**Demostración:** (Haciendo un absurdo con los casitos en que $hi_j \leq k$)

Luego, sería interesante analizar cual es la mejor manera de distribuir acciones de colocar con costo $c$ y mover con costo $m$ con el objetivo de que $hi_i + c*no_c + m*no_m = k$. Ahora, cuando se analiza detenidamente el problema, no es difícil fijarse que la solución está en el mínimo entre el costo de igualar $hi_i$ con $k$ usando solo operaciones de inserción o usando operaciones de movimiento mientras sea posible más operaciones de inserción en caso de que se agoten los movimiento. Esto se intuye a partir de analizar qué sucede cuando el costo de mover es menor que el costo de quitar de una columna y colocar luego en otra, es decir, si $m < c + e$. Es interesante plantearnos esto ya que el proceso de mover es equivalente a quitar y colocar, pero la diferencia radica en cuál de estos procesos es óptimo respecto al costo de operaciones. Entonces necesitamos probar que:

#### **Proposición 2.1.3)** Sea una columna con altura $hi_i < k$, donde $k$ es una altura pivote a la cual se quiere igualar. Dado que solo tiene sentido que $hi_i$ aumente, los aumentos solo puenden ser de dos formas, y la que se escoja, es lo mejor que se puede hacer para llevar la altura $hi_i$ al valor de $k$:
 1. Si $m < c + e$, entonces realiza tantas acciones de movimiento como columnas existan con tamaño superior a $k$, y si no alcanza para igualar a $k$, entonces lo restante solo se puede rellenar utilizando operaciones de inserción.
 2. En caso contrario se hacen sólo operaciones de inserción para hacer que $hi_i = k$.

**Demostración:** (Demostrar con un análisis de casos y absurdos.)

Ahora, en el caso en que lleguemos a una columna con altura $hi_i > k$, dado que solo tiene sentido que esta disminuya su tamaño, las posibles operaciones a realizar son quitar un palito y disminuir su altura (con costo $e$), o mover el palito más arriba de esta hacia la parte superior de otra columna. Sucede que lo mejor que se puede hacer sobre una altura

### **2.2) Solución greedy #2:**

### **2.3) Solución greedy #2 + Búsqueda ternaria:**

### **2.4) Solución óptima para cuando $k >> n$:**

### **2.5) Solución óptima generalizada**
 
## **3) Organización del proyecto:**

## **4) Evaluadores y útiles implementados:**

