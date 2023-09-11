import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets for the password
    characters = string.ascii_letters  # Letters (both uppercase and lowercase) are always included

    if use_digits:
        characters += string.digits  # Include digits (0-9)

    if use_special_chars:
        characters += string.punctuation  # Include special characters

    # Generate the password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))

    return password

# Example usage:
if __name__ == "__main__":
    password_length = 16  # You can change the desired password length
    include_digits = True  # Set to False if you don't want digits in the password
    include_special_chars = True  # Set to False if you don't want special characters

    generated_password = generate_password(
        length=password_length,
        use_digits=include_digits,
        use_special_chars=include_special_chars
    )

    print("Generated Password:", generated_password)
