from random import sample
import numpy as np

def repopulate(actual_population, size_new_population):
    """
    Repopulates the matrix.

    actual_population: Array of the actual population.
    size_new_population: Number of units for this new generation.

    """
    unit_len = len(actual_population[0]) # Number of places the path passes through
    num_actual_paths = actual_population.shape[0]
    
    num_new_paths = 0 if size_new_population < num_actual_paths else size_new_population - num_actual_paths

    if num_new_paths == 0:
        return actual_population

    new_paths = np.ones((num_new_paths, unit_len))

    for i in range(num_new_paths):
        random_places = sample(range(0, unit_len - 1), unit_len - 1)
        new_paths[i][:-1] = random_places
        new_paths[i][-1] = -1 # The -1 represents the starting point

    return np.vstack((actual_population, new_paths))