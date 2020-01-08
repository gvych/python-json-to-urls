#!/usr/bin/env python3

import argparse
import json
import sys

cli_parser = argparse.ArgumentParser()
cli_parser.add_argument("input_file", help="path to file cointaining input data")
arguments = cli_parser.parse_args()

try:
    with open(arguments.input_file) as input_file:
        data = json.load(input_file)
        print(data)

    """
    finally:
        input_file.close()
    """

except:
    print( "Unexpected error:",  file=sys.stderr )
    raise

