Password Strength Assessment

Introduction
This script assesses the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters.

Usage
1. Run the script.
2. Enter your desired password.

Features
- Calculates the strength of a password based on length and character composition.
- Provides feedback on password strength, suggesting improvements if necessary.

Functions
1. assess_password_strength(password): Evaluates the strength of the provided password.
2. password_feedback(password): Provides feedback on the strength of the password.

Example Usage
password = input("Enter your password: ")
feedback = password_feedback(password)
print(feedback)

Requirements
- Python 3.x
- Regular Expression (re module)
