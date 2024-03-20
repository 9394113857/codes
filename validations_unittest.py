import unittest  # Importing the unittest module

# Importing the functions to be tested
from re_validations.validations import validate_email, validate_phone

# Defining a test class that inherits from unittest.TestCase
class TestValidationFunctions(unittest.TestCase):
    
    # Test case for a valid email
    def test_valid_email(self):
        # Asserting that the function returns True for a valid email
        assert validate_email('test@example.com') == True

    # Test case for an invalid email
    def test_invalid_email(self):
        # Asserting that the function returns False for an invalid email
        assert validate_email('invalid_email') == False

    # Test case for a valid phone number
    def test_valid_phone(self):
        # Asserting that the function returns True for a valid phone number
        assert validate_phone('1234567890') == True

    # Test case for an invalid phone number
    def test_invalid_phone(self):
        # Asserting that the function returns False for an invalid phone number
        assert validate_phone('invalid_phone_number') == False

# This block of code is required to execute the tests
if __name__ == '__main__':
    unittest.main()
