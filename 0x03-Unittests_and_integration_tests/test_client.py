#!/usr/bin/env python3
"""Unit test module for GithubOrgClient in client.py."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class."""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns expected data.

        Args:
            org_name (str): Name of the organization.
            mock_get_json (Mock): Mocked get_json function.
        """
        expected_payload = {"name": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name)
        )

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns correct repos_url from org.
        """
        test_url = "https://api.github.com/orgs/google/repos"
        org_payload = {"repos_url": test_url}

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, test_url)
