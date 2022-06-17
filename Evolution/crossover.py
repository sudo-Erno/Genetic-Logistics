import random
import numpy as np
from utils.read_yaml import read_yaml

values = read_yaml()
initial_size = values["INITIAL_POPULATION"]

def single_point_crossover():
    pass

def two_point_crossover(population):
    """
    This crossover will be made between 2 consecutives items. That means, number 0 with number 1, number 2 with number 3, and so on.
    
    population: List of the population.
    
    """

    len_population = len(population)
    new_population = population.copy()

    # Index of range for crossover
    start, final = random.randint(0, len_population - 1), random.randint(0, len_population - 1)
    
    while final == start:
        final = random.randint(0, len_population - 1)

    # Set the range for selecting the genes fro crossover
    start, final = sorted([start, final])

    for i in range(0, len_population, 2):
        p1 = population[i]

        if i + 1 < len_population:
            
            # Select the pairs
            p2 = population[i + 1]

            # The .copy() is for unlinking the variables so if I change one, the other one is not modified
            genes_1 = list(p1[start:final].copy())
            genes_2 = list(p2[start:final].copy())

            # Check if there are any duplicates
            genes_index_crossover = [] # List containing the index of the genes that are not duplicated

            for g in genes_1:
                if not g in genes_2:
                    ind = genes_1.index(g)
                    genes_index_crossover.append(ind)

            for i in genes_index_crossover:
                g1, g2 = genes_1[i], genes_2[i]

                genes_1[i] = g2
                genes_2[i] = g1

            new_population = np.vstack((new_population, p1, p2))

    return np.array(new_population)

def uniform_crossover():
    pass