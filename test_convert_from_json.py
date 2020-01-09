#!/usr/bin/env python3


import unittest
import convert_from_json

class TestConvertFromJSON(unittest.TestCase):

    def test_required_field_is_absent(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {})

    def test_disabled_is_set(self):
        result = convert_from_json.to_url({"disabled":True,"domain_name":"test.com"})
        self.assertEqual(result, None)

    def test_disabled_is_not_set(self):
        result = convert_from_json.to_url({"disabled":False,"domain_name":"test.com"})
        self.assertEqual(result, "//test.com")

    def test_disabled_is_not_boolean(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {"disabled":"not boolean","domain_name":"test.com"})

    def test_valid_scheme(self):
        result = convert_from_json.to_url({"domain_name":"test.com","scheme":"http"})
        self.assertEqual(result, "http://test.com")

    def test_scheme_is_invalid(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {"domain_name":"test.com","scheme":"ftp"})

    def test_domain_is_invalid(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {"domain_name":"^"})

    def test_port_is_not_integer(self):
        self.assertRaises(ValueError, convert_from_json.to_url, {"domain_name":"test.com","port":"not a port"})



if __name__ == '__main__':
    unittest.main()
