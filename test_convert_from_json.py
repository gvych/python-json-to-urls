#!/usr/bin/env python3


import unittest
import convert_from_json

class TestConvertFromJSON(unittest.TestCase):

    def test_all_args(self):
        result = convert_from_json.to_url({"scheme": "http", "username":"user","password":"pass", "domain_name": "test.com", "port": "8080", "path": "path/to/file","fragment": "header2", "query": { "key1": "value1" } })
        self.assertEqual(result, "http://user:pass@test.com:8080/path/to/file?key1=value1#header2")

    def test_invalid_scheme(self):
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","scheme":"ftp"})

    def test_invalid_domain(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {})
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"^"})

    def test_disabled_field(self):
        result = convert_from_json.to_url({"disabled":True,"domain_name":"test.com"})
        self.assertEqual(result, None)
        self.assertRaises(ValueError, convert_from_json.to_url, {"disabled":"not boolean","domain_name":"test.com"})

    def test_invalid_port(self):
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","port":"not a port"})
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","port":"-123"})
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","port":"12.3"})
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","port":"66000"})

    def test_invalid_path(self):
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","path":"^"})

    def test_invalid_query(self):
        self.assertRaises(TypeError, convert_from_json.to_url, {"domain_name":"test.com","query":"<>\^`{|}"})
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","query":{"key1":"<>\^`{|}"}})

    def test_invalid_fragment(self):
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","fragment":"<>\^`{|}"})


if __name__ == '__main__':
    unittest.main()
