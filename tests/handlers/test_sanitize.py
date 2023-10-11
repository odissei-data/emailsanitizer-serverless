import unittest

from src.handlers.sanitize import sanitize


class SanitizeTestCase(unittest.TestCase):


    def test_sanitize_success(self):
        test_string = "This string contains a test@email.com"
        replacement = "<omitted>"
        result = sanitize(test_string, replacement)
        assert result == 'This string contains a <omitted>'

    def test_sanitize_no_email_found(self):
        test_string = "This string contains no test-at-email.com"
        replacement = "<omitted>"
        result = sanitize(test_string, replacement)
        assert result == 'This string contains no test-at-email.com'
