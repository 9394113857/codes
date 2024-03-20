import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None

email_valid = False
phone_valid = False

while not email_valid:
    email = input("Enter an email address:")
    if validate_email(email):
        email_valid = True
        print("Email is valid.")
    else:
        print("Email is invalid, please try again.")



while not phone_valid:
    phone = input("Enter a phone number (10 digits Indian format):")          
    if validate_phone(phone):
        phone_valid = True
        print("Phone is valid.")
    else:
        print("Phone is invalid, please try again.")


# Printing the fianl results
print("\nFinal results:")
print("Email:", email)
print("Phone:", phone)                      

