#!/usr/bin/env python3
"""module to test client.py"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock, MagicMock
from typing import Dict, List, Any


class TestGithubOrgClient(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 response: Dict[str, Any], mock_get_json: MagicMock) -> None:
        """test function"""
        mock_get_json.return_value = response
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, response)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, org_mock: PropertyMock) -> None:
        """test public url"""
        org_mock.return_value = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        client = GithubOrgClient("test-org")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

        org_mock.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get: MagicMock) -> None:
        """test public repos"""
        test_payload = [
            {"name": "first_repo", "license": {"key": "mit"}},
            {"name": "second_repo", "license": {"key": "apache-2.0"}},
            {"name": "third_repo", "license": {"key": "mit"}},
        ]
        mock_get.return_value = test_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as url:
            url.return_value = "https://api.github.com/orgs/test-org/repos"
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            expected = ["first_repo", "second_repo", "third_repo"]

            url.assert_called_once()
            mock_get.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Any],
                         key: str, expected: bool) -> None:
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected)
