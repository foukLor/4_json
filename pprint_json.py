import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as j_file:
        data = json.load(j_file)
    return data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys = True, indent = 4, 
                        separators = (':', ',')))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python3.5 pprint_json.py filepath")
    data = load_data(sys.argv[1])
    if data is not None:
        pretty_print_json(data)
