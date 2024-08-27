#!/usr/bin/env python3
"""first unit test"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str, ...], expected: Any) -> None:
        """test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                                         path: Tuple[str, ...]) -> None:
        """test exception"""
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ke.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """get json test class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, Any]) -> None:
        """patch requests.get with mock object"""
        with patch("utils.requests.get") as mock_get:
            response = Mock()
            response.json.return_value = test_payload
            mock_get.return_value = response

            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """memoize test class"""
    def test_memoize(self) -> None:
        """test function"""
        class TestClass:
            """memoize class"""

            def a_method(self) -> int:
                """test method"""
                return 42

            @memoize
            def a_property(self) -> int:
                """memoize method"""
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            test = TestClass()

            first = test.a_property
            second = test.a_property

            self.assertEqual(first, 42)
            self.assertEqual(second, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
