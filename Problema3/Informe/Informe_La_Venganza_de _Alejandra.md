# Informe sobre solución al problema: La Venganza de Alejandra
## Equipo: $D^{aa}$
## Integrantes:
 - Andry Rosquet Rodríguez - C411
 - Rolando Sánchez Ramos - C411

## **1) Introducción al problema:**
En el archivo [La Venganza de Alejandra]() nos definen un problema donde se tiene un grafo, no dirigido, con aristas simples consideradas las relaciones entre los compañeros de Alejandra. El número de nodos y aristas del grafo serán denotados por $n$ y $m$ respectivamente en el resto del documento.

La solución del problema consiste en determinar si es posible eliminar aristas del grafo,de manera, que el grafo resultante tenga a todos sus nodos con grado 3 ó 0, exceptuando el caso en que todos tengan grado 0. Lo anterior se traduce en que cada compañero de Alejandra termine com 3 o ninguna amistad.

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
def brute_force_recursive(n, m, edges):
    bitmask = [True for i in range(m)]
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True
    else:
        return brute_force_recursion(n, m, edges, bitmask, 0)

def brute_force_recursion(n, m, edges, bitmask, arist):
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

def is_valid_graph(n, m, edges, bitmask):
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
Nos encontramos en presencia de un algoritmo recursivo que internamente llama el método de validación de la slución cada vez que alcanza la condición de parada. La complejidad de la recursividad resulta simple de determinar en este caso; notemos que se llamará a sí misma a lo sumo 2 veces y además se adentrará hasta que $arist$ alcance el valor de m. Por tanto, como $arist$ aumenta en 1 unidad con cada llamado podemos concluir que la complejidad de la recursividad, sin tener en cuenta los llamados al método de validación, será $O(2^m)$. Ahora, al considerar los llamados a $is\_valid\_graph$ vemos que la complejidad final será $O((m+2n)*2^m). Esto se debe a que el método anterior hace primero un recorrido por las $m$ aristas y luego dos ciclos por el array $degrees\_vertex$ con tamaño $n$. Finalmente la complejidad se puede reducir a solo $O(2^m)$, ya que se puede despreciar la parte polinomial.

### **2.2) Solución Fuerza Bruta con Máscara de Bits:**
Al igual que en el algoritmo anterior se desea iterar por cada posibilidad que nos otorga el remover o dejar una arista. Para luego, concluir si hay al menos una variante válida.

**Idea general de solución:**

El método $brute\_force\_bitmask$ iterará por las $2^m$ posibilidades que de manera intuitiva nos brinda el poder dejar o remover una arista del grafo. Lo anterior, lo hará usando como recurso máscaras de bits. El ciclo desde 1 a $2^m$ nos brinda la posibilidad de recorrer todos los números binarios con longitud $\leq$ m. Luego notemos que si elevamos $2^i$, con 0 $\leq$ i $\leq$ m, en binario estos números constituirán máscaras donde todos sus dígitos son 0 exceptuando la posición $i$.
Entonces con estas herramientas y con el uso de la operación $Y Lógica(&)$ entre el número del ciclo exterior y las máscaras del ciclo interno, es que iremos ubicando $True$ o $False$ en la lista $bitmask$ que constituye la variación que se debe verificar.
Notar que se recorren todas las variaciones gracias a que como se explicó el ciclo externo estará constituido por todos los números desde 1 a hasta $2^m$, los cuales en binario son todas las variantes de ubicar 1s y 0s en $m$ casillas.

**Pseudocódigo:**
```
def brute_force_bitmask(n, m, edges):
    bitmask = [True for i in range(m)]
    
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True
    
    for i in range(1, 2**m):
        for j in range(m):
            bitmask[j] = True if i & (2**j) else False
        if is_valid_graph(n, m, edges, bitmask):
            return True

    return False
def is_valid_graph(n, m, edges, bitmask):
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
La complejidad temporal de este algoritmo viene dada por el ciclo con $2^m$ iteraciones y dentro de cada una de estas iteraciones se lleva a cabo otro ciclo, este de longitud m, y un llamado a la función $is\_valid_graph$ de la cual ya conocemos su complejidad (véase complejidad de solución fuerza bruta con recursividad $O(2n+m)$). Por tanto, el algoritmo tiene como complejidad temporal $O((2n+2m)*2^m)$, la cual es equivalente a $O(2^m)$.

### **2.3) Solución !!!!!Pendiente!!!!!!:**


**Idea general de solución:** 


**Pseudocódigo:**
```
```

**Complejidad Temporal:**


## **3) Implementación del proyecto:**
El proyecto está dividido en tres secciones principales: Soluciones, Informe y Pruebas. Todas las implementaciones fueron realizadas con el lenguaje de programación $Python$. El punto de entrada para la ejecución del proyecto es el archivo $main.py$ en el directorio principal. Desde este se pueden ejecutar los scripts en las carpetas de *Soluciones* y *Pruebas* importando el archivo y los métodos específicos que se deseen ejecutar.

Para ejecutar el proyecto sólo es necesario ejecutar el archivo $main.py$ el cual por defecto tiene la implementación para hallar la solución de una instancia del problema. Una vez ejecutamos este script se debe dar de entrada los valores $n$ y $m$ en una misma línea, denotando las dimensiones del grafo que queremos crear, luego en las siguientes $m$ líneas se deben escribir duplos de la forma $(x, y)$ denotando una arista entre los nodos $x$ e $y$.
A continuación se muestra un ejemplo de flujo de entrada y salida por consola:
```
Input:
```
```
Output:

```

- **Soluciones:**


- **Informe:** Constituye el resumen de los experimentos llevados a cabo en el proyecto y contiene las demostraciones que prueban la correctitud de los mismos.

- **Pruebas:** Contiene el script [algos_output_tester.py](), el cual genera casos de prueba aleatorios y compara las salidas de las soluciones implementadas y comprueba la igualdad en la salida de estas para mostrar su equivalencia. También se incluyó el archivo [tester.py]() que contiene la función *test_solution(...)* que recibe de entrada una función que resuelve el problema y se desea evaluar y luego se comparan las respuestas de esta con las del método de solución *!!!!!!!!!!!!!!!!!!rellenar!!!!!!!!!!!!!!!!* y finalmente se da como retorno "Accepted!!" si coincidieron todas las respuestas y "Wrong Answer!!" en caso contrario. 
