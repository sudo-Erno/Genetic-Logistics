# https://pypi.org/project/geopy/
import os
import json
from geopy.geocoders import Nominatim

data = {}
kys = ['boundingbox', 'lat', 'lon', 'display_name']

def save_locations(locations, config_name='My_Route_1'):
    """
    Given a list of streets names and numbers, save it for future use with a config name desired.

    locations: List with the locations of the destinations.
    config_name: Name of the file where the locations will be saved.
    """

    path = f'Data\{config_name}.json'
    geolocator = Nominatim(user_agent='Erno') # TODO: Change the user_agent variable

    for direction in locations:
        location = geolocator.geocode(direction)
        location = location.raw
        
        loc = {}

        for k, v in location.items():
            if k in kys:
                loc[k] = v

        data[location['place_id']] = loc
    
    with open(path, 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return data

if __name__ == "__main__":
    save_locations(["Virrey del Pino 1480", "Olazabal 3228", "Blanco Encalada 5250"], "test")