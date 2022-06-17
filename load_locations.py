from API.geographic_data import save_locations
import sys
import os

args = sys.argv[1:]

def load_locations(path):
    
    with open(path, 'r') as file:
        raw_locations = file.readlines()
        clean_locations = []

        for l in raw_locations:
            l = l.split('\n')[0]
            clean_locations.append(l)

    save_locations(clean_locations)