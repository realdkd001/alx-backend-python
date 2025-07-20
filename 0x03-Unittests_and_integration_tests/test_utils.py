#!/usr/bin/env python3
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2 )
    ])
    def test_access_nested_map(self, nested_map, path, expected ):
        self.assertEqual(access_nested_map(nested_map, path), expected)
        
    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path))


class TestGetJson(unittest.TestCase):
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True} ),
            ("http://holberton.io", {"payload": False} )
        ]
    )
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_json_response = MagicMock()
        mock_json_response.json.return_value = test_payload
        mock_get.return_value = mock_json_response
        res = get_json(test_url)
        self.assertEqual(res, test_payload)