import unittest
from email_validation import validate_email

class TestEmailValidation(unittest.TestCase):

    def test_valid_emails(self) -> None:
        """
        Test valid email addresses against the email validation rules.
        """
        self.assertTrue(validate_email("user@gmail.com"))
        self.assertTrue(validate_email("user@yahoo.com"))
        self.assertTrue(validate_email("user@outlook.com"))

    def test_invalid_emails(self) -> None:
        """
        Test invalid email addresses against the email validation rules.
        """
        self.assertFalse(validate_email("user@example.com"))
        self.assertFalse(validate_email("user@yopmail.com"))
        self.assertFalse(validate_email("invalidemail"))

if __name__ == '__main__':
    unittest.main()
