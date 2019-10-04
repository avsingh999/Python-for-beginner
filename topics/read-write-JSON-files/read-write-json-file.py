# -*- coding: utf-8 -*-
import json

def main():
    # Define data
    data = {'a list': [1, 2, 3.141, 1993, 'help', u'€'],
            'a string': 'bla',
            'another dictionary': { 'foo': 'bar',
                                    'key': 'value',
                                    'the answer': 42
                                    }
            }

    # Write JSON file
    with open('data.json', 'w') as outfile:
        _make_str = json.dumps(data, indent = 4, sort_keys = True, ensure_ascii = False)
        outfile.write(_make_str)

    # Read JSON file
    with open('data.json') as data_file:
        data_loaded = json.load(data_file)

    # Check for read and write data is equel or not
    print(data == data_loaded) 

if __name__ == "__main__":
    main()
