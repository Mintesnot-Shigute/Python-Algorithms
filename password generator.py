import secrets
import string

def generate_password(length=12, use_digits=True, use_uppercase=True, use_lowercase=True, use_symbols=True):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = int(input("Enter the desired password length: "))
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

generated_password = generate_password(
    length=password_length,
    use_digits=include_digits,
    use_uppercase=include_uppercase,
    use_lowercase=include_lowercase,
    use_symbols=include_symbols
)

print(f"Generated Password: {generated_password}")
