import re


def check_password_strength(password):
    """
    Check the strength of a password and return its level.

    Levels:
    - Weak: Less than 6 characters or only letters
    - Moderate: At least 6 characters, contains letters and numbers
    - Strong: At least 8 characters, contains letters, numbers, and special characters
    """
    if len(password) < 6:
        return "Weak"
    if password.isalpha():
        return "Weak"
    if re.match(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{6,}$", password):
        return "Moderate"
    if re.match(
        r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$", password
    ):
        return "Strong"
    return "Weak"


# Run locally for testing
if __name__ == "__main__":
    while True:
        password = input("Enter a password (or type 'exit' to quit): ")
        if password.lower() == "exit":
            break
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")
