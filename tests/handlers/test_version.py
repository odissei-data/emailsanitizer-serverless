import unittest

from src.handlers.version import return_version


class VersionTestCase(unittest.TestCase):

    def test_version(self):
        result = return_version()
        assert result == {"version": "serverless 0.1.0"}
