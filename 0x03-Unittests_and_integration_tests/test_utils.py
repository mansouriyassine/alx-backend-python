#!/usr/bin/env python3
import unittest
from parameterized import (
    parameterized
)
from unittest.mock import (
    patch,
    PropertyMock
)
from utils import (
    access_nested_map,
    get_json,
    memoize
)

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, nested_map, path, expected_result
    ):
        self.assertEqual(
            access_nested_map(nested_map, path), expected_result
        )

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_key
    ):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(
            str(context.exception), 
            f"Key '{expected_key}' not found in nested map"
        )

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)

class TestMemoize(unittest.TestCase):
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        instance = self.TestClass()
        instance.a_property()
        instance.a_property()
        mock_a_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
