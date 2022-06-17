import numpy as np
import sys
import os
import json
import random
from utils.read_yaml import read_yaml
from graph_data import plot_locations, plot_times_average
from utils.preprocessing import preprocess_location_locations
# from GUI.main_window import run_gui
from Evolution.fitness import fitness
from Evolution.selection import selection
from Evolution.crossover import two_point_crossover
from Evolution.repopulation import repopulate
from load_locations import load_locations

args = sys.argv[1:]

# random.seed(42)
values = read_yaml()

# READ THE VALUES FROM THE .yaml
num_initial_population = values["INITIAL_POPULATION"]
avg_speed = values["AVG_SPEED"]
survivors = values["SURVIVORS"]
new_pop_size = values["NEW_POP_SIZE"]
generations = values["GENERATIONS"]
debug = values["DEBUG"]
locations = preprocess_location_locations(values["LOCATIONS"]) # List with lat and lon of each location

if not locations:
    print("[!] Error reading the locations file.")
    quit()

def flag_parser():
    global debug
    for i in range(len(args)):
        flag = args[i]
        if flag == '--plot-locations':
            plot_locations(locations)
            exit()
        if flag == '--debug':
            debug = True

flag_parser()

num_locations = len(locations) - 1 # We substract one since the first location is the starting point

# Create the matrix where all posible options will be stored.
paths_matrix = np.ones((num_initial_population, num_locations + 1)) # We add 1 since ith will be de -1 indicating the end of the path

# Create initial generations
for i in range(num_initial_population):
    random_places = random.sample(range(0, num_locations), num_locations)
    random_places.append(-1) # The -1 represents the starting point
    paths_matrix[i] = random_places

paths_matrix = np.unique(paths_matrix, axis=0).astype("int") # Remove the repeated ones.

initial_generation = paths_matrix.copy() # For debugging purpose

abs_min_value = float("inf")
times_averages = []
best_path = 0

for _ in range(generations):
    population_fitness = fitness(paths_matrix, locations, avg_speed) # Calculates the total time and returns them in increasing order
    selected_paths = selection(population_fitness, survivors) # Returns lists with the best paths and with its total time

    selected_paths_indeces, selected_paths_values = selected_paths

    times_averages.append(sum(selected_paths_values) / len(selected_paths_values))

    selected_paths = np.array([paths_matrix[i] for i in selected_paths_indeces])
    
    min_value = min(selected_paths_values)
    if min_value < abs_min_value:
        abs_min_value = min_value
        bi = selected_paths_values.index(min_value)
        best_path = selected_paths[bi]

    crossover_genes = two_point_crossover(selected_paths.copy()) # .copy() for unlinking the variables
    paths_matrix = repopulate(crossover_genes, new_pop_size)

    if debug:
        print(f"\nSummary of generation {_}")
        print("\nBest Routes\n")
        print(selected_paths)
        print("\nAfter Crossover\n")
        print(crossover_genes)
        print("\nNew Population\n")
        print(paths_matrix)

if debug:
    print("\nInitial Population\n")
    print(initial_generation)
    print(f"\nBest time: {abs_min_value} seconds. / {abs_min_value / 60} minutes. / {abs_min_value / 3600} hours.")
    print(f"\nBest path: {best_path}")

data = [times_averages, abs_min_value, best_path]



# run_gui(data)

plot_times_average(times_averages)
# plot_locations(locations)