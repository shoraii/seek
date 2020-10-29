import argparse
import json
import yaml
import logging
import os


def get_key_list(key):
    if key[0] == '[' and key[-1] == ']':
        key = key[1:-1]
    key = key.split(',')
    for i in range(len(key)):
        key[i] = key[i].strip()
        if key[i].isdigit() or key[i].startswith('-') and key[1:].isdigit():
            key[i] = int(key[i])
        else:
            key[i] = str(key[i])
            if key[i][0] == '\'' or key[i][0] == '"':
                key[i] = key[i][1:]
            if key[i][-1] == '\'' or key[i][-1] == '"':
                key[i] = key[i][:-1]
    return key


def get_data(path_to_file, key, file_type):
    with open(path_to_file) as file:
        logging.info(f'Opened {path_to_file}')
        if file_type == 'json':
            data = json.load(file)
        else:
            data = yaml.full_load(file)
    return data


def get_value(data, key):
    for key_element in key:
        data = data[key_element]
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

    logging.info(f'Converting key argument to list...')
    key_list = get_key_list(key)
    logging.info(f'Converted key argument')

    data = get_data(path_to_file, key, file_type)
    logging.info(f'Successfully read data from {path_to_file}')

    value = get_value(data, key_list)
    print(value)


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
    parser.add_argument(
        'path_to_file',
        action='store',
        help='path to examined file')
    parser.add_argument('key', action='store', help='key to seek for')
    parser.add_argument('-t', action='store', help='file_type: json, yaml')

    args = parser.parse_args()
    logging.info(
        f'Parsed arguments, got args.key = {args.key}, args.t = {args.t}')
    main(args.path_to_file, args.key, args.t)
