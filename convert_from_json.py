from rfc3986 import builder
import validators


def to_url( record ):
    if 'disabled' in record:
        if not isinstance(record['disabled'], (bool)):
            raise KeyError('"disabled" field must be boolean type')

        if record['disabled']:
          return

    if not validators.domain(record['domain_name']):
        raise KeyError('domain_name is in invalid format')
    uri_builder = builder.URIBuilder().add_host(record['domain_name'])

    if 'username' in record:
        #TODO: check if password and username is alphanumeric only
        if 'password' in record:
            uri_builder = uri_builder.add_credentials(record['username'],record['password'])
        else:
            uri_builder = uri_builder.add_credentials(record['username'])


    if 'scheme' in record:
        if record['scheme'] not in ['http','https']:
            raise KeyError('scheme is invalid, only http and https allowed')
        uri_builder = uri_builder.add_scheme(record['scheme'])
    if 'port' in record:
        uri_builder = uri_builder.add_port(record['port'])
    if 'path' in record:
        uri_builder = uri_builder.add_path(record['path'])
    if 'query' in record:
        uri_builder = uri_builder.add_query_from(record['query'])
    if 'fragment' in record:
        uri_builder = uri_builder.add_fragment(record['fragment'])
       
    uri = uri_builder.finalize().unsplit()

    return uri
