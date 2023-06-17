from random import randrange
import matplotlib.pyplot as plt
import numpy as np
#from Pruebas.test_cases_generator import generate_test_cases
import math

def generate_test_cases(number_test_cases):
    test_cases = []

    for i in range(number_test_cases):
        n = randrange(7,8) 
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

def genetic_algorithm():
    graph = generate_test_cases(1)[0]
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
    i=0
    while len(new_solutions)<= int(math.log2(m)):
        for j in dict_penalties[ordered_penalties[i]]:
            new_solutions.append(j)
        i+=1
    #Aqui ya tenemos log(m) en base 2 soluciones posibles. Las mejores penalizadas segun distanciamiento de cada nodo del
    #grado 0 o 3
    final_solution=compare_solutions(new_solutions)
    #La solucion final la construye en base a si la arista i aparece como que debe quedarse en una mayor
    #cantidad de soluciones
    return final_solution 
#El proceso solo se hace una vez podemos coger el cuerpo del algoritmo y crear un metodo generico al que
# se le pasa la solucion final. El ejecuta todo igual que este pero como primera new_solution tedria
# final_solution

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
        raise Exception("Imposible graph")
        return
    number_solutions= 2**(m-1)
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

class GeneticAlgorithm:
    
    def __init__(self, create_individual, fitness, crossover, mutations) -> None:
        self.create_individual = create_individual
        self.fitness = fitness
        self.crossover = crossover
        self.mutations = mutations

    def fit(self):
        
        population_size = 200
        generation = 0
        population = []
        for i in range(population_size):
            individual = self.create_individual()
            population.append(individual)
            
        best_fitness = self.fitness()


        for i, ind in enumerate(population):
            self.fitness(ind)
    
    
genetic_algorithm()