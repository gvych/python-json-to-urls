#!/usr/bin/env python3

import argparse
import json
import sys
import rfc3986
from rfc3986 import builder


def convert_to_urls( json ):
    for record in json:


        if not ('disabled' in record and record['disabled']):
            uri_builder = builder.URIBuilder().add_host(record['domain_name'])
            
            if 'scheme' in record:
                uri_builder = uri_builder.add_scheme(record['scheme'])

            if 'username' in record:
                if 'password' in record:
                    uri_builder = uri_builder.add_credentials(record['username'],record['password'])
                else:
                    uri_builder = uri_builder.add_credentials(record['username'])

            if 'port' in record:
                uri_builder = uri_builder.add_port(record['port'])

            if 'path' in record:
                uri_builder = uri_builder.add_path(record['path'])

            if 'query' in record:
                uri_builder = uri_builder.add_query_from(record['query'])

            if 'fragment' in record:
                uri_builder = uri_builder.add_fragment(record['fragment'])

               

            
            print(uri_builder.finalize().unsplit())
            #print(record)
            



cli_parser = argparse.ArgumentParser()
cli_parser.add_argument("input_file", help="path to file cointaining input data")
arguments = cli_parser.parse_args()

try:
    with open(arguments.input_file) as input_file:
        data = json.load(input_file)
        urls = convert_to_urls(data)
        #print(urls)


except:
    print( "Unexpected error:",  file=sys.stderr )
    raise

