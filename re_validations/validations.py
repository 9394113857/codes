# Import the regular expression module
import re

# Function to validate an email address
def validate_email(email):
    # Define the regex pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # Check if the email matches the pattern
    return re.match(pattern, email) is not None

# Function to validate a 10-digit Indian phone number
def validate_phone(phone):
    # Define the regex pattern for phone number validation
    pattern = r'^\d{10}$'
    # Check if the phone number matches the pattern
    return re.match(pattern, phone) is not None

# Initialize flags for email and phone validation
email_valid = False
phone_valid = False

# Validate email input in a loop until a valid email is provided
while not email_valid:
    # Prompt the user to enter an email address
    email = input("Enter an email address: ")
    # Validate the email address
    if validate_email(email):
        # Set the email_valid flag to True if the email is valid
        email_valid = True
        # Print a confirmation message if the email is valid
        print("Email is valid.")
    else:
        # Print an error message if the email is invalid
        print("Email is invalid. Please try again.")

# Validate phone number input in a loop until a valid phone number is provided
while not phone_valid:
    # Prompt the user to enter a phone number
    phone = input("Enter a phone number (10 digits in Indian format): ")
    # Validate the phone number
    if validate_phone(phone):
        # Set the phone_valid flag to True if the phone number is valid
        phone_valid = True
        # Print a confirmation message if the phone number is valid
        print("Phone number is valid.")
    else:
        # Print an error message if the phone number is invalid
        print("Phone number is invalid. Please try again.")

# Print the final results
print("\nFinal Results:")
print("Email:", email)
print("Phone number:", phone)
