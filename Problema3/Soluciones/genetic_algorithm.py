from random import randrange
import matplotlib.pyplot as plt
import numpy as np
import math

def generate_test_cases(number_test_cases):
    test_cases = []

    for i in range(number_test_cases):
        n = randrange(6,7) 
        m = 0
        edges = []
        for j in range(n-1):
            for k in range(j, n):
                if j != k and randrange(0, 2):
                    edge = (j, k)
                    edges.append(edge)
                    m += 1
        test_cases.append((n, m, edges))
    return test_cases

def genetic_algorithm(graph,iterative_solution):
    m=graph[1]
    n=graph[0]
    edges=graph[2]
    solutions=random_solutions(m)
    dict_penalties={}

    for i in range(len(solutions)):
        degrees=get_degrees(n,solutions[i],edges)
        penalty=make_calculation(degrees,m)
        if dict_penalties.get(penalty) == None:
            dict_penalties[penalty]=[solutions[i]]
        else:
            dict_penalties[penalty].append(solutions[i])


    ordered_penalties = sorted(dict_penalties)
    new_solutions=[]
    if iterative_solution != []:
        new_solutions.append(iterative_solution)
            
    i=0
    while len(new_solutions)<= int(math.log2(m)):
        for j in dict_penalties[ordered_penalties[i]]:
            new_solutions.append(j)
        i+=1
    new_solutions= [new_solutions[i] for i in range(int(math.log2(m)))]
    
    final_solution=compare_solutions(new_solutions)
    final_penalty=make_calculation(get_degrees(n,final_solution,edges),m)
   
    return final_solution,final_penalty 

def compare_solutions(solutions):
    final_solution=[]
    trues=0
    falses=0
    for i in range(len(solutions[0])):
        for j in range(len(solutions)):
            if solutions[j][i]:
                trues+=1
            else:
                falses+=1
        if trues>=falses:
            final_solution.append(True) 
        else:
            final_solution.append(False)  
        trues=0
        falses=0    
    return final_solution

def get_degrees(n,bitmask,edges):
    degree_vertex = [0 for i in range(n)]

    for i in range(len(edges)):
        if bitmask[i]:
            a, b = edges[i]
            degree_vertex[a] += 1
            degree_vertex[b] += 1
    return degree_vertex

def random_solutions(m):
    if m<6:
        raise Exception("Imposible graph, it should have more than 6 arist at least")
    if m<10:
        number_solutions= 50
    else:
        number_solutions=200
    solutions=[]
    while len(solutions) !=number_solutions:
        posible_solution=generate_solution(m)
        if differents_solutions(posible_solution,solutions):
            solutions.append(posible_solution)
    return solutions

def differents_solutions(posible_solution,solutions):
    if len(solutions)==0:
        return True
    for i in solutions:
        if i==posible_solution:
            return False
    return True    

def generate_solution(m):
    solution=[]
    for i in range(m):
        r=randrange(0,2)
        if r==1:
            solution.append(True)
        else:
            solution.append(False)
    return solution

def difference_cost(x):
    if x == 0 or x == 3:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return x - 3

def make_calculation(degrees,m):
    if sum(degrees)==0:
        return m

    fit = 0
    for i in degrees:
        fit += difference_cost(i)
    return fit


def genetic_same_graph_different_population():
    graph = generate_test_cases(1)[0]
    degrees = get_degrees(graph[0],[True for i in range(graph[1])],graph[2])
    initial_penalty = make_calculation(degrees,graph[1])

    results=[]
    results.append(initial_penalty)
    x=[1,2,3,4,5,6,7,8,9,10,11]

    for i in range(10):
        final_solution,final_penalty=genetic_algorithm(graph,[])
        results.append(final_penalty)

    plt.plot(x,results,"o")
    plt.show()
    
def iterative_genetic():
    graph = generate_test_cases(1)[0]
    results=[]
    final_solution=[]
    x=[i for i in range(30)]

    for i in range(30):
        final_solution,final_penalty=genetic_algorithm(graph,final_solution)
        results.append(final_penalty)

    plt.plot(x,results,"o")
    plt.show()