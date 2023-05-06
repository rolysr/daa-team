# Informe sobre solución al problema: El Viaje
## Equipo: $D^{aa}$
## Integrantes:
 - Andry Rosquet Rodríguez - C411
 - Rolando Sánchez Ramos - C411

## **1) Introducción al problema:**
En el archivo [El Viaje]() nos definen un problema donde se tiene un grafo conexo, no dirigido, con aristas con costo no negativo ($\geq 0$). Además, en el problema se tiene un grupo $Q$ de tuplas de la forma $(u, v, l)$, las cuales son fundamentales para los caminos y carreteras útiles en el grafo.

En el contexto del problema, un camino útil es un camino entre algún par de nodos $u$ y $v$ presentes en alguna tupla en $Q$ tal que el costo de las aristas de dicho camino sea menor o igual que $l$. Luego, una carretera útil sería una arista perteneciente a dicho camino útil.

La solución del problema consiste en hallar la cantidad carreteras útiles dado el conjunto $Q$, es decir, determinar el número de aristas que perteneces a algún camino de un nodo $u$ a un nodo $v$ con costo menor igual que $l$ para alguna tupla $(u, v, l)$ en $Q$.

Es importante hacer notar que por "camino" nos referimos a cualquier secuencia válida de vértices que puedan recorrerse a partir de aristas que los conecten, es decir, un camino es una secuencia finita de nodos $u_1, u_2, \cdots, u_n$ donde $\forall i \leq n$ se cumple que existe la arista $(u_i, u_{i+1})$ excepto quizás para el último nodo de la secuencia. En otras palabras, los caminos definidos en el problema pueden repetir nodos y aristas.
## **2) Soluciones:**
El desarrollo de la mejor solución encontrada al problema se expone de manera iterativa, es decir, inicialmente se demostrará la correctitud de una solución intuitiva, la cual se irá mejorando a medida que probemos una serie de proposiciones que nos permitirán optimizar la complejidad temporal de cada algoritmo implementado.

### **2.1) Solución Fuerza Bruta:**

Se desea obtener el número de aristas útiles del grafo según las $Q-tuplas$ de la forma $u$, $v$, $l$ donde $u$ será el origen, $v$ el destino y $l$ el costo máximo de los caminos útiles de un nodo al otro.
Para llevar a cabo dicho cálculo; el algoritmo buscará, para una $Q-tupla$ dada, todos los caminos útiles. Finalmente, obteniendo estos caminos tendríamos las aristas útiles, que serán aquellas que forman dichos caminos.
Se desea encontrar los caminos con menor costo que $l$ partiendo de $u$ y llegando a 4v$. El algoritmo entonces se posicionará en el nodo u del grafo y analizará que ocurre si avanza a cada nodo adyacente de $u$. Este procedimiento lo continuará haciendo para cada nodo, asegurando encontrar todos los posibles caminos válidos (formado por aristas consecutivas o retrocediendo en ella misma) del grafo mediante combinaciones de aristas partiendo desde $u$. El algoritmo comprueba en cada paso que al tomar una nueva arista, el costo de esta sumado al camino actual no sobrepase $l$. Por tanto, el algoritmo no es infinito porque este tiene como condición de parada que el costo total de las aristas del camino no exceda a $l$, permitiendo que la cantidad de caminos sea finito. La condición de parada además es la que permite que al no sobrepasar $l$, el camino sea útil en caso de que el nodo final sea $v$.
Como el algoritmo nos proveerá de los caminos útiles, solo resta agrupar las aristas que se encuentran en alguno de estos caminos, obteniendo el conjunto deseado para la q-tupla que se analizó. Si se repite el proceso para cada tupla de $Q$ obtendríamos lo mismo para cada una y por tanto el resultado final es el conjunto deseado. 

**Idea general de solución:**
El método $brute_force$ será el que itere por cada tupla de $Q$ y haga un llamado a $get_useful\_edges$ con la información del grafo y de la tupla que se desea analizar. El método $get\_useful_edges$ hará un llamado de $get\_paths$ esperando obtener todos los caminos útiles para luego solo extraer cada arista de cada camino útil. Por tanto, $get_\paths$ será el encargado de recursivamente recorrer el grafo para analizar todos los posibles caminos y de estos solo guardar en total_paths aquellos que sean útiles. Notar como el algoritmo itera por cada nodo adyacente que tiene el nodo en que se encuentra el final del camino actual, no se excluye alguno que haya sido visitado, ni tampoco de donde viene en el llamado recursivo anterior (nodo adyacente que fue el final provisional del camino antes de visitar el nodo actual).

**Pseudocódigo:**
```

```

### **2.2) Solución con Dijkstra para cada arista y tupla de Q:**

### **2.3) Solución con Dijkstra precalculado y análisis para cada arista y tupla de Q:**
Luego de analizada la solución de la subsección **2.2)**, una idea interesante para mejorarla es realizar los llamados al algoritmo de Dijkstra solamente para los nodos que así lo requieran, en este caso, dado que en la solución anterior se realiza más de una vez el algoritmo de Dijkstra en caso de si un nodo $u$ aparece más de una vez como extremo de alguna tupla del conjunto $Q$, sería más óptimo si estos mismo llamos se precalculan en un array $node\_dist$ el cual sea un array donde en su índice $i$ almacene el valor del Dijkstra calculado para el nodo $i$ si fue necesario y se guarde un valor nulo (*None* en caso de Python) para aquellos para los cuales no fue necesario calcularlo.

Luego, teniendo en cuenta las ideas anteriores, solo es necesario recorrer cada una de las tuplas $Q$ y ejecutar un Dijkstra por cada uno de los nodos $u$ y $v$ que formen parte de estas, y si alguno ya fue calculado, se podrá saber por el contenido en $node\_dist$. Luego se procede a realizar el mismo procedimiento que en el algoritmo de la subsección anterior, donde se analiza para cada tupla en $Q$ y por cada arista en el grafo dado, si esta pertenece a algún camino de $u$ a $v$ con costo menor que $l$, lo cual demostramos anteriormente que denotaremos por carretera útil.

**Idea general de solución:** 
Primeramente, se itera por cada tupla del conjuno $Q$, donde se va rellenando una lista $node\_dist$, la cual contiene para cada índice $i$ el array de distancia resultante de aplicar el algoritmo de Dijkstra sobre el nodo $i$ como fuente. La forma de colocar los valores en dicho array es peguntar para cada nodo $u$ y $v$ de la tupla $(u, v, l) \in Q$ si se calculó previamente el array de Dijkstra de distancia a partir de este en el grafo dado, en caso negativo se realiza un llamado al método $dijkstra(...)$ el cual utilizamos en la solución de la sección **2.2)**. Una vez calculado dichos valores de $dijkstra$, realizamos el mismo procedimiento que en la subsección anterior, donde para cada tupla en $Q$ se analiza cada arista del grafo y se evalúa el predicado que utilizamos para determinar si esta es útil, teniendo en cuenta que solo debemos indexar por el valor de distancia precalculado en el array $node\_dist$. Finalmente, se mantiene la misma idea que la solución anterior, se aumenta en $1$ la respuesta por cada vez que se encuentra una arista útil.

**Pseudocódigo:**
```
dijkstra_qe(n, m, edges, useful_paths_tuples):
    g = Graph(n, m, edges)
    useful_edge = [False for i in range(m)]
    node_dist = [None for i in range(n)]
    total_useful_edges = 0
    
    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        if node_dist[u] is None:
           node_dist[u] = dijkstra(u, g)
        if node_dist[v] is None:
            node_dist[v] = dijkstra(v, g)
    
    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        for i in range(m):
            edge = edges[i]
            if useful_edge[i]:
                continue
            x, y, weight = edge
            if node_dist[u][x] + weight + node_dist[v][y] <= l or node_dist[u][y] + weight + node_dist[v][x] <= l:
                useful_edge[i] = True
                total_useful_edges += 1

    return total_useful_edges
```

**Complejidad Temporal**
En las primeras líneas del algoritmo se realiza una fase de preprocesamiento donde se construye un grafo en $O(n + m)$ donde $n$ y $m$, es la cantidad de nodos y aristas del grafo, luego, se inicializa el array $useful\_edges$ donde para la arista $i$ se determina si esta es útil o no y dicha inicialización es realizada en $O(m)$. Posteriormente, se procede a inicializar el array $node\_dist$ en $O(n)$.

Para actualizar los valores de $node\_dist$ se recorre el conjunto $Q$ y se analiza por cada tupla los nodos $u$ y $v$ y se procede a determinar el array resultante de aplicar el algoritmo de Dijkstra sobre estos en caso de que no hayan sido calculados. Dicho procedimiento se ejecuta en $O(q*(mlogm))$ para el peor caso donde el grafo fuese denso y donde $q$ denota el tamaño de $Q$.

En la última sección del algoritmo, se analiza cada arista del grafo por cada tupla de $Q$ y se procede a verificar el predicado para determinar si una arista es útil, teniendo los valores necesarios de distancia precalculados, los cuales pueden ser accedidos en $O(1)$.

Finalmente, la complejidad del algoritmo sería $O(n + m + m + n + q*(m\log{m}) + q*m) = O(m + n + q*(m\log{m}) + q*m)$.

## **3) Implementación del proyecto:**
El proyecto está dividido en tres secciones principales: Soluciones, Informe y Pruebas. Todas las implementaciones fueron realizadas con el lenguaje de programación $Python$. El punto de entrada para la ejecución del proyecto es el archivo $main.py$ en el directorio principal. Desde este se pueden ejecutar los scripts en las carpetas de *Soluciones* y *Pruebas* importando el archivo y los métodos específicos que se deseen ejecutar.

Para ejecutar el proyecto sólo es necesario ejecutar el archivo $main.py$ el cual por defecto tiene la implementación para hallar la solución de una instancia del problema. Una vez ejecutamos este script se debe dar de entrada los valores $n$ y $m$ en una misma línea, denotando las dimensiones del grafo que queremos crear, luego en las siguientes $m$ líneas se da de entrada se deben escribir tiplos de la forma $(x, y, z)$ denotando una arista entre los nodos $x$ e $y$ con peso $z$. Luego, se debe entrar el valor de $q$ y en las siguientes $q$ líneas se deben entrar los triplos de la forma $(u, v, l)$, denotando la posibilidad de hallar las aristas de los caminos de $u$ a $v$ con costo menor o igual a $l$. Finalmente, al presionar $enter$ de devuelve la respuesta al problema: el número de carreteras útiles dado el conjunto $Q$.
A continuación se muestra un ejemplo de flujo de entrada y salida por consola:
```
Input:
3 2
0 1 1
1 2 1
2
0 2 3
0 1 1
```
```
Output:
2
```

- **Soluciones:**
En esta carpeta se encuentran las distintas soluciones probadas para resolver el problema planteado. Todas contienen en esencia un método principal que recibe una entrada en el formato $n, m, edges, useful\_paths\_tuples$ donde $n$ y $m$ son la cantidad de nodos y arista del grafo respectivamente, $edges$ el es conjunto de aristas y $useful\_path\_tuples$ es el conjunto $Q$. Como salida de estos métodos se da un valor entero que representa el número de carreteras (aristas) útiles.

- **Informe:** Constituye el resumen de los experimentos llevados a cabo en el proyecto y contiene las demostraciones que prueban la correctitud de los mismos.

- **Pruebas:** Contiene el script [algos_output_tester.py](), el cual genera casos de prueba aleatorios y compara las salidas de las soluciones implementadas y comprueba la igualdad en la salida de estas para mostrar su equivalencia. También se incluyó el archivo [tester.py]() que contiene la función *test_solution(...)* que recibe de entrada una función que resuelve el problema y se desea evaluar y luego se comparan las respuestas de esta con las del método de solución *brute_force(...)* y finalmente se da como retorno "Accepted!!" si coincidieron todas las respuestas y "Wrong Answer!!" en caso contrario. 
