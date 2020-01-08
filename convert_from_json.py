from rfc3986 import builder


def to_urls( json ):
    result = ''
    for record in json:
        print('start of processing of record')
        if not ('disabled' in record and record['disabled']):
            print('executing of convertions')
            result += convert_record_to_url(record)
            print('result=',result)
    return result


def convert_record_to_url(record):

    uri_builder = builder.URIBuilder().add_host(record['domain_name'])
    if 'scheme' in record:
        uri_builder = uri_builder.add_scheme(record['scheme'])
    if 'username' in record:
        #TODO: check if password and username is alphanumeric only
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
       

            
#            print(uri_builder.finalize().unsplit())
            #print(record)
    return uri_builder.finalize().unsplit()
            


