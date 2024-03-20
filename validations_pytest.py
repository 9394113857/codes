import pytest  # Importing the pytest module

# Importing the functions to be tested from the re_validations module
from re_validations.validations import validate_email, validate_phone

# Test case for a valid email address
def test_valid_email():
    # Asserting that the function returns True for a valid email
    assert validate_email('test@example.com') == True

# Test case for an invalid email address
def test_invalid_email():
    # Asserting that the function returns False for an invalid email
    assert validate_email('invalid_email') == False

# Test case for a valid 10-digit Indian phone number
def test_valid_phone():
    # Asserting that the function returns True for a valid phone number
    assert validate_phone('1234567890') == True

# Test case for an invalid phone number
def test_invalid_phone():
    # Asserting that the function returns False for an invalid phone number
    assert validate_phone('invalid_phone_number') == False
