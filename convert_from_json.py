from rfc3986 import builder
import validators


def to_url( record ):
    if 'disabled' in record:
        if not isinstance(record['disabled'], (bool)):
            raise ValueError('"disabled" field must be boolean type')

        if record['disabled']:
          return


    if not validators.domain(record['domain_name']):
        raise ValueError('domain_name is in invalid format')

    uri_builder = builder.URIBuilder().add_host(record['domain_name'])


    if 'username' in record:
        if not record['username'].isalnum():
            raise ValueError('username must be alphanumeric string')
        if 'password' in record:
            if not record['password'].isalnum():
                raise ValueError('password must be alphanumeric string')
            uri_builder = uri_builder.add_credentials(record['username'],record['password'])
        else:
            uri_builder = uri_builder.add_credentials(record['username'])


    if 'scheme' in record:
        if record['scheme'] not in ['http','https']:
            raise ValueError('scheme is invalid, only http and https allowed')
        uri_builder = uri_builder.add_scheme(record['scheme'])


    if 'port' in record:
        uri_builder = uri_builder.add_port(record['port'])

    if 'path' in record:
        uri_builder = uri_builder.add_path(record['path'])
        if not validators.url(uri_builder.finalize().unsplit()):
            raise ValueError('path is invalid format')

    if 'query' in record:
        uri_builder = uri_builder.add_query_from(record['query'])
        if not validators.url(uri_builder.finalize().unsplit()):
            raise ValueError('query is invalid format')

    if 'fragment' in record:
        uri_builder = uri_builder.add_fragment(record['fragment'])
        if not validators.url(uri_builder.finalize().unsplit()):
            raise ValueError('fragment is invalid format')
       

    uri = uri_builder.finalize().unsplit()


    return uri
