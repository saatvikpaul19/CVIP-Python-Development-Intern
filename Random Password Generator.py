import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    if not any([use_uppercase, use_lowercase, use_digits, use_special_chars]):
        return "Please select at least one character type."

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        return "No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))

    if use_uppercase and any(c.isupper() for c in password) and use_digits and any(c.isdigit() for c in password) and use_special_chars and any(c in string.punctuation for c in password):
        return password
    else:
        return generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    print("Generated Password:", password)