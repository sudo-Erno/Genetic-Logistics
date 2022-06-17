from os.path import isfile
from API.geographic_data import save_locations

def preprocess_location_locations(raw_locations_path):
    
    locations = []
    lat_lon = []

    route_file_name = raw_locations_path.split('\\')[-1].split('.')[0]

    if isfile(raw_locations_path):
        with open(raw_locations_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                line = str(line[:-1])
                locations.append(line)

        data = save_locations(locations, route_file_name)

        # Get the lat and lon of the locations
        for info in data.values():
            lat, lon = 0, 0
            for k, v in info.items():
                if k == 'lat':
                    lat = float(v)
                elif k == 'lon':
                    lon = float(v)
            
            lat_lon.append((lat, lon))

        return lat_lon
        
    return False