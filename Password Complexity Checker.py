import re

def assess_password_strength(password):
    score = 0
    
    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    
    # Criteria 2: Uppercase and lowercase letters
    if re.search("[A-Z]", password) and re.search("[a-z]", password):
        score += 1
    
    # Criteria 3: Numbers
    if re.search("[0-9]", password):
        score += 1
    
    # Criteria 4: Special characters
    if re.search("[!@#$%^&*()-_+=]", password):
        score += 1
    
    return score

def password_feedback(password):
    strength_score = assess_password_strength(password)
    
    if strength_score == 0:
        return "Very weak password. Please consider a longer password with a mix of uppercase and lowercase letters, numbers, and special characters."
    elif strength_score == 1:
        return "Weak password. Consider adding more characters and a mix of uppercase and lowercase letters, numbers, and special characters."
    elif strength_score == 2:
        return "Moderate password. It's a good start, but consider adding more characters and a mix of uppercase and lowercase letters, numbers, and special characters."
    elif strength_score == 3:
        return "Strong password! Keep it up, but consider adding a mix of uppercase and lowercase letters, numbers, and special characters for even better security."
    else:
        return "Very strong password! Well done on creating a secure password."

# Example usage
password = input("Enter your password: ")
feedback = password_feedback(password)
print(feedback)
