#!/usr/bin/env python3

import argparse
import json
import sys
import convert_from_json


try:
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("input_file", help="path to file cointaining input data")
    arguments = cli_parser.parse_args()

    with open(arguments.input_file) as input_file:
        for record in json.load(input_file):
            url = convert_from_json.to_url(record)
            if url: print(url)

except:
    print( "Unexpected error:",  file=sys.stderr )
    raise

