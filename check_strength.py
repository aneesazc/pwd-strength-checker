# Strength Checking:Define a set of rules or scoring mechanisms for determining password strength:
# Length of the password.
# Inclusion of uppercase and lowercase letters.
# Inclusion of numbers.
# Presence of special characters.

def load_common_passwords(file_path):
    """Load a set of common passwords from a text file."""
    with open(file_path, 'r') as file:
        # Read all lines and strip whitespace
        passwords = set(line.strip() for line in file)
    return passwords

common_passwords = load_common_passwords('common_passwords.txt')


def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1
    if password not in common_passwords:
        score += 1
    return score