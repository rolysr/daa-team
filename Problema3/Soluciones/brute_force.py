import copy


def brute_force1(n, m, edges):
    bitmask = [True for i in range(m)]
    
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True
    
    for i in range(1, 2**m):
        for j in range(m-1):
            #print(len(bitmask), j)
            bitmask[j] = i & j
        if is_valid_graph(n, m, edges, bitmask):
            return True

    return False

def brute_force(n,m,edges):
    bitmask = [True for i in range(a[0][1])]
    if m== 0 or is_valid_graph(n,m,edges,bitmask):
        print(True)
    else:
        print(brute_force_recursive(n,m,edges,bitmask,0))

def brute_force_recursive(n, m, edges,bitmask,arist):
    if arist== m:
        print(bitmask)
        return is_valid_graph(n,m,edges,bitmask)
    
    arist+=1
    if brute_force(n,m,edges,bitmask,arist):
        return True
    bitmask[arist-1]=False
    if brute_force(n,m,edges,bitmask,arist):
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
