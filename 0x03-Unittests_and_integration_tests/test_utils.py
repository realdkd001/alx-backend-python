#!/usr/bin/env python3
"""Unit test module for the utils module."""


import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns correct result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError on invalid path."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns expected JSON payload from URL."""
        mock_json_response = MagicMock()
        mock_json_response.json.return_value = test_payload
        mock_get.return_value = mock_json_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches method result after first call."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", 
                          return_value=48) as mock_method:
            obj = TestClass()
            result_1 = obj.a_property
            result_2 = obj.a_property

            self.assertEqual(result_1, result_2)
            self.assertEqual(result_1, 48)
            mock_method.assert_called_once()
            
