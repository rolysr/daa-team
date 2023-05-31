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
