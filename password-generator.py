# import libraries
import re
import string
import secrets

# Define a Function, generate_password
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    parameters: length [length of the password to be generated]
                nums: default=1
                special_chars: default = 1
                uppercase: default = 1
                lowercase: default = 1
    Instructions:
        obtain all_characters variable
        Implement a for loop inside while to generate the password

    Constraints:
        The elements in the constraints list should be tuples

    Check constraints:
        The password should at least contain each of the different chars

    Others:
        raw string (r) was used to ensure all characters are treated literally
    """

    # Obtain characters required to generate the password
    digits = string.digits
    letters = string.ascii_letters
    symbols = string.punctuation

    # Combine all characters
    all_characters = digits + letters + symbols

    # loop to create password and check against constraints
    while True:
        # Generate the password
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)
    
        # Define constraints
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'a-z')
            ]
    
        # Checking constraints
        if all(
            constraint <= len(re.findall(pattern, password)) 
            for constraint, pattern in constraints
        ):
            break

    
    return password