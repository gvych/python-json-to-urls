from rfc3986 import builder


def to_url( record ):
    if 'disabled' in record:
        if record['disabled'] not in [True,False]:
            raise KeyError

        if record['disabled']:
          return

    uri_builder = builder.URIBuilder().add_host(record['domain_name'])

    if 'scheme' in record:
        if record['scheme'] not in ['http','https']:
            raise KeyError
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
       
    return uri_builder.finalize().unsplit()
