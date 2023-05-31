from random import randrange

class Graph:
    def __init__(self, n, m, edges) -> None:
        self.n = n
        self.m = m
        self.nodes = [i for i in range(n)]
        self.edges = edges
        self.adyacents = {}
        for i in range(n):
            self.adyacents[i] = []
        for edge in edges:
            node_x, node_y = edge
            if not self.adyacents[node_x].__contains__(node_y):
                self.adyacents[node_x].append(node_y)
                self.adyacents[node_y].append(node_x)
    
    def delete_node(self , node):
        adyacent = self.adyacents[node]
        temp=[]
        for i in self.edges:
            if i[0] != node and i[1] != node:
                temp.append(i)
        self.edges = temp
        self.m = len(temp)/2
        k=-1
        if self.m !=0:
            for i in self.edges:
                if i[1]>k:
                    k=i[1]
                if i[0]>k:
                    k=i[0]
            mark=[False  for i in range(k+1)]
            for i in self.edges:
                if not mark[i[0]]:
                    mark[i[0]]=True
                elif not mark[i[1]]:
                    mark[i[1]]=True
            c=0
            temp=[]
            for i in range(len(mark)):
                if mark[i]:
                    temp.append(i)
                    c+=1
            self.n=c
            self.nodes=temp
        else: 
            self.n=0
            self.nodes =[]
        self.adyacents.__delitem__(node)
        for i in adyacent:
            temp=self.adyacents.__getitem__(i)
            temp.remove(node)
            self.adyacents[i]=temp
 
def generate_test_cases(number_test_cases):
    test_cases = []

    for i in range(number_test_cases):
        n = randrange(5,6)
        m = 0
        edges = []
        for j in range(n):
            for k in range(n):
                if j != k:
                    edge = (j, k,)
                    edges.append(edge)
                    m += 1

        test_cases.append((n, m, edges))

    return test_cases

def generate_test_cases1(number_test_cases):
    test_cases = []
    n = 7
    m = 6
    edges = []
    edges.append((0,1))
    edges.append((1,0))
    edges.append((0,2))
    edges.append((2,0))
    edges.append((0,3))
    edges.append((3,0))
    edges.append((4,5))
    edges.append((5,4))
    edges.append((0,6))
    edges.append((6,0))
    edges.append((6,1))
    edges.append((1,6))
    test_cases.append((n, m, edges))

    return test_cases
        
def generate_test_cases2(number_test_cases):
    test_cases = []
    n = 7
    m = 8
    edges = []
    edges.append((0,1))
    edges.append((1,0))
    edges.append((0,2))
    edges.append((2,0))
    edges.append((0,3))
    edges.append((3,0))
    edges.append((4,5))
    edges.append((5,4))
    edges.append((0,6))
    edges.append((6,0))
    edges.append((6,1))
    edges.append((1,6))
    edges.append((2,1))
    edges.append((1,2))
    edges.append((6,2))
    edges.append((2,6))
    
    test_cases.append((n, m, edges))

    return test_cases

def brute_force(n, m, edges):
    g = Graph(n, m, edges)
    degrees = [0 for i in range(n)]
    for edge in edges:
        degrees[edge[0]]+=1
    get_reduction(g,degrees)
 #   for i in g.nodes:
#        k
    return g
        
def get_reduction(g,degrees):
    cicle=True
    temp=degrees
    while cicle:
        cicle=False
        for i in range(len(temp)):
            if temp[i] < 3 and temp[i] != 0:
                g.delete_node(i)
                cicle=True
        if cicle:
          temp=[0 for i in range(len(degrees))]  
          for edge in g.edges:
              temp[edge[0]]+=1          
        

a= generate_test_cases2(1)
print(a[0])
g= brute_force(a[0][0],a[0][1],a[0][2])
print(g.n)
print(g.m)
print(g.edges)
print(g.adyacents)
print(g.nodes)

