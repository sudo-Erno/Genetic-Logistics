from math import dist, sqrt
import numpy as np
from geopy.distance import geodesic

def fitness(paths, locations, avg_speed=15):
    """
    Calculates all the times it takes, and sort it by the best.

    paths: Matrix with the random generated paths.
    starting_location: List containing the latitude and longitude of the location where we start.
    locations: List containing latitude and longitude.
    avg_speed: Average speed of the delivery [m/s].
    """

    times_dic = {}
    path_count = 0
    starting_location = locations[0]
    locations = locations[1:]

    for path in paths:

        times = []
        actual_location = starting_location
    
        for i in range(len(path)):
            loc_index = path[i]

            if loc_index == -1: # Reached the starting point
                distance = float(geodesic(actual_location, starting_location).meters)

            else:
                final_location = locations[loc_index]
                distance = float(geodesic(actual_location, final_location).meters)
                
                actual_location = locations[loc_index]
            
            time = distance / avg_speed
            times.append(time)

        times_dic[path_count] = np.sum(np.array(times))
        path_count += 1

    times_dic = sorted(times_dic.items(), key=lambda kv: kv[1])

    return times_dic

if __name__ == '__main__':
    fitness(np.array([[0, 1, 2, -1], [1, 0, 2, -1], [1, 2, 0, -1]]), [(-34.560831994594594, -58.44246026486486), (-34.56496493877551, -58.466294667346936), (-34.57679675510204, -58.48830855102041), (-34.5453508, -58.4739094)])