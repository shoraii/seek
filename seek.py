import argparse
import json
import yaml
import logging
import os

def get_data(path_to_file, key, file_type):
    with open(path_to_file) as file:
        logging.info(f'Opened {path_to_file}')
        if file_type == 'json':
            data = json.load(file)
        else:
            data = yaml.full_load(file)
    return data

def main(path_to_file, key, file_type):
    logging.info(f'file_type before checking is {file_type}')
    if file_type is None or file_type not in ['json', 'yaml']:
        filename, file_extension = os.path.splitext(path_to_file)
        file_extension = file_extension.lower()
        if file_extension == '.json':
            file_type = 'json'
        elif file_extension in ['.yaml', '.yml']:
            file_type = 'yaml'
        else:
            raise NameError
    logging.info(f'file_type after checking is {file_type}')
    data = get_data(path_to_file, key, file_type)
    logging.info(f'Successfully read data from {path_to_file}')
    print(data[key]) # TODO: complex key

if __name__ == "__main__":
    logging_level_var = os.environ.get('SEEK_LOGGING_LEVEL', 'DEBUG')
    logging_level = None
    if logging_level_var == 'DEBUG':
        logging_level = logging.DEBUG
    elif logging_level_var == 'INFO':
        logging_level = logging.INFO
    elif logging_level_var == 'WARNING':
        logging_level = logging.WARNING
    elif logging_level_var == 'ERROR':
        logging_level = logging.ERROR
    elif logging_level_var == 'CRITICAL':
        logging_level = logging.CRITICAL
    else:
        logging_level = logging.DEBUG
    logging.basicConfig()
    logging.getLogger().setLevel(logging_level)

    logging.info('Started seek.py')
    logging.info(f'Initialised logger, logging level: {logging_level_var}')

    parser = argparse.ArgumentParser(description='seek.py: get value')
    parser.add_argument('path_to_file', action='store', help='path to examined file')
    parser.add_argument('key', action='store', help='key to seek for')
    parser.add_argument('-t', action='store', help='file_type: json, yaml')

    args = parser.parse_args()
    logging.info(f'Parsed arguments, got args.key = {args.key}, args.t = {args.t}')
    main(args.path_to_file, args.key, args.t)