# Informe sobre solución al problema: ¿Jenga?
## Equipo: $D^{aa}$
## Integrantes:
 - Andry Rosquet Rodríguez - C411
 - Rolando Sánchez Ramos - C411

## **1) Introducción al problema:**
En el archivo [¿Jenga?]() nos definen un problema donde a partir de una lista de números enteros que representan alturas de columnas formadas por palitos y la definición de costos de operaciones como colocar o quitar un palito encima de una columna o mover un palito encima de una columna hacia la parte superior de otra, debemos dar como respuesta el menor costo posible que sería necesario para igualar la altura de cada una de las columnas utilizando solamente dichas acciones definidas.

Nótese que el problema sería equivalente a, dado un array $hi$ de $n$ enteros y unos valores de costo de realizar cada operación definida anteriormente, $c$ (costo de colocar), $e$ (costo de quitar) y $m$ (costo de mover), se desea computar el mínimo costo total con el cual se podrían igualar los valores de dicho $array$. Por lo que el objetivo del problema se reduce a hallar el valor $min(c*n_c + e*n_e + m*n_m)$ donde $n_c, n_e$ y $n_m$ representan la cantidad de veces que se utilizó cada tipo de operación, se asume que $n_c, n_e, n_m \geq 0$ y se cumple que después de realizadas dichas operaciones $h_i = h_j ,\forall i, j$, donde $h_i$ representa la altura de la i-ésima columna. De esta forma se tiene bien definida la entrada y salida del algoritmo esperado.

## **2) Soluciones:**
El desarrollo de la mejor solución encontrada al problema se expone de manera iterativa, es decir, inicialmente se demostrará la correctitud de una solución intuitiva, la cual se irá mejorando a medida que probemos una serie de proposiciones que nos permitirán optimizar la complejidad temporal de cada algoritmo implementado.

### **2.1) Solución greedy #1:**
Inicialmente se pensó en la implementación de una solución utilizando un algoritmo de Backtracking, donde recursivamente se iterara por cada posición del array $hi$ de entrada y se decidiera si aumentar su altura por cierta cantidad, disminuir esta o en otro caso ver si es posible mover un palito de dicha columna hacia otra. Además, se debe notar que es necesario iterar por cada una de las posibles cantidades de veces que se pueden realizar dichas operaciones para cada posición de $hi$, esto con el objetivo de estar iterando realmente por todas las soluciones posibles. Finalmente, el caso base del Backtracking sería, un vez analizadas todas las posiciones del array de alturas y realizando un conjunto de operaciones válidas, se verifica que se calcularía el valor $c*n_c + e*n_e + m*n_m$ y se compararía con la mejor solución global que se tuviese hasta ese momento.

La solución anteriormente explicada no aprovecha una serie de cuestiones intuitivas que vienen a la mente una vez nos sentamos a programarla. Primeramente, se puede notar que en cada iteración del Backtacking se puede dejar a una columna de un tamaño específico a partir de conjunto arbitrario de operaciones y posteriormente hacer lo mismo con otra columna, de tal forma que sea posible que después de dichas operaciones estas hayan quedado con distinto tamaño y por lo tanto, se estén generando casos que no son posible solución del problema, por lo que primeramente se propone, para cada altura posible, realizar el proceso de Backtracking de tal forma que se tenga en cuenta a qué altura llevar una columna en un llamado determinado del Backtracking. Evidentemente, esto nos asegura que la solución generada recursivamente sea posible candidata en el caso base, aunque no necesariamente optimal, lo cual nos reduce el espacio de búsqueda general y la complejidad temporal al tener que preguntar solamente si el valor $c*n_c + e*n_e + m*n_m$ es menor que lo mínimo encontrado en anteriores casos bases analizados. Finalmente, dicho resultado es transitivo al algoritmo general, dado que se logra optimizar un subprocedimeinto del procedimiento general.

Por otro lado, vemos que al analizar las operaciones posibles para llevar la columna $hi_i$ a una altura prefijada $k$, si esta está debajo de dicha altura solo tiene sentido subirla, ya que bajarla la aleja más del formato de la solución deseada y le añade al costo global del algoritmo un valor no negativo, lo cual es posible que empeore la solución general. Esto ocurre análogamente para las columnas cuya altura inicial $hi_i$ está por encima del umbral que define una altura a la cual se quieren llevar todas las alturas iniciales de las columnas. También, intuitivamente vemos que no tiene sentido variar la altura de una columna cuyo tamaño coincide con la altura objetivo, ya que se estaría añadiendo un costo no negativo que igualmente puede empeorar la solución general. Por lo tanto queremos demostrar la siguiente proposición:

#### **Proposición 2.1.1)** Sea $k$ una altura a la cual se desea llevar cada una de las columnas dadas inicialmente, se cumple que para cada altura $hi_i$, solo tiene sentido que esta aumente en caso de que $hi_i < k$, que disminuya si $hi_i > k$ y se mantenga igual si ocurre que $hi_i = k$. Además, no se tiene sentido que $k < min(hi)$ ni $k > max(hi)$.

Demostración:

#### **¿Todo lo que sube, nunca baja?**

Demostremos ahora que si se desea llevar una columna $n$ a una altura $k$ entonces:

1.	Si altura de $z$<$k$ entonces a $z$ siempre se le aumentará su altura hasta alcanzar $k$ y por tanto nunca se le realizará operaciones que disminuyan su altura.
2.	Si altura de $z$=$k$ entonces no se requiere cambio alguno. Cualquier operación sobre dicha columna será un costo innecesario ya que esta tiene la altura deseada.
3.	Si altura de $z$>$k$ entonces a $z$ siempre se le disminuirá su altura hasta alcanzar $k$ y por tanto nunca se le realizará operaciones que aumenten su altura.

Podemos notar que los puntos 1 y 3 son situaciones análogas y como se podrá apreciar a continuación la demostración aborda ambos a la vez.
Para dicha demostración asumamos que tanto el punto 1 como el 3 no se cumplen en algún momento y por tanto se generan todas las posibles situaciones que lleven a una contradicción en alguno de ellos:

1.	Se colocó un palito en la columna $z$ y luego se eliminó un palito en la misma.
2.	Se colocó un palito en la columna $z$ y luego se movió a otra columna $n$.
3.	Se eliminó un palito de la columna $z$ y luego se colocó uno en la misma.
4.	Se eliminó un palito de la columna $z$ y luego se movió de una columna $n$ a $z$ un palito.
5.	Se movió un palito de $n$ a $z$ y luego se eliminó uno de $z$.
6.	Se movió un palito de $z$ a $n$ y luego se colocó de vuelta un palito en $z$.
7.	Se movió un palito de $z$ a $n$ y luego se movió otro de $x$ a $z$, donde $x$ puede ser $n$.
8.	Se movió un palito de $n$ a $z$ y luego se movió otro de $z$ a $x$, donde $x$ puede ser $n$.

Ahora demostremos que todas son operaciones no factibles debido a los costos de cada operación. Para ello a continuación se demostrará la infactibilidad de cada uno de los puntos:
1.	Al colocar un palito en la columna $z$ y luego eliminarlo entonces esta volvió a su estado anterior (subió y bajó). Para ello realizamos operaciones con costo $c+e \ge 0$ y sin embargo el estado de las columnas permanece intacto, por tanto, infactible. 
2.	Al colocar un palito en la columna $z$ y luego moverlo a $n$ entonces $z$ cambio su estado y luego volvió al anterior (subió y bajó) y $n$ aumentó su altura en 1. Para ello se realizaron operaciones con costo $c+m$ y sin embargo colocando un palito en $n$ era suficiente para alcanzar el estado antes descrito. Lo anterior tiene costo $c \leq c+m$ el cual era el costo de la operación 2, por tanto, infactible.
3.	Al eliminar un palito de $z$ y luego colocar en dicha columna 1 palito esta cambió su estado y luego volvió al anterior (bajó y subió). Para ello realizamos operaciones con costo $c+e \ge 0$ y sin embargo el estado de las columnas permaneció intacto, por tanto, infactible.
4.	Al eliminar un palito de $z$ y luego mover de $n$ a $z$ otro, la columna cambió su estado y luego volvió al anterior (bajó y subió). Para ello se realizaron operaciones con costo $m+e$ y sin embargo solo era necesario eliminar un palito de $n$ para alcanzar el estado antes descrito. Lo anterior tiene costo $e \leq m+e$ que es el costo de la operación 4, por tanto, infactible.
5.	Al mover un palito de $n$ a $z$ y luego eliminar uno de la columna $z$, esta cambió su estado y luego regresó al anterior ( subió y bajó). Para ello se realizaron operaciones con costo $m+e$ y solo era necesario eliminar un palito de la columna $n$ para llegar al estado antes descrito. Lo anterior tiene costo $e \leq m+e$ que es el costo de la operación 5, por tanto, infactible.
6.	Al mover un palito de $z$ a $n$ y luego colocar en $z$ uno nuevo, se alteró la columna y luego regresó a su rayado anterior (bajó y subió). Para ello se realizaron operaciones con costo $m+c$ y solo era necesario colocar un palito en $n$ para alcanzar el estado antes descrito. Lo anterior tiene costo $c \leq m+c$ que es el costo de la operación 6, por tanto, infactible.
7.	Al mover un palito de $z$ a $n$ y luego mover desde una columna $x$ a $z$ otro palito, se alteró el estado de $z$ y luego regresó al anterior (bajó y subió). Para ello se realizaron operaciones con costo $2m$ y sin embargo era suficiente mover un palito de $x$ a $n$ para alcanzar el estado antes descrito. Notar que si $x$ es $n$ entonces no es requerida ninguna operación. Mover de $x$ a $n$ tiene costo $m \leq 2m$ que es el costo de la operación 7, por tanto, infactible.
8.	Al mover un palito de $n$ a $z$ y luego mover a una columna $x$ un palito de $z$, se alteró el estado de $z$ psra luego regresar al anterior (subió y bajó). Para ello se realizaron operaciones con costo $2m$ y sin embargo era suficiente mover un palito de $n$ a $x$ para alcanzar el estado antes descrito. Notar que si $x$ es $n$ entonces no es requerida ninguna operación. Mover de $n$ a $x$ tiene costo $m \leq 2m$ que es el costo de la operación 8, por tanto, infactible.

Como encontramos una contradicción en cada uno de los casos posibles entonces la hipótesis que indicaba que los puntos 1 y 3 no se cumplían, es falsa y por tanto podemos afirmar que si se cumplen.

#### **Respeta los límites**.

Demostremos que si la altura $k$ es la óptima según sus costos de operaciones necesarias para llevar todas las columnas del array a dicha altura entonces $Min$(alturas del array)$ \leq k \leq Máx$(alturas del array).
Para ello hay que demostrar:
1.	Nunca se cumplirá que $k<Min$(alturas del array).
2.	Nunca se cumplirá que $k>Máx$(alturas del array).

Demostremos 1:

Asumamos, sin pérdida de la generalidad, que se cumple que $k<Min$(alturas del array) para algún caso. Si $x=Min$(alturas del array), $g$ es el costo óptimo de las operaciones necesarias para llevar el array a altura $x$ y $n$ es el array resultantes con todas las columnas igual a $x$. 

Entonces obligatoriamente debemos eliminar palitos de cada columna de $n$ hasta llevar cada una a altura $k$, demostremos esta afirmación. Podemos descartar colocar palitos ya que sabemos que las columnas deben disminuir hasta $k$ y por la proposición anterior sabemos que no tiene sentido aumentar si luego va a disminuir. Ahora para descartar el mover palitos podemos utilizar lo mismo puesto que al mover de $z$ a $p$ estaríamos disminuyendo la altura de $z$ pero a la par aumentamos la de $p$ que ya conocemos debemos disminuirla luego. Por tanto, solo queda la única operación lógica para la situación, eliminar palitos.

Como es necesario eliminar $(x-k)*$(dimensión del array)$>0$ palitos con costo $r=e*(x-k)$(dimensión del array)$>0$ entonces finalmente para llevar todas las columnas del array a altura $k$ costará $g+r$. Pero sabemos que $r>0$ por tanto $g+r>g$, entonces llevar el array a altura $x$ es un óptimo comparado con llevarlo a altura $k$. Encontramos una contradicción, por tanto, podemos concluir que la hipótesis no se cumple, entonces $k>Min$(alturas del array).

El punto 2 es análogo con la diferencia que solo se realizarían operaciones de colocar, con lo cual se cubre la demostración de la proposición.

Ahora, una vez que sabemos que para una altura específica $k$ a la cual se quiere igualar todas las columnas, solo es necesario subir las columnas con alturas debajo de dicho umbral, bajar las que queden por encima y mantener invariante aquellas cuya altura sea igual al umbral, entonces nos surge una idea que nos ayuda a evitar el Backtracking: En vez de probar con las posibles combinaciones entre todas las acciones admitidas para una columna en un momento dado, podemos para cada columna solo dedicidir cuánto bajar o subir en correspondencia a su relación con la altura pivote ($k$).

Analicemos ahora las situaciones posibles que se presentan cuando tiene sentido variar la altura de una columna. Supongamos que nos toca modificar una columna cuya altura $hi_i$ es menor estricta que la altura pivote $k$. Es evidente que las operaciones posibles para subirla son solamente combinaciones entre colocar con costo $c$ o mover con costo $m$ de otra columna $hi_j$. Es entonces que nos surge la idea de que, en el caso de que se vaya a mover un palito de $hi_j$ hacia $hi_i$, no tiene sentido que estos movimientos se hagan si $hi_j \leq hi_i$, o de forma más general, no tiene sentido que $hi_j \leq k$ con $i \neq j$. Esta idea se puede resumir en la siguiente proposición:

#### **Proposición 2.1.2)** Sea una columna con altura $hi_i < k$, donde $k$ es una altura pivote a la cual se quiere igualar. Dado que solo tiene sentido que $hi_i$ aumente, entonces si se decide aumentar con un movimiento de un palito de otra altura $hi_j$ con $i \neq j$ se debe cumplir que $hi_j > k$.

**Demostración:**

Si elegimos $hi_j < k$, entonces al mover un palito de dicha columna a $hi_i$ estaríamos disminuyendo la altura de $hi_j$. Pero sabemos que las columnas con altura menor que el pivote $k$ solo pueden aumentar para alcanzar dicha altura, luego, no es válido mover un palito de $hi_j<k$ hacia $hi_i$ ya que estaríamos contradiciendo la proposición $2.1.1)$ y se termina la demostración.

Luego, sería interesante analizar cual es la mejor manera de distribuir acciones de colocar con costo $c$ y mover con costo $m$ con el objetivo de que $hi_i + c*no_c + m*no_m = k$. Ahora, cuando se analiza detenidamente el problema, no es difícil fijarse que la solución está en el mínimo entre el costo de igualar $hi_i$ con $k$ usando solo operaciones de inserción o usando operaciones de movimiento mientras sea posible más operaciones de inserción en caso de que se agoten los movimiento. Esto se intuye a partir de analizar qué sucede cuando el costo de mover es menor que el costo de quitar de una columna y colocar luego en otra, es decir, si $m < c + e$. Es interesante plantearnos esto ya que el proceso de mover es equivalente a quitar y colocar, pero la diferencia radica en cuál de estos procesos es óptimo respecto al costo de operaciones. Entonces necesitamos probar que:

#### **Proposición 2.1.3)** Sea una columna con altura $hi_i < k$, donde $k$ es una altura pivote a la cual se quiere igualar. Dado que solo tiene sentido que $hi_i$ aumente, los aumentos solo puenden ser de dos formas, y la que se escoja, es lo mejor que se puede hacer para llevar la altura $hi_i$ al valor de $k$:
 
**Demostración:**

#### **¡Seamos greedys!**
Caso $m<c+e$ donde hay columnas con altura menor que $k$ y otras con altura mayor que $k$:

En este caso siempre será óptimo realizar movimientos de palitos de una columna $x$ con altura mayor que $k$ a otra $z$ con altura menor que $k$, en lugar de colocar en $z$ y luego en un futuro eliminar de $x$. Para demostrarlo, es sencillo notar que si se desea incrementar el tamaño de $z$ y tenemos columna/s $x$ con altura mayor que $k$, entonces se podrá decrementar la/s columna/s $x$ en la misma operación. Esto se debe precisamente a que el costo de mover será mejor que colocar y luego eliminar. En caso de que no exista columna $x$ con altura mayor que $k$, solo resta hacer inserciones.

Caso $m>c+e$:

Al contrario que en el caso anterior, ahora se puede apreciar que es mejor eliminar un palito de $x$ y luego colocar en $z$, en lugar de mover de una columna a otra. Esto se debe precisamente a los costos de cada operación, donde la suma del costo de eliminar un palito junto a colocar otro, tendrá menor valor que mover de una columna a otra. Por tanto nunca resultará óptimo mover porque el resultado de dicha operación puede ser logrado combinando las otras dos en un menor costo.

Caso $m=c+e$:

Ahora tendremos la posibilidad de escoger cualquiera de los dos procedimientos antes descritos (mover de una columna a otra o colocar un palito en "z" y eliminar en "x") puesto que ambas costarán lo mismo. En nuestros algoritmos decidimos mover en algunos y en otros eliminar y colocar. 

Por lo tanto logramos demostrar la correctitud de la proposición para los casos posibles.

Ahora, en el caso en que lleguemos a una columna con altura $hi_i > k$, dado que solo tiene sentido que esta disminuya su tamaño, las posibles operaciones a realizar son quitar un palito y disminuir su altura (con costo $e$), o mover el palito más arriba de esta hacia la parte superior de otra columna (con costo $m$). Sucede que lo mejor que se puede hacer sobre una columna con estas características es algo análogo a la proposición $2.1.3)$ pero sucede que esto no nos dice mucho, ya que no nos permite converger a una metodología para saber qué hacer cuando llegamos a una columna de este estilo, dado el procedimiento mencionado con dicha proposición para ajustar la altura de aquellas columnas por debajo del umbral $k$.

Debido a estas ideas anteriores, vemos que existe un problema a la hora de decidir de qué forma podemos encontrar para una columna con altura inferior a la altura pivote (en el caso de que sea mejor realizar acciones de movimiento) aquellas columnas con tamaño superior (análogamente para una columna encima del umbral y que haga falta hallar otra por debajo para hacer acciones de movimiento), tal que puedan servir para quitarle palitos que participen en dicha acción. Existen una idea directa que consiste en recorrer todo el array $hi$ solo hacia la derecha de la columna actual y determinar aquellas que están por encima del umbral e ir quitándole los palitos necesarios hasta que sea posible. Por otro lado, si llegamos a una columna encima del umbral, vemos que debemos ver a la derecha, en caso de ser necesarias acciones de movimiento, cuáles están debajo del umbral. La idea de por qué funciona es por el principio básico de que estamos iterando de izquierda a derecha, llevando todas las alturas al umbral deseado, por lo que a la izquierda de la columna que se analiza en un momento dado solo habrán alturas igualadas al umbral y a la derecha alturas que puedan estar encima, debajo o al mismo nivel. Intuitivamente lo que estamos haciendo es nivelando de izquierda a derecha las alturas, por esto podemos argumentar la idea anterior.

Una propuesta para simplificar la forma de operar sobre las columnas es si las ordenáramos inicialmente, luego, al iterar por cada una vemos que una vez que logremos nivelar las alturas menores al umbral mediante el procedimiento de la proposición $2.1.3)$, al llegar a las alturas por encima del umbral sólo sería ncesario que estas disminuyan su altura. Por lo tanto, es necesario probar que:

#### **Proposición 2.1.4)** Si se aplicara el algoritmo de iterar por cada columna nivelándola a una altura pivote $k$ aplicando el procedimiento de la proposición $2.1.3)$ y haciendo este de forma análoga para cuando $hi_i > k$. Entonces, el resultado es equivalente a cuando lo hacemos sobre el array ordenado y cuando una columna cumple que su altura es $hi_i > k$, solo es necesario realizar operaciones de quitar palitos.

**Demostración:**

Sabemos que todas las columnas con alturas menores que $k$ deberán aumentar en cada operación que se haga sobre ellas y las de altura mayor que $k$ solo deberán disminuir, esto por proposición $2.1.2)$. Disponemos ya de una estrategia para escoger la forma óptima de aumentar y de disminuir columnas, proposición $2.1.3)$. Luego, teniendo las columnas ordenadas de menor a mayor, iterando por cada una de ellas y conociendo que operación o combinación de operaciones son las óptimas, se podrá establecer el procedimiento de $2.1.4)$ de la siguiente manera:

Para las columnas $x$ de altura menor que $k$ determinamos la cantidad de palitos necesarios para alcanzar $k$ y luego procedemos a calcular el costo óptimo de llevar a cabo dicha acción. 
1. Conocemos que si el óptimo es colocar y eliminar ya que $m>c+e$; entonces no hay mucho que analizar, calculamos $(k-x)*c$ y esto será lo mejor para dicha columna. 
2. Pero si lo mejor es mover palitos por la relación de costos entonces debemos determinar el número de palitos disponibles en las columnas $z$ con alturas mayores que $k$, que pueden ser movidos hacia $x$. 

Entonces utilizando lo antes descrito podemos notar que si nos encontramos en 1, es una situación bastante sencilla, las alturas menores que $k$ serán aumentadas con operaciones de inserción y cuando se llega a las de altura mayor que $k$ solo podremos eliminar palitos. Sin embargo, si estamos en 2 entonces se irán moviendo palitos de las columnas $z$ hacia $x$; con lo cual pueden darse dos nuevas situaciones. La primera es que las columnas $x$ alcancen $k$ solo moviendo palitos desde $z$ y por tanto, solo resta eliminar los palitos en $z$ que hacen que existan columnas con altura mayor que $k$; si no existen dichos palitos significa que no quedan columnas con alturas distintas de $k$ y por tanto el array se encuentra nivelado. La segunda situación, es que por el proceder de ir moviendo de $z$ a $x$ se agoten las columnas de altura mayor que $k$ ($z$) y por tanto es obligatorio colocar palitos en las columnas que aún poseen alturas menor que $k$. Entonces podemos notar que en la iteración cuando llegamos a las columnas,que en el estado inicial poseían altura mayor que $k$, en ciertas ocasiones no requerirá realizar ninguna operación porque ya alcanzaron la altura $k$ mientras se movían palitos hacia $x$, o solo restará eliminar todos los sobrantes producto de que es la operación óptima o que las columnas que tenían altura menor que $k$ ya alcanzaron dicho estado.

Finalmente, gracias a las proposiciones anteriores, el siguiente algoritmo ofrece la respuesta al problema planteado:

**Idea general de solución:** 
Dado un array de enteros $hi$ de tamaño $n$ y costos $c$, $e$ y $m$ almacenamos en $min_{hi}$ y $max_{hi}$ las alturas mínima y máxima en el array. Luego, ordenamos $hi$ en orden creciente. Posteriormente, para cada posible altura $min_{hi} \leq k \leq max_{hi}$ ejecutamos el procedimiento descrito anteriormente para cada columna $i$:
- Si $hi_i = k$ no se hace nada.
- Si $hi_i < k$, agregamos a la solución global para la altura $k$ el mínimo entre los procedimientos mencionados en $2.1.3)$.
- Si $hi_i > k$, solo agregamos a la solución global para $k$ el costo de bajar la columna con operaciones de quitar (con costo $e$) exclusivamente.

**Pseudocódigo:**
```
greedy1(n, hi, c, e, m):
    min_h = min(hi)
    max_h = max(hi)
    answer = inf
    hi.sort() # sort the heights

    for height in range(min_h, max_h + 1):
        cpy = [x for x in hi]
        result = solve(n, cpy, c, e, m, height)
        answer = min(result, answer)

    return answer

solve(n, hi, c, e, m, height):
    result = 0

    for x in hi:
        if x = height:
            do nothing
        elif x < height:
            result += min(c*(height-x), m*(number_of_needed_noves)+c*(height-new_x))
        else:
            result += e*(x-height)

    return result
```

El algoritmo está implementado en [greedy1.py]().

**Complejidad temporal:**
La complejidad temporal de hallar el máximo y mínimo de $hi$ se puede lograr en $\Omicron{(n)}$, luego el proceso de ordenamiento de $hi$ se puede lograr en $\Omicron(n\log{n})$ a partir de un ordenamiento con el algoritmo de *Merge Sort*. Por otro lado, el método *solve(...)* se ejecuta en $O(n^2)$ ya que por cada elemento del array $hi$ en la posición $i$, se hacen a lo sumo $n-i$ operaciones buscando los elementos a la derecha con los cuales verificar si es posible realizar las acciones de movimiento, por lo tanto, $solve(...)$ tiene complejidad temporal $O(n^2)$ en el peor caso. Finalmente, dado que por cada altura posible se ejecuta el método $solve(...)$ y se ejecuta la creación de un array copia de $hi$ en $\Omicron(n)$ (esto es necesario ya que durante el método $solve(...)$ se varía $hi$ para simular las variaciones en las columnas y de esta forma se evita que persistan los cambios una vez se salga del método), se cumple que el $for$ que realiza este proceso tiene un costo en el peor caso de $\Omicron{(m)}*\Omicron{(n + n^2)} = \Omicron{(mn^2)}$, donde $m=max_{hi}-min_{hi}$. Finalmente, el costo total sería $\Omicron(n + n + n\log{n} + m*n^2) = O(mn^2)$.

### **2.2) Solución greedy #2:**
Al analizar el proceso del método $solve(...)$ propuesto, vemos que no es necesario tener que simular todo el proceso *voraz* de realizar las variaciones de alturas ya que si nos fijamos, solo nos interesan las cantidades totales de palitos por debajo y por encima del umbral de una altura pivote $k$, que se quiere "rellenar" o "quitar". Esta idea intuitiva nos permite deducir que, para determinar el costo mínimo de variar las columnas con altura distinta de $k$, debemos pensar en una idea en la que solo necesitemos las unidades de palitos que deben ponerse encima de aquellas columnas debajo del umbral y aquellas que debemos sustraer de forma análoga para las columas encima de este. Como ya demostramos, no tiene sentido variar las columnas con altura igual a la que queremos llegar.

Una vez que tenemos los valores $count_{ups}$ y $count_{downs}$ referentes a las unidades de palitos que deben "rellenarse" y "quitarse" respectivamente, pasamos a analizar otro hecho interesante ya demostrado: el caso donde $m <= c + e$ (el costo de mover es mejor o igual que el costo de quitar y de poner). Es posible demostrar que no tiene sentido usar operaciones de movimiento cuando estas son más costosas que realizar de manera seguida los procesos de quitar y poner palitos y, en caso contrario es conveniente hacer el movimiento siempre que sea posible. Aunque parezca que esto es parecido a la proposicion **$2.1.3)$**, se debe notar que en esta ocasión, se desea dar una respuesta global dadas las cantidades $count_{ups}$ y $count_{downs}$. Por lo que debemos demostrar que:

#### **Proposición 2.2.1)** Sean los valores $count_{ups}$ y $count_{downs}$ calculados:
1. Si $count_{ups} = count_{downs}$ y $m < c + e$, entonces el costo mínimo de igualar las alturas es $count_{ups}*m$.
2. Si $count_{ups} < count_{downs}$ y $m < c + e$, entonces el costo mínimo de igualar las alturas es $count_{ups}*m + (count_{downs} - count_{ups})*e$.
3. Si $count_{ups} > count_{downs}$ y $m < c + e$, entonces el costo mínimo de igualar las alturas es $count_{downs}*m + (count_{ups} - count_{downs})*c$.
4. En otro caso, el costo mínimo de operaciones es $count_{ups}*c + count_{downs}*e$.

**Demostración:** 

Para demostrar 1, podemos apreciar que el número de palitos requeridos a ubicar en las columnas con alturas menores que $k$ son igual al número que se deben eliminar de las columnas con alturas mayores que $k$. Sabemos que $m<c+e$ luego por proposición $2.1.2)$ tenemos que lo óptimo será mover palitos siempre que sea posible. Por tanto, debemos mover y al tener un igual número de palitos en ambos lados del umbral $k$ el costo de nivelar las columnas a $k$ será $m*count_{ups}$ o $m*counts_{downs}$. 

Para demostrar 2, podemos utilizar la demostración de la proposición $2.1.4)$. En ella concluimos que si $m<c+e$ entonces se deberán mover todos los palitos posibles desde las columnas con altura mayor que $k$ hacia aquellas con altura menor que $k$. Por tanto, si $count_{ups}<count_{downs}$ se moverán todos los palitos posibles hasta que las columnas por debajo del umbral $k$ lo alcancen, esto se hará con costo $m*count_{ups}$. Pero, sabemos que aún restaron $count_{downs}-count_{ups}$ palitos en las columnas por encima del umbral, estos deberán ser eliminados, resultado que se puede apreciar en la demostración de $2.1.4)$. Finalmente, eliminar dichos palitos costará $e*(count_{downs}-count_{ups})$, resultando en un costo total $count_{ups}*m + (count_{downs} - count_{ups})*e$.

Para demostrar 3, podemos apreciar que es una situación análoga a 2. Con la diferencia que en lugar de eliminar los palitos restantes en las columnas con alturas por encima del umbral $k$ ahora los $count_{downs}$ no son suficientes para llevar las columnas con alturas por debajo del umbral $k$ hasta este. Por tanto, es requerido colocar palitos en dichas columnas. Mover todos los palitos posibles costará $count_{downs}*m$ y luego colocar los faltantes en las columnas por debajo del umbral $(count_{ups} - count_{downs})*c$, resultando en $count_{downs}*m + (count_{ups} - count_{downs})*c$.
Para demostrar 4, podemos utilizar la proposición 2.1.3, específicamente el caso 2 y el 3. Estos nos dicen que si $c+e \leq m$ entonces mover no es una operación óptima o resulta igual colocar y eliminar. Por tanto, se podrá colocar palitos en todas las columnas con altura menor que el umbral $k$ y eliminar en todas aquellas con alturas mayores. Esto costará $count_{ups}*c + count_{downs}*e$.

**Idea general de solución:** 
Dada la proposición $2.2.1)$, es posible realizar el método $solve(...)$ con un sólo recorrido sobre el arreglo de alturas, además, podemos eliminar el factor de ordenación ya que el cálculo del nuevo método $solve(...)$ es posible con el array $hi$ original. La idea sería hallar los valores $count_{ups}$ y $count_{downs}$ y luego verificar el cumplimiento de las condiciones mencionadas en $2.2.1)$ y devolver como resultado lo correspondiente aquella que se cumpla.

**Pseudocódigo:**
```
greedy2(n, hi, c, e, m):
    min_h = min(hi)
    max_h = max(hi)
    answer = inf

    for height in range(min_h, max_h + 1):
        result = solve(n, hi, c, e, m, height)
        answer = min(result, answer)

    return answer

solve(n, hi, c, e, m, height):
    count_ups, count_downs = compute_count_ups_downs(...)
    result = 0

    if count_ups == count_downs and m <= c + e:
        result = count_ups*m

    elif count_ups < count_downs and m <= c + e:
        result = count_ups*m + (count_downs - count_ups)*e

    elif count_ups > count_downs and m <= c + e:
        result = count_downs*m + (count_ups - count_downs)*c

    else:
        result = count_ups*c + count_downs*e

    return result
```
El algoritmo está implementado en [greedy2.py]().

**Complejidad temporal:**
En este caso, se elimina el factor de ordenamiento en $O(n\log{n})$ de la solución anterior y se varía el método $solve(...)$ a una implementación en $O(n)$ ya que en este solo se itera una vez por $hi$ verificando las columnas con altura menor o mayor que $k$ y aumentando o disminuyendo las variables $count_{ups}$ y $count_{downs}$ mientras sea necesario. Finalmente, el algoritmo mejora su complejidad a $O(n*m)$. 

### **2.3) Solución greedy #2 + Búsqueda ternaria:**
Una de las grandes interrogantes del problema es si es posible encontrar de forma más eficiente la altura óptima a la cual igualar todas las columnas con el mínimo costo de operaciones posibles. Algunas ideas iniciales erróneas nos hacían pensar que era posible que la altura óptima siempre coincidiría con la altura de alguna columna, algo que se logró comprobar como incorrecto a partir de un *script* que generaba casos de prueba y verificaba con los algoritmos anteriores si la altura resultante coincidía con la altura inicial de alguna de las columnas y se notaba que no siempre era cierto.

Una idea interesante para ganar intuición sobre el comportamiento de las alturas con respecto al costo mínimo de igualar todas las columnas de $hi$ a esta es imprimiendo dichos costos uno al lado del otro, representando que el costo $c_i$ era correspondiente a la i-ésima altura. Luego, a partir de este experimento notamos que para cada instancia del problema, había una altura a partir de la cual, las soluciones solo empeoraban, incluso, habían casos donde había un cojunto de alturas consecutivas que eran óptimas. Por lo tanto, sería interesante graficar en un plano de bidimensional los puntos $(h, result)$ donde $h$ es una altura y $result$ es el costo mínimo de llevar las columnas a dicha altura. Para este experimento implementamos un plotter sencillo y estos fueron los resultados para algunas instancias aleatorias del problema:

![img1](img/plot1.png)
![img1](img/plot2.png)
![img1](img/plot3.png)
![img1](img/plot4.png)
![img1](img/plot5.png)

A partir de estos experimentos, resulta interesante analizar que estas funciones cumplen que poseen un solo mínimo y en caso de tener más de uno, todos son provenientes de valores consecutivos en el eje de las alturas. Nótese que esta definición es idéntica a la de función unimodal, donde el único extremo en este caso es un mínimo. Por lo tanto debemos demostrar que:

#### **Proposición 2.3.1)** Sea la función $f(h) = r$, donde $h$ es una altura de un rango válido en una instancia del problema Jenga y $r$ es el costo mínimo de igualar todas las alturas de las columnas $hi$ a $h$, esta es unimodal:

**Demostración:** 

De forma general, una función unimodal de dos dimensiones puede verse como una función con un punto $x$ tal que $f(x)$ es el mínimo (o máximo) de la función y se cumple que $\forall{x'}, x' < x, f(x') \geq f(x)$, y la función es monótona decreciente a la izquierda y $\forall{x'}, x' > x, f(x') \geq f(x)$, y la función es monótona creciente para los valores a la derecha de $x$. Análogamente, esto se cumple para las funciones unimodales con máximo, pero alternado los tipos de monotonía respecto al caso cuando es unimodal de mínimo.

Para el caso específico de este problema, es necesario demostrar que $f(h) = r$ es una función unimodal de mínimo, es decir, existe una altura para la cual se alcanza el valor óptimo de solución del problema y todas las alturas menores o mayores cumplen que tienen evaluaciones mayores o iguales al valor de la función en dicho punto y a la izquierda de esta, $f$ es decreciente y a su derecha, creciente.

Por definición del problema, siempre va a existir al menos un punto donde la función alcance su valor óptimo mínimo, esto ya que trivialmente pudiéramos iterar por los posibles valores de las alturas dadas y quedarnos con aquel que de como resultado el menor costo de las operaciones para igualar todas las columnas de $hi$ a esta. Ahora, suponiendo la existencia de un mínimo, es evidente que toda altura válida menor o mayor que esta producirá valores mayores iguales al valor óptimo hallado, ya que en caso contrario, la altura denotada como óptima no lo sería, ya que existiría otra con una evaluación estrictamente menor. Luego, lo que resulta interesante para demostrar es que la función a la izquierda de $h$ es monótona decreciente y la de la derecha, monótona creciente. Para esto vamos a realizar la demostración para el trozo de la función a la izquierda de $h$, comprobando que para todo par de valores consecutivos $h'$ y $h'-1$, se cumple $f(h'-1) \geq f(h')$, sabiendo que ambas evaluaciones son mayores o iguales a $f(h)$.

La clave está en analizar qué sucede en los casos posibles de acuerdo a los valores de $c$, $e$ y $m$.
- Si $m > c + e$, entonces solo tiene sentido hacer acciones de quitar y colocar palitos, por lo tanto si $c=e$, el paso de $f(h')$ a $f(h'-1)$ es equivalente ya que para las operaciones necesarias da igual las cantidades que habrían que subir o bajar. Por otro lado, si $c < e$ entonces tiene sentido que al aumentar la cantidad de palitos para quitar con respecto a los que hay que poner, entonces $f(h'-1) \geq f(h')$. Finalmente, en el caso en que $c > e$, entonces la cantidad de palitos para poner aumenta en el paso de $h'$ a $h'-1$ y disminuye la cantidad de los que hay que quitar, pero en dicho paso todavía no se alcanzan las distribuciones para la cantidad de palitos para subir y bajar que corresponden a la solución óptima. Para este último caso, podemos pensar en que las cantidades de palitos a subir y bajar óptimas son $count_{ups_{op}}$ y $count_{downs_{op}}$ y que lo que se logra con el paso de $h'-1$ a $h'$ sería $count_{ups}'$ y $count_{downs}'$. Luego vemos que al aumentar la altura, $count_{ups}'$ aumenta y se acerca más a $count_{ups_{op}}$, y $count_{downs}'$ disminuye y se acerca más a $count_{downs_{op}}$, por lo tanto con el paso dado, se acerca más el costo $c*count_{ups}'+ count_{downs}'*e$ a $c*count_{ups_{op}} + count_{downs_{op}}*e$ de forma lineal, luego podemos afirmar que necesariamente $f(h'-1) \geq f(h')$.

- Si $m \leq c + e$ nótese que podemos reducirlo al caso anterior realizando mientras sea posible las acciones de movimiento, y en este caso la expresión de paso de $h'-1$ a $h'$ podría verse como la cantidad de cada acciones posibles de cada tipo para llegar a la cantidad de acciones posibles para la altura óptima que dan la solución ideal. Nótese que esta expresión para la altura óptima $h$ sería $m*moves_{op} + c*adds_{op} + e*dels_{op}$ donde $moves_{op}, adds_{op}$ y $dels_{op}$ son la cantidad de operaciones de movimiento, colocar y eliminar y que de manera análoga al caso anterior, dichos valores se acercan de forma lineal al valor óptimo a mendida que aumenta la altura en el paso de $h'-1$ a $h'$, por lo tanto debe cumplirse que $f(h'-1) \geq f(h')$.

Finalmente, para completar la demostración se debe hacer el razonamiento equivalente para aquellos valores a la derecha de la altura óptima, con el objetivo de demostrar su monotonía creciente, el cual es análogo al visto anteriormente.

Ahora, una vez demostrado esto, debemos encontrar un algoritmo que nos permita hallar de manera eficiente y precisa el valor de la altura óptima. En la literatura dicho algoritmo se denomina *Búsqueda Ternaria*. Su principio de funcionamiento es similar a la *Búsqueda Binaria*, solo que, en vez de analizar dos secciones de un espacio de búsqueda, se analizan tres, y en base a un criterio análogo permite converger correctamente al valor buscado analizando solamente uno de las tres secciones dadas. Por lo tanto, debemos demostrar que:

#### **Proposición 2.3.2)** La *Búsqueda Ternaria* encuentra correctamente el valor de una función unimodal.

**Demostración:**  

Esta búsqueda tiene la misma idea principal que la **Búsqueda Binaria**, que es la idea de ir examinando valores de la función y “descartando” posiciones candidatas en base a la información obtenida.

Sea $f(x)$ una función unimodal en el intervalo $[a; b]$. Tomamos dos puntos $m1$ y $m2$ en este segmento: $a < m1 < m2 < b$. Entonces, hay tres posibilidades:

- Si $f(m1) < f(m2)$, entonces el máximo requerido no puede ubicarse en el lado izquierdo - $[a; m1]$. Esto significa que el máximo debe buscarse en el intervalo $[m1;b]$.
- Si $f(m1) > f(m2)$, de manera similar al anterior caso. Ahora, el máximo requerido no puede estar en el lado derecho - $[m2; b]$, así que debe buscarse en el segmento $[a; m2]$.
- Si $f(m1) = f(m2)$, entonces la búsqueda debe realizarse e $[m1; m2]$, pero este caso se puede atribuir a cualquiera de los dos anteriores (para simplificar el código). Tarde o temprano, la longitud del segmento será un poco menor que una constante predeterminada, y el proceso podrá detenerse.

En cada paso, tendremos entonces dos extremos $a$
y $b$, y lo que sabemos en todo momento es que el mínimo que estamos buscando está dentro de este intervalo. Es decir, una posición con el valor mínimo que buscamos se encuentra seguro en $[a,b)$. Al final, cuando tengamos $b=a+1$, es decir, cuando tengamos un intervalo de longitud $1$, habremos localizado el mínimo.

La gran diferencia está en que la **Búsqueda Binaria** en cada paso examina la situación en la posición central, separando todo el intervalo que estamos analizando en dos partes. La **Búsqueda Ternaria**, como sugiere su nombre, separa el intervalo en tres partes, y para ello examina el valor de la función en los dos puntos de división entre las partes. Es decir, vamos a examinar dos posiciones dentro de nuestro intervalo, $m1$ y $m2$, con $a≤m1<m2<b$.

Si $f(m1)≤f(m2)$, sabemos que necesariamente $m2$ ya pasó la primera parte inicial, en la que la función decrece estrictamente: si no fuera así, la función decrecería siempre estrictamente entre $m1$ y $m2$, y sería imposible observar lo que estamos observando. Por lo tanto, como el valor mínimo que buscamos se puede encontrar siempre en el último punto de la parte decreciente, y este está más a la izquierda que $m2$, asignaremos $b=m2$. Observemos que no podemos asignar $b$ a nada más pequeño con seguridad: podría ser que el mínimo estuviera de hecho en $m2−1$, y que la razón por la que vemos que $f(m1)<f(m2)$ fuera que la función tenga un aumento enorme entre $m2−1$ y $m2$, que supere todo lo que venía bajando desde $m1$ hasta $m2−1$.

Si $f(m1)>f(m2)$, con un razonamiento análogo podemos deducir que m1 está todavía estrictamente dentro de la primera parte, en la que la función está decreciendo estrictamente (pues sino, la función nunca decrecería entre $m1$ y $m2$), y entonces podemos poner $a=m1+1$, ya que el mínimo tiene que estar sí o sí más a la derecha que $m1$. No podemos poner a en nada más grande, ya que podría pasar que el máximo esté en efecto en $m1+1$: por ejemplo, eso ocurriría si la razón por la que es $f(m1)>f(m2)$ fuera que la función tiene un enorme decrecimiento entre $m1$ y $m1+1$, que compense lo que luego sube desde $m1+1$ hasta $m2$.

Para elegir $m1$ y $m2$, partimos al intervalo $[a,b)$ en tres, tomando: $m1=a+⌊b−a3⌋$, $m2=a+⌊2(b−a)3⌋.$ Si $b−a>1$, estos dos valores $m1$ y $m2$ son siempre distintos entre sí, y caen dentro del rango $[a,b)$. Además, estando $m1$ y $m2$ dentro del rango, los reemplazos $a=m1+1$ y $b=m2$ siempre achican el rango, así que el procedimiento va a llegar en algún momento a tener un rango de un único elemento, que será el mínimo. 

Por lo tanto, de esta forma tenemos demostrada la proposición.

**Idea general de solución:** 
Para solucionar el problema, ahora solo será necesario buscar la altura óptima utilizando el algoritmo de *Búsqueda Ternaria*, luego durante la ejecución de la **Búsqueda Ternaria** se ejecuta la solución con el método $solve(...)$ con la mejor complejidad encontrada hasta el momento y se procede a calcular el mínimo número de operaciones para las dos alturas que dividen cada instancia del espacio de búsqueda en tres secciones de igual tamaño. Finalmente, se retorna el mínimo valor al que converja la función unimodal $f(h) = r$ definida anteriormente.

**Pseudocódigo:**
```
greedy2_ts(n: int, hi: list[int], c: int, e, m) -> int:

    min_h = min(hi)
    max_h = max(hi)
    answer = math.inf
    
    answer = ts_solve(min_h, max_h, n, hi, c, e, m)

    return answer

ts_solve(h1, h2, n, hi, c, e, m):
    if h1 == h2:
        return solve(n, hi, c, e, m, h1)
    
    elif h2 - h1 == 1:
        result_h1 = solve(n, hi, c, e, m, h1)
        result_h2 = solve(n, hi, c, e, m, h2)
        answer = min(result_h1, result_h2)
        return answer
    
    mid1 = h1 + (h2 - h1) // 3
    mid2 = h2 - (h2 - h1) // 3

    result_mid1 = solve(n, hi, c, e, m, mid1)
    result_mid2 = solve(n, hi, c, e, m, mid2)

    if result_mid1 == result_mid2:
        return ts_solve(mid1, mid2-1, n, hi, c, e, m)

    elif result_mid1 < result_mid2:
        return ts_solve(h1, mid2-1, n, hi, c, e, m)
    
    else:
        return ts_solve(mid1+1, h2, n, hi, c, e, m)
```
El algoritmo está implementado en [greedy2_ts.py]().

**Complejidad temporal:**
La variación principal de este algoritmo radica en que la complejidad temporal de la búsqueda de la altura 
óptima y su costo mínimo correspondiente se basa en una **Búsqueda Ternaria** con la modificación de que el factor no recursivo de su función $T(n)$ de complejidad temporal ahora es lineal y no constante como en su versión clásica, ya que dicho factor es el producto de ejecutar el método $solve(...)$ en $\Omicron(n)$. Finalmente, se tiene que $T(m) = T(\frac{2m}{3}) + n$ ya que en cada instancia no base de la *Búsqueda Ternaria*, se realiza un llamado recursivo sobre una sección con tamaño igual a $\frac{2}{3}$ del tamaño del problema en el llamado actual. Por lo tanto, si aplicamos el **Teorema Maestro** vemos que $T(n) \in \Omicron(n\log{m})$, por lo que esta misma sería la complejidad total del algoritmo.  

### **2.4) Solución óptima para cuando $m >> n$:**
En las soluciones anteriores no hemos tenido en cuenta qué relación puede haber entre el tamaño del espacio de búsqueda de la altura óptima y el tamaño del array $hi$. Es decir, nuestras ideas son independientes a si $m$ es mayor o menor que $n$. Por lo tanto, nuestro objetivo consiste en separar el problema en los casos en que $n \geq m$ y $n < m$. Intuitivamente, para lograr una mejora con respecto al segundo caso ($n < m$) necesitaríamos hacer que la complejidad temporal total sea menor que $\Omicron{(n\log{m})}$, lo cual solo se lograría si pudieramos expresar dicha complejidad en función de términos o factores menores que $\Omicron{(n\log{m})}$, es decir, lograr que la nueva complejidad tenga la forma $\sum{t_i}$ donde $t_i < n\log{m}$.

Para lograr llevar a cabo la idea anterior sería necesario encontrar una manera de ejecutar el método $solve(...)$ en algo mejor que $\Omicron{(n)}$, ya que de esta forma pudiésemos mejorar el factor lineal por el cual se multiplica el valor $\log{m}$ en la complejidad de nuestra mejor solución hasta el momento.

A partir de las experiencias de la solución $greedy$ #1 sobre ordenar el array $hi$, nos surge la idea de analizar si es posible convertir a este en una lista de valores que cumplan una propiedad monotónica para poder ejecutar $solve(...)$ en un orden infralineal o logarítmico. Primeramente, es necesario notar que no podemos obtener los valores de $count_{ups}$ y $count_{downs}$ en algo mejor que un orden lineal aunque los valores originales de $hi$ estén ordenados, ya que no existe forma de para una posición en el mismo y una altura pivote $k$ prefijada, determinar la cantidad de unidades de palitos en que cada columna a la izquierda de esta que deben "rellenarse" y análogamente a la derecha para las que deben quitarse, esto debido a que sería necesario calcular recorriendo por cada una de las alturas de las columnas en $hi_i$ e ir realizando las mismas comprobaciones planteadas cuando calculábamos $count_{ups}$ y $count_{downs}$ en $greedy$ #2.

La pregunta principal ahora sería: ¿De qué forma pudiéramos resumir para una columna en $hi$ y una altura $k$ de pivote, cuántas unidades a la izquierda necesitan "rellenarse" para igualar todas las alturas de estas columnas a $k$ y cómo pudiésemos determinar lo mismo para aquellas a la derecha? Es entonces que surge la idea de probar con el array de sumas acumuladas del array $hi$ ordenado, al cual denotaremos como $hi_{sum}$. Este presenta como propiedad fundamental, la capacidad de conocer la respuesta a la pregunta anterior con un costo constante ($\Omicron{(1)}$), ya que para la posición $i$ en $sum_{hi}$, se tiene la suma acumulada de todas las columnas con alturas menores o iguales a $hi_i$ y, si tenemos una altura pivote $k$ y se cumpliera a su vez que $hi_i \geq k$ para el primer índice $i$ (indexando en $0$) para el cual se cumple dicha relación, entonces no es difícil notar que $k*i - sum_{hi}[i-1] = counts_{ups}$. Esta última relación es cierta ya que si todas las $i-1$ alturas a la izquierda estuvieran igualadas a $k$, entonces su suma acumulada sería $k*(i-1)$, luego si tenemos la suma actual $sum_{hi}[i-1]$ para dichas $i-1$ columnas, entonces $k*(i-1) - sum_{hi}[i]$ expresa la cantidad de unidades de palitos de la distribución actual de alturas que son necesarias para igualarlas a la altura pivote usando operaciones de aumento de altura, lo cual es exactamente equivalente a $counts_{ups}$. Es evidente también que a la derecha de dicha altura $hi_i$, todas las alturas a la derecha son mayores o iguales a $k$ prefijada, luego por un razonamiento análogo al caso anterior para aquellas que quedan a la izquierda, podemos ver que $count_{downs} = (sum_{hi}[n-1] - sum_{hi}[i-1]) - k*(n-1)$, ya que $k*(n-i)$ es la suma acumulada en el caso de que las columnas desde $i$ hasta $n-1$ tuvieran todas altura $k$ y $(sum_{hi}[n-1] - sum_{hi}[i-1])$ es el acumulado de las alturas a la derecha de la posición $i$ (incluyéndola), las cuales son mayores o iguales que la altura pivote $k$.

Ya mencionamos que la propiedad anterior se basa en el principio de lograr encontrar aquella posición $i$ lo más a la izquierda posible tal que cumpla que $hi_i \geq k$. Esto con el objetivo de asegurar que las columnas a la izquierda de la posición $i$ en el array $hi$ ordenado cumplan que su altura es menor que $k$ y las que esten a partir de $i$ son mayores o iguales que $k$, lo que asegura la correctitud de la idea anterior. Ahora, la cuestión es cómo encontrar en un orden mejor que algo lineal dicho elemento con las condiciones planteadas. Debemos notar que ahora los valores del array tienen un comportamiento monótono. Luego, para encontrar la primera posición donde hay una columna con altura mayor o igual a una altura pivote $k$, vemos que es posible utilizar la **Búsqueda Binaria**, esto dado que podemos recursivamente para cada porción del array de sumas, analizar si el valor del medio es el valor que estamos buscando con la propiedad anteriormente mencionada, y si es mayor convergemos a la izquierda, mientras que si es menor lo hacemos a la derecha. Finalmente, bajo este principio logramos converger correctamente a la posición deseada. 

**Idea general de solución:** 
Ahora la idea general de esta vía consiste en primeramente ordenar al array $hi$, luego se calcula el array de sumas acumuladas anteriormente descrito y se procede a comprobar por las alturas posibles empleando una **Búsqueda Ternaria** modificada. Esta **Búsqueda Ternaria** solo se diferencia con la del algoritmo anterior en el componente no recursivo de la expresión $T(n)$ general, donde en este caso serían un procedimiento en orden logarítmico utilizando la **Búsqueda Binaria** con el array de sumas acumuladas. Finalmente, se devuelve el costo mínimo para la altura óptima encontradas.

**Pseudocódigo:**
```
greedy_bs_ts(n: int, hi: list[int], c: int, e, m) -> int:
    min_h = min(hi)
    max_h = max(hi)
    answer = math.inf
    hi.sort() # sort the heights
    hi_sum = get_sum_array(hi)

    answer = ts_solve(min_h, max_h, n, hi_sum, c, e, m)

    return answer

ts_solve(h1, h2, n, hi_sum, c, e, m):
    if h1 == h2:
        return solve(0, n-1, n, hi_sum, c, e, m, h1)
    
    elif h2 - h1 == 1:
        result_h1 = solve_bs(0, n-1, n, hi_sum, c, e, m, h1)
        result_h2 = solve_bs(0, n-1, n, hi_sum, c, e, m, h2)
        answer = min(result_h1, result_h2)
        return answer
    
    mid1 = h1 + (h2 - h1) // 3
    mid2 = h2 - (h2 - h1) // 3

    result_mid1 = solve(0, n-1, n, hi_sum, c, e, m, mid1)
    result_mid2 = solve(0, n-1, n, hi_sum, c, e, m, mid2)

    if result_mid1 == result_mid2:
        return ts_solve(mid1, mid2-1, n, hi_sum, c, e, m)

    elif result_mid1 < result_mid2:
        return ts_solve(h1, mid2-1, n, hi_sum, c, e, m)
    
    else:
        return ts_solve(mid1+1, h2, n, hi_sum, c, e, m)

solve_bs(a, b, n, hi_sum, c, e, m, height):
    if a==b:
        count_ups = (a)*height - (hi_sum[a-1]) if a > 0 else 0
        count_downs = (hi_sum[n-1] - hi_sum[a-1]) - (n-a)*height if a > 0 else  hi_sum[n-1] - (n-a)*height
        result = 0

        if count_ups == count_downs and m <= c + e:
            result = count_ups*m

        elif count_ups < count_downs and m <= c + e:
            result = count_ups*m + (count_downs - count_ups)*e

        elif count_ups > count_downs and m <= c + e:
            result = count_downs*m + (count_ups - count_downs)*c

        else:
            result = count_ups*c + count_downs*e

        return result

    mid = int((a+b)/2)
    current_height = hi_sum[mid] - hi_sum[mid-1] if mid > 0 else hi_sum[mid]

    if current_height < height:
        return solve(mid + 1, b, n, hi_sum, c, e, m, height)
    
    else:
        return solve(a, mid, n, hi_sum, c, e, m, height)

```
El algoritmo está implementado en [greedy_bs_ts.py](). 

**Complejidad temporal:**
La ordenación del array $hi$ es en $\Omicron{(n\log{n})}$, luego el proceso de hallar el array de sumas acumuladas se puede hacer en $\Omicron{(n)}$. Luego, tal y como se muestra en el código, el método $solve\_ts$ es idéntico al de la solución anterior, variando solamente el método $solve$ por $solve\_bs(...)$, el cual consiste en una **Búsqueda Binaria**, la cual por conferencias conocemos que es en $\Omicron{(\log{n})}$. Por lo tanto, el método $solve\_ts(...)$ correspondiente a la **Búsqueda Ternaria** tiene complejidad temporal $T(m) = T(\frac{2m}{3}) + \log{n}$ y por **Teorema Maestro** $T(n) \in \Omicron{(\log{n}\log{m})}$. Finalmente, el algoritmo general tiene complejidad temporal $\Omicron{(n\log{n} + \log{n}\log{m})}$, lo cual para $m > n$ cumple que es mejor que $O(n\log{m})$ dado que es posible hallar una constante $c > 0$ tal que para $m,n$ naturales y con $m > n$, ya que puede determinar que $c*n\log{m} \geq n\log{n} + \log{n}\log{m}$, luego vemos que para $c \geq 2$ es posible que se cumpla dicha relación, o de forma más general, si se tiene que hallar un $c$ tal que $c*n\log{m} \geq a*n\log{n} + b*\log{n}\log{m}$, se podría lograr la misma relación haciendo $c \geq a + b$. Por lo tanto, tenemos que la complejidad del algoritmo planteado es mejor cuando $m > n$, en esencia poque $n\log{n}$ y $\log{n}\log{m}$ "pierden" (son menores) con $n\log{m}$ para $n$ y $m$ suficientemente grandes con $m > n$.

### **2.5) Solución óptima generalizada:**
La solución óptima generalizada consisten en verificar inicialmente si $m > n$ entonces se procede a ejecutar el método de la sección $2.4)$, y en caso contrario se ejecuta el de la sección $2.3)$ por lo tanto para este caso la complejidad temporal de la solución general sería equivalente a $\Omicron{(min(n\log{m}, n\log{n} + \log{n}\log{m})})$.

**Peudocódigo:**
```
gbt_or_g2t(n, hi, c, e, m):
    min_hi = min(hi)
    max_hi = max(hi)
    k = max_hi - min_hi

    if n < k: # O(nlogn + logk*logn)
        return greedy_bs_ts(n, hi, c, e, m)
    
    # O(nlogk)
    return greedy2_ts(n, hi, c, e, m)
```

El algoritmo está implementado en [gbt_or_g2t.py]().

**Complejidad temporal:**
Ahora, debido a la propuesta anterior, debemos notar que el algoritmo es en general $\Omicron{(min(n\log{m}, n\log{n} + \log{n}\log{m}))}$ dado que tiene complejidad $\Omicron(n\log{m})$ o $\Omicron(n\log{n} + \log{n}\log{m})$ en caso de que $n \geq m$ o $m > n$ respectivamente.

## **3) Implementación del proyecto:**
El proyecto está dividido en tres secciones principales: Soluciones, Informe y Pruebas. Todas las implementaciones fueron realizadas con el lenguaje de programación $Python$. El punto de entrada para la ejecución del proyecto es el archivo $main.py$ en el directorio principal. Desde este se pueden ejecutar los scripts en las carpetas de *Soluciones* y *Pruebas* importando el archivo y los métodos específicos que se deseen ejecutar.

Para ejecutar el proyecto sólo es necesario ejecutar el archivo $main.py$ el cual por defecto tiene la implementación para hallar la solución de una instancia del problema. Una vez ejecutamos este script se requiere entrar un valor $n$ entero que represente el número de columnas $hi$, luego en la siguiente línea se deben escribir $n$ valores correspondientes a las alturas de las columnas de $hi$, luego en las siguientes tres líneas se procede a entrar los valores de costo $c, e$ y $m$. Finalmente al presionar $enter$ de devuelve la respuesta al problema: el costo mínimo de llevar todas las columnas a una misma altura utilizando las operaciones predefinidas. A continuación se muestra un ejemplo de flujo de entrada y salida por consola:
```
Input:
6
7 11 8 2 10 4
2
3
3
```
```
Output:
24
```

- **Soluciones:**
En esta carpeta se encuentran las distintas soluciones probadas para resolver el problema planteado. Todas contienen en esencia un método principal que recibe una entrada en el formato $n, hi, c, e, m$ donde $n$ es la cantidad de columnas, $hi$ es el array de tamaño $n$ de las alturas de las columnas de palitos y $c, e$ y $m$ son los costos de las operaciones de colocar, quitar y mover respectivamente. Como salida de estos métodos principales se da un entero que representa el costo mínimo de igualar todas las alturas de las columnas en $hi$ con las operaciones predefinidas.

- **Informe:** Constituye el resumen de los experimentos llevados a cabo en el proyecto y contiene las demostraciones que prueban la correctitud de los mismos.

- **Pruebas:** Contiene el script [plotter.py](), el cual fue utilizado para comprobar la propiedad fundamental que justifica el funcionamiento de la solución $2.3)$ (se debe tener instalado $matplotlib$) y el script [algos_output_tester.py](), el cual genera casos de prueba aleatorios y compara las salidas de las soluciones implementadas y comprueba la igualdad en la salida de estas para mostrar su equivalencia. También se incluyó el archivo [tester.py]() que contiene la función *test_solution(...)* que recibe de entrada una función que resuelve el problema y se desea evaluar y luego se comparan las respuestas de esta con las del método de solución *greedy2(...)* y finalmente se da como retorno "Accepted!!" si coincidieron todas las respuestas y "Wrong Answer!!" en caso contrario. 
