#!/usr/bin/env python3


import unittest
import convert_from_json

class TestConvertFromJSON(unittest.TestCase):

    def test_disabled_is_set(self):
        result = convert_from_json.to_urls([{"disabled":"true","domain_name":"test.com"}])
        self.assertEqual(result, "")

    def test_disabled_not_set(self):
        result = convert_from_json.to_urls([{"disabled":False,"domain_name":"test.com"}])
        print(result)
        self.assertEqual(result, "")



if __name__ == '__main__':
    unittest.main()
