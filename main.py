#!/usr/bin/env python3

import argparse
import json
import sys
import convert_from_json


cli_parser = argparse.ArgumentParser()
cli_parser.add_argument("input_file", help="path to file cointaining input data")
arguments = cli_parser.parse_args()

try:
    with open(arguments.input_file) as input_file:
        data = json.load(input_file)
        urls = convert_from_json.to_urls(data)
        #print(urls)


except:
    print( "Unexpected error:",  file=sys.stderr )
    raise

