#!/usr/bin/env python3


import unittest
import convert_from_json

class TestConvertFromJSON(unittest.TestCase):

    def test_required_field_is_absent(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {})

    def test_disabled_is_set(self):
        result = convert_from_json.to_url({"disabled":"true","domain_name":"test"})
        self.assertEqual(result, None)

    def test_disabled_is_not_set(self):
        result = convert_from_json.to_url({"disabled":False,"domain_name":"test"})
        self.assertEqual(result, "//test")

    def test_disabled_is_not_boolean(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {"disabled":"not boolean","domain_name":"test"})

    def test_valid_scheme(self):
        result = convert_from_json.to_url({"domain_name":"test","scheme":"http"})
        self.assertEqual(result, "http://test")

    def test_scheme_is_invalid(self):
        self.assertRaises(KeyError, convert_from_json.to_url, {"domain_name":"test","scheme":"ftp"})




if __name__ == '__main__':
    unittest.main()
