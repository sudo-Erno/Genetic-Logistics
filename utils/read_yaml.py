import yaml

path = 'VALUES.yaml'
def read_yaml():
    with open(path, 'r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

if __name__ == '__main__':
    print(read_yaml())