import json
from pprint import pprint
import collections
from collections import defaultdict

keys = list()
nested_keys = []


def parse_record(record):

    for key in record.keys():
        keys.append(key)

        if type(record[key]) is list:

            parse_dictionary(record[key], key, level = 0)


def parse_dictionary(dictionary, key, level):

    if level == len(nested_keys):
        nested_keys.append(defaultdict(list))

    for element in dictionary:
        if type(element) is dict:
            for element_key in element.keys():
                nested_keys[level][key].append(element_key)
                nested_keys[level][key] = list(set(nested_keys[level][key]))
                if type(element[element_key]) is list:
                    level = level + 1
                    parse_dictionary(element[element_key], element_key, level)
                    level = level - 1


def print_data():

    key_number = 1
    print ''
    print ''
    print ' Key No.    Key'
    for key in keys:
        print ''
        print '    ', key_number, ' ' , key
        key_number += 1

        if key in nested_keys[0].keys():
            for sub_key in nested_keys[0][key]:
                print '           |'
                print '           |-', sub_key
                if sub_key in nested_keys[1].keys():
                   for inner_key in nested_keys[1][sub_key]:
                        print '               |'
                        print '               |-', inner_key
            print ''


if __name__ == '__main__':

    # Open edited sample json file.
    with open('edited_sample.json') as data_file:
         data = json.load(data_file)

    # sample_key : Key mapped for all dictionaries.
    for record in data['sample_key']:
        parse_record(record)
    keys = list(set(keys))
    print_data()
