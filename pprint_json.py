import json
import pprint


def load_data(filepath):
    with open (filepath, 'r', encoding = 'utf8') as file:
        data = json.load(file)
    return data


def pretty_print_json(data):
    data.insert(0, data)
    pprint.pprint(data)


if __name__ == '__main__':
    filepath = input('Введите путь к файлу' + '\n')
    data = load_data(filepath)
    
