import argparse
import json
import yaml
import logging # TODO: add logging
import os

def get_data(path_to_file, key, type):
    with open(path_to_file) as file:
        if type == 'json':
            data = json.load(file)
        else:
            data = yaml.full_load(file)
    return data

def main(path_to_file, key, type):
    if type is None or type not in ['json', 'yaml']:
        filename, file_extension = os.path.splitext(path_to_file)
        file_extension = file_extension.lower()
        if file_extension == '.json':
            type = 'json'
        elif file_extension in ['.yaml', '.yml']:
            type = 'yaml'
        else:
            raise NameError
    data = get_data(path_to_file, key, type)
    print(data[key]) # TODO: complex key

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='seek.py: get value')
    parser.add_argument('path_to_file', action='store', help='path to examined file')
    parser.add_argument('key', action='store', help='key to seek for')
    parser.add_argument('-t', action='store', help='file type: json, yaml')
    args = parser.parse_args()
    main(args.path_to_file, args.key, args.t)