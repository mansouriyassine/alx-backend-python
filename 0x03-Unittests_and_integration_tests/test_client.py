#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import (
    parameterized,
    parameterized_class
)
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        test_payload = {"org": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, org_name)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock,
           return_value="test_org")
    def test_public_repos_url(self, mock_org):
        client = GithubOrgClient("test_org")
        expected_url = "https://api.github.com/orgs/test_org/repos"
        self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock,
           return_value="test_org")
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock,
           return_value="https://api.github.com/orgs/test_org/repos")
    @patch('client.get_json')
    def test_public_repos(
            self, mock_get_json, mock_public_repos_url, mock_org):
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test_org/repos"
        )
        self.assertEqual(repos, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [("org_payload", "repos_payload", "expected_repos", "apache2_repos")]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.get_json')
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def setUp(self):
        self.mock_get_json.side_effect = [self.org_payload, self.repos_payload]

    def test_public_repos(self):
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
