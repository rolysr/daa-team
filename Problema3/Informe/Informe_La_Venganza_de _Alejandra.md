# Informe sobre solución al problema: La Venganza de Alejandra
## Equipo: $D^{aa}$
## Integrantes:
 - Andry Rosquet Rodríguez - C411
 - Rolando Sánchez Ramos - C411

## **1) Introducción al problema:**
En el archivo [La Venganza de Alejandra]() nos definen un problema donde se tiene un grafo, no dirigido, con aristas simples consideradas las relaciones entre los compañeros de Alejandra. El número de nodos y aristas del grafo serán denotados por $n$ y $m$ respectivamente en el resto del documento.

La solución del problema consiste en determinar si es posible eliminar aristas del grafo, de forma tal que el grafo resultante tenga a todos sus nodos con grado 3 ó 0, exceptuando el caso en que sea necesario eliminar todas las aristas del grafo para alcanzar tal condición. Lo anterior se traduce en que cada compañero de Alejandra termine com 3 o ninguna amistad.

Por último, es importante mencionar que tanto nodos como aristas serán enumerados indexando en $0$. Es decir, el primer nodo del grafo es el $0$ y no el $1$, lo cual no influye en ningún momento en la complejidad de las soluciones planteadas.
## **2) Soluciones:**
El desarrollo de la mejor solución encontrada al problema se expone de manera iterativa, es decir, inicialmente se demostrará la correctitud de una solución intuitiva, la cual se irá mejorando a medida que probemos una serie de proposiciones que nos permitirán optimizar la complejidad temporal de cada algoritmo implementado.

### **2.1) Solución Fuerza Bruta Recursividad:**
Se desea determinar si entre todas las variantes de escoger o no cierta arista, extendiendo la desición a cada una de las pertenecientes al grafo, hay al menos una que haga cumplir con las condiciones del problema. O sea, se procederá generando el árbol de posibilidades que se nos otorga al poder quitar o dejar cierta arista. Para luego, con cada posibilidad analizarl si válida para solucionar el problema. 

**Idea general de solución:**

El método $brute\_force\_recursive$ será el encargado de controlar los casos esquinados como pueden llegar a ser:
1. El grafo inicial no tiene aristas.
2. Si dejando todas las aristas del grafo inicial, ya este es váido para la solución.

Además crea el array $bitmask$, en este, al valor $True$ se le corresponde la acción de dejar la arista en el grafo y $False$ removerla.
Luego, sino se encuentra en un caso esquinado, procederá a ejecutar $brute\_force\_recursion$. Este método recursivo tendrá como condición de parada haber iterado las $m$ aristas, esto gracias a la variable que el controla llamada arist. Cuando alcanza la condición de parada, significa que ya se tomó la desición de remover o dejar cada arista y por tanto, es válido analizar si esta variación es válida. Si quedan aristas por decidir entonces, realiza los dos llamados recursivos posibles:
1. Dejar la arista y entonces se aumenta la variable arist en 1 para avanzar a la siguiente, si falta alguna por analizar.
2. Otorgarle a $bitmask$ en la posición de la arista que se está analizando el valor $False$ y aumentar en 1 arist. Entonces esta arista en el llamado recursivo ha sido removida.
Luego se deshacen los cambios para futuras combinaciones debido a que Python trabaja la lista $bistmask$ con referencia. Notar que se recorrerán todas las posibilidades, puesto que no existen más variantes que dejar o remover las aristas y la recursividad se encarga de conformar todas las variantes posibles.
El método, ya mencionado en par de ocasiones, encargado de comprobar la validez de la combinación de aristas es $is\_valid\_graph$. Este, intuitivamente iterará por cada arista del grafo y en un array llamado $degree\_vertex$ recogerá la información de los grados de cada nodo. Por cada arista, accede a los nodos que la conforman, para luego aumentar el grado de ambos en 1. El algoritmo irá controlando si algún nodo sobrepasa el grado 3, en dicho caso devolverá falso. Finalmente itera por el array $degree\_vertex$, donde analiza si los grados de cada nodo son 0 ó 3, únicamente. Además controla el caso esquinado donde todas las aristas hallan sido removidas, en dicho caso devuelve falso ya que incumple la condición de no eliminar todas las relaciones de amistad.

**Pseudocódigo:**
```
brute_force_recursive(n, m, edges):
    bitmask = [True for i in range(m)]
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True
    else:
        return brute_force_recursion(n, m, edges, bitmask, 0)

brute_force_recursion(n, m, edges, bitmask, arist):
    if arist == m:
        return is_valid_graph(n, m, edges, bitmask)
    
    arist+=1
    if brute_force_recursion(n, m, edges, bitmask, arist):
        return True
    bitmask[arist-1]=False
    if brute_force_recursion(n, m, edges, bitmask, arist):
        return True
    bitmask[arist-1]=True
    
    return False

is_valid_graph(n, m, edges, bitmask):
    degree_vertex = [0 for i in range(n)]

    for i in range(m):
        if bitmask[i]:
            a, b = edges[i]
            degree_vertex[a] += 1
            degree_vertex[b] += 1
            if degree_vertex[a] > 3 or degree_vertex[b] > 3:
                return False
    count=0   
    for degree in degree_vertex:
        if degree != 3 and degree != 0:
            return False
    for bit in bitmask:
        if not bit:
            count+=1
    if count == m:
        return False
    return True      
```
**Complejidad Temporal:**
Nos encontramos en presencia de un algoritmo recursivo que internamente llama el método de validación de la slución cada vez que alcanza la condición de parada. La complejidad de la recursividad resulta simple de determinar en este caso; notemos que se llamará a sí misma a lo sumo 2 veces y además se adentrará hasta que $arist$ alcance el valor de m. Por tanto, como $arist$ aumenta en 1 unidad con cada llamado podemos concluir que la complejidad de la recursividad, sin tener en cuenta los llamados al método de validación, será $O(2^m)$. Ahora, al considerar los llamados a $is\_valid\_graph$ vemos que la complejidad final será $O((m+2n)*2^m)$. Esto se debe a que el método anterior hace primero un recorrido por las $m$ aristas y luego dos ciclos por el array $degrees\_vertex$ con tamaño $n$. Finalmente la complejidad se puede reducir a solo $O(2^m)$, ya que se puede despreciar la parte polinomial.

### **2.2) Solución Fuerza Bruta con Máscara de Bits:**
Al igual que en el algoritmo anterior se desea iterar por cada posibilidad que nos otorga el remover o dejar una arista. Para luego, concluir si hay al menos una variante válida.

**Idea general de solución:**

El método $brute\_force\_bitmask$ iterará por las $2^m$ posibilidades que de manera intuitiva nos brinda el poder dejar o remover una arista del grafo. Lo anterior, lo hará usando como recurso máscaras de bits. El ciclo desde 1 a $2^m$ nos brinda la posibilidad de recorrer todos los números binarios con longitud $\leq$ m. Luego notemos que si elevamos $2^i$, con 0 $\leq$ i $\leq$ m, en binario estos números constituirán máscaras donde todos sus dígitos son 0 exceptuando la posición $i$.
Entonces con estas herramientas y con el uso de la operación Y Lógica(&) entre el número del ciclo exterior y las máscaras del ciclo interno, es que iremos ubicando $True$ o $False$ en la lista $bitmask$ que constituye la variación que se debe verificar.
Notar que se recorren todas las variaciones gracias a que como se explicó el ciclo externo estará constituido por todos los números desde 1 a hasta $2^m$, los cuales en binario son todas las variantes de ubicar 1s y 0s en $m$ casillas.

**Pseudocódigo:**
```
brute_force_bitmask(n, m, edges):
    bitmask = [True for i in range(m)]
    
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True
    
    for i in range(1, 2**m):
        for j in range(m):
            bitmask[j] = True if i & (2**j) else False
        if is_valid_graph(n, m, edges, bitmask):
            return True

    return False

is_valid_graph(n, m, edges, bitmask):
    degree_vertex = [0 for i in range(n)]

    for i in range(m):
        if bitmask[i]:
            a, b = edges[i]
            degree_vertex[a] += 1
            degree_vertex[b] += 1
            if degree_vertex[a] > 3 or degree_vertex[b] > 3:
                return False
    count=0   
    for degree in degree_vertex:
        if degree != 3 and degree != 0:
            return False
    for bit in bitmask:
        if not bit:
            count+=1
    if count == m:
        return False
    return True      
```

**Complejidad Temporal:**
La complejidad temporal de este algoritmo viene dada por el ciclo con $2^m$ iteraciones y dentro de cada una de estas iteraciones se lleva a cabo otro ciclo, este de longitud m, y un llamado a la función $is\_valid\_graph$ de la cual ya conocemos su complejidad (véase complejidad de solución fuerza bruta con recursividad $O(2n+m)$). Por tanto, el algoritmo tiene como complejidad temporal $O((2n+2m)*2^m)$, la cual es equivalente a $O(2^m)$.

### **2.3) Solución utilizando metaheurística:**
Una vez analizadas las soluciones anteriores, es posible notar una interesante aproximación en base a la distancia de soluciones parciales con respecto a una solución admisible para el problema en cuestión.

**Idea general de solución:** 


**Pseudocódigo:**
```
```

**Complejidad Temporal:**


### **2.4) Demostración de la NP-completitud del problema:**

**Nociones básicas:**

En teoría de la complejidad computacional, la clase de complejidad NP-completo es el subconjunto de los problemas de decisión en NP tal que todo problema en NP se puede reducir en cada uno de los problemas de NP-completo. Se puede decir que los problemas de NP-completo son los problemas más difíciles de NP y muy probablemente no formen parte de la clase de complejidad P. La razón es que de tenerse una solución polinómica para un problema NP-completo, todos los problemas de NP tendrían también una solución en tiempo polinómico. Si se demostrase que un problema NP-completo, llamémoslo A, no se pudiese resolver en tiempo polinómico, el resto de los problemas NP-completos tampoco se podrían resolver en tiempo polinómico. Esto se debe a que si uno de los problemas NP-completos distintos de A, digamos X, se pudiese resolver en tiempo polinómico, entonces A se podría resolver en tiempo polinómico, por definición de NP-completo. Ahora, pueden existir problemas en NP y que no sean NP-completos para los cuales exista solución polinómica, aun no existiendo solución para A.

Por ejemplo para el caso específico de nuestro problema, dado un grafo $G$, si se tiene un subgrafo del mismo, es fácil corroborar que este cumple con las condiciones establecidas en el problema.

*Grafos Cúbicos:*

El problema en particular que tratamos puede ser reducido al hecho de encontrar un subgrafo regular de grado $3$ de un grafo arbitrario dado como entrada. Vemos que esto es equivalente a lo que se pide en nuestro problema pues si encontramos tal subgrafo, este tendría una cantidad de aristas menor o igual a la del grafo inicial, con lo cual se pudiese inferir que el proceso de quitar aristas hasta que todo nodo cumpla que, o tiene grado $3$ o tiene grado $0$. Dichos subgrafos son conocidos como grafos cúbicos.

En teoría de grafos, un grafo cúbico o grafo trivalente es un grafo cuyos vértices son todos incidentes a exactamente tres aristas. En otras palabras, un grafo cúbico es un grafo 3-regular.

*Problema NP-Completo:*

Nuestro problema es un problema de desición, ya que su respuesta se basa en afirmar o negar una sentencia, en este caso, si para un grafo dado, existe una reducción de aristas, de no todas a la vez, tal que el grafo resultante cumpla que cada nodo tiene grado 3 o 0. Ahora, un problema de decisión C es NP-completo si:

1. C es un problema NP
2. Todo problema de NP se puede transformar polinómicamente en C.

Se puede demostrar que C es NP demostrando que un candidato a solución de C puede ser verificado en tiempo polinómico.

Una transformación polinómica de L en C es un algoritmo determinista que transforma instancias de l ∈ L en instancias de c ∈ C, tales que la respuesta a c es positiva si y sólo si la respuesta a l lo es.

Como consecuencia de esta definición, de tenerse un algoritmo en P para C, se tendría una solución en P para todos los problemas de NP.

Es entonces en base a dichas ideas, que probaremos la NP-completitud de nuestro problema a partir de la demostración del siguiente teorema:


**Teorema 2.4.1)** El problema de encontrar un subgrafo k-regular para un grafo $G$ es NP-completo para $k \geq 3$. (Problema k-R)

**Demostración:** El problema planteado es NP, esto, dado que es posible en tiempo polinomial determinar si una solución referente a una instancia del mismo es correcta, es decir, para un subgrafo dado como respuesta, es posible determinar si el mismo cumple que todo nodo tiene grado $k$ simplemente recorriendo el conjunto de las aristas de este y aumentando en uno el grado de los nodos conectados en la misma.

Es conocido que el problema de determinar si un grafo es 3-coloreable (problema 3-C) es NP-completo, ya que dicha condición fue demostrada por [Karp](https://link.springer.com/chapter/10.1007/978-1-4684-2001-2_9) en 1972. Luego, teniendo esto en cuenta, el objetivo será reducir el problema 3-C al problema k-R. Además, denotemos por $K_k'$ el grafo completo con $k$ vértices con una arista faltante.

Dado un grafo arbritrario $G$ como entrada al problema 3-C, con $V(G) = \{v_1, v_2, \cdots, v_n\}$ y $E(G) = \{e_1, e_2, cdots, e_m\}$, podemos construir un nuevo grafo $G'$ de la siguiente manera:

1. Para cada nodo $v_i$ en $G$, construyamos $3$ ciclos $C_i^1, C_i^2, C_i^3$ en $G'$, cada uno con longitud $2d(v_i) + 1$. Ahora, denotemos los vértices en $C_i^h$ como $c_{ij}^h$, con $1 \leq i \leq n, 1 \leq j \leq 2d(v_i) + 1$ y $1 \leq h \leq 3$.

2. Para cada arista $e_j$, con $1 \leq j \leq m$, construyamos $3(k-2)$ subgrafos correspondientes denotados como $D_{jp}^h$ en $G'$, con $1 \leq p \leq k-1, 1 \leq h \leq 3$, donde cada $D_{jp}^h$ es un grafo $K_{k+1}'$. Además, denotemos los dos vértices con grado $k-1$ en $D_{jp}^h$ como $x_{jp}^h$ e $y_{jp}^h$.

3. Sea la arista $e_j$ incidente sobre los vértices $v_s$ y $v_t$ en $G$. Para cada $h$, $1 \leq h \leq 3$, sean $c_{s\alpha}^h$ y $c_{s\beta}^h$ ($c_{t\gamma}^h$ y $c_{t\delta}$) dos vértices en $C_s^h$ ($C_t^h$) tales que $c_{s\alpha}^h$ y $c_{s\beta}^h$ ($c_{t\gamma}^h$ y $c_{t\delta}$) tengan grado dos. Para $1 \leq p \leq 3(k-2)$, agreguemos las aristas $(c_{s\alpha}^h, x_{jp}^h), (c_{s\beta}^h, y_{jp}^h), (c_{t\gamma}^h, x_{jp}^h)$ y $(c_{t\delta}^h, y_{jp}^h)$ al conjunto de aristas $E(G')$.
Una vez que todas las aristas en $G$ hayan sido consideradas en el paso $3.$, cada cilco $C_i^h$ ($1 \leq i \leq n, 1 \leq h \leq 3$) contendrá exactamente un vértice de grado dos. Nombremos estos vértices como $w_i^h$, con $1 \leq i \leq n, 1 \leq h \leq 3$.

4. Para $1 \leq i \leq n$, sea $U_i$ un subgrafo formado como: $U_i$ contiene $(k-2)$ veces el grafo K_{k+1}' y $(k-2)$ otros vértices. Denotemos estos otros vértices como $u_{ij}$, y los vértices en $K_{k+1}'$ con grado $k-1$, $x_{ij}$ e $y_{ij}$ con $1 \leq j \leq k-2$. Luego, unamos los vértices $u_{ij}$ con los grafos $K_{k+1}'$ añadiendo las aristas $(u_{ij}, x_{ij})$. Luego, añadimos los subgrafos $U_1, U_2, \cdots, U_n$ y las aristas $(u_{ij}, w_i^1), (y_{ij}, w_i^2)$ y $(y_{ij}, w_i^3)$  a $G'$. Esto lo hacemos para cada $i$ y $j$, con $1 \leq i \leq n, 1 \leq j \leq k-2$.

5. Finalmente, añadimos un ciclo $C'$ de longitud $(k-1)n$ a $G´$; este ciclo es sobre los nuevos vértices $a_{11}, a_{12}, \cdots, a_{1n}, a_{21}, \cdots, a_{(k-1)n}$. Para $1 \leq i \leq n, 1 \leq j \leq k-2$ y $1 \leq p \leq k-1$, añadimos las aristas $(a_{pi}, u_{ij})$ a $G'$.

Es evidente que la construcción del grafo $G'$ puede ser realizada en tiempo polinomial para cualquier grafo $G$ dado. Ahora, la demostración principal del teorema consiste en probar que: *Un grafo $G$ es 3-coloreable si y solo si el grafo $G'$ construido contiene un subgrafo k-regular.*

($\Rightarrow$) Dado el grafo $G$ y cualquier tripartición de $V(G)$ en subconjuntos $V_1, V_2$ y $V_3$, podemos construir un subgrafo de $G'$, al cual denotaremos por $H$, de la siguiente manera:

1. Todos los vértices $a_{ij}$, $1 \leq i \leq k-1, 1 \leq j \leq n$ están en $V(H)$.
2. Todos los vértices $u_{ij}$, $1 \leq i \leq n, 1 \leq j \leq k-2$ están en $V(H)$.
3. Si $v_i$ de $G$ está en el subconjunto $V_c$, $1 \leq c \leq 3$, entonces el ciclo $C_i^c$ está en $H$. Si el subconjunto $V_c$ no está en $V_1$, entonces se añaden también los vértices en los $k-2$ grafos $K_{k+1}'$ de $U_i$.

4. Si la arista $e_j$, $1 \leq j \leq m$, es adjacente al vértice $v_s$ el cual está en el subconjunto $V_c$, entonces los subgrafos $D_{jp}^c$ adyacentes a $C_s^c$ están en $V(H)$ para $1 \leq p \leq k-2$.
5. El subgrafo $H$ se define como $G'[V(H)]$.

Es trivial comprobar que el subgrafo $H$ contruido existe para cualquier tripartición de $G$. Además, todos los vértices en $H$ tienen grado $k$ excepto posiblemente dichos vértices $x_{jp}^c$ e $y_{jp}^c$ en $D_{jp}^c$ para $1 \leq j \leq m, 1 \leq p \leq k-2$ y $1 \leq c \leq 3$. Por lo tanto, es fácil notar que si la tripartición es una coloración, por ejemplo, $G$ es 3-coloreable, entonces el subgrafo $H$ construido es k-regular.

($\Leftarrow$) Asumamos que $G'$ contiene un subgrafo k-regular $H$, las siguientes propiedades son verdad respecto a $H$:

1. Todos los vértices $a_{ij}$ y $u_{jl}$, $1 \leq i \leq k-1, 1 \leq j \leq n$ y $1 \leq l \leq k-2$ están en $V(H)$. Esto es debido a que el subgrafo $H$ no puede ser k-regular sin la inclusión de un vértice $u_{jl}$, pero la inclusión de uno de dichos vértices obliga a que todos los vértices en $C'$ y otros vértices $u_{jl}$ sean incluidos.
2. Para cada $i$, $1 \leq i \leq n$, exactamente uno del ciclo $C_i^h$, $1 \leq h \leq 3$, está en $V(H)$.
3. Para cada $i$, $1 \leq i \leq n$, si $C_i^h \subseteq H$, entonces $C_j^h \not\subseteq H$ para todo $j$ tal que $(i, j) \in E(G)$. Esto asegura que todos los vértices $x_{jp}^h$ e $y_{jp}^h$, $1 \leq j \leq m$, $1 \leq p \leq k-2, 1 \leq h \leq 3$, tienen grado $3$.

Por la propiedad $2.$, se llega a que el subgrafo $H$ de $G'$ corresponde a una tripartición para los vértices de $G$ tal que un vértice $v_i$ está en una partición $c$ si el ciclo $C_i^c \in H$. La propiedad $3.$ asegura que los vértices adyacentes están en una partición diferente, por lo tanto, esto muestra que la tripartición correspondiente a $H$ es de hecho una coloración de $G$. Por lo tanto, $G$ es 3-coloreable si $G'$ contiene un subgrafo k-regular $H$. De esta forma se completa la demostración.□

Una vez demostrado el teorema anterior, vemos que demostramos también que el problema enfrentado en este proyecto es $NP-completo$, esto dado que si lo reducimos para $k=3$, se cumple por el teorema anterior. Luego, dado ese subgrafo 3-regular que se asegura para un grafo arbitrario en caso de que lo tenga, bastaría con quitar las aristas necesarias para llegar a él como parte de la solución de la situación planteada, donde estará un subgrafo regular y posiblemente, otros nodos con grado $0$, lo cual corresponde con la validez de una solución buscada.
## **3) Implementación del proyecto:**
El proyecto está dividido en tres secciones principales: Soluciones, Informe y Pruebas. Todas las implementaciones fueron realizadas con el lenguaje de programación $Python$. El punto de entrada para la ejecución del proyecto es el archivo $main.py$ en el directorio principal. Desde este se pueden ejecutar los scripts en las carpetas de *Soluciones* y *Pruebas* importando el archivo y los métodos específicos que se deseen ejecutar.

Para ejecutar el proyecto sólo es necesario ejecutar el archivo $main.py$ el cual por defecto tiene la implementación para hallar la solución de una instancia del problema. Una vez ejecutamos este script se debe dar de entrada los valores $n$ y $m$ en una misma línea, denotando las dimensiones del grafo que queremos crear, luego en las siguientes $m$ líneas se deben escribir duplos de la forma $(x, y)$ denotando una arista entre los nodos $x$ e $y$.
A continuación se muestra un ejemplo de flujo de entrada y salida por consola:
```
Input:
6 7
0 1
0 2
0 3
1 2
1 3
2 3
0 4
```
```
Output:
True
```

- **Soluciones:**
En esta carpeta se encuentran las distintas soluciones probadas para resolver el problema planteado. Todas contienen en esencia un método principal que recibe una entrada en el formato $n, m, edges$ donde $n$ y $m$ son la cantidad de nodos y aristas del grafo respectivamente y $edges$ el es conjunto de aristas. Como salida de estos métodos se da un valor booleano que representa la respuesta a la interrogante de si es posible, con el uso o no de la operación de quitar aristas del grafo original dado (no todas a la vez), el grafo resultante cumpla que cada nodo tiene grado $3$ o $0$.

- **Informe:** Constituye el resumen de los experimentos llevados a cabo en el proyecto y contiene las demostraciones que prueban la correctitud de los mismos.

- **Pruebas:** Contiene el script [algos_output_tester.py](), el cual genera casos de prueba aleatorios y compara las salidas de las soluciones implementadas y comprueba la igualdad en la salida de estas para mostrar su equivalencia. También se incluyó el archivo [tester.py]() que contiene la función *test_solution(...)* que recibe de entrada una función que resuelve el problema y se desea evaluar y luego se comparan las respuestas de esta con las del método de solución $brute\_force\_recursive$ y finalmente se da como retorno "Accepted!!" si coincidieron todas las respuestas y "Wrong Answer!!" en caso contrario. 
