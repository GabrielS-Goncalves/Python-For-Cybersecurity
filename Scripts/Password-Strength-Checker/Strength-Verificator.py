# Goal:
# Make a code for check the strength of passwords.
# Return: Weak, Okay, Good and Strong.

# Packages block
import string
from time import sleep

# Presentation block
print('''
-------------------------------------
|             Welcome!              |
|     Password Strength Checker.    |
|        Type your password...      |
|        By Gabriel Gonçalves       |
-------------------------------------
''')
sleep(1)

UserPassword = input("Give me your password: ")

# Common Password Checker block
def CheckCommonPassword(UserPassword):
    with open('common-password.txt', 'r') as f:
        common = f.read().splitlines()
    if UserPassword in common:
        return True
    return False

# Strength Password Checker block
def CheckPasswordStrength(UserPassword):
    score = 0
    length = len(UserPassword)

    upper_case = any(c.isupper() for c in UserPassword)
    lower_case = any(c.islower() for c in UserPassword)
    special = any(c in string.punctuation for c in UserPassword)
    digits = any(c.isdigit() for c in UserPassword)

    characters = [upper_case, lower_case, special, digits]

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    score += sum(characters) - 1

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score

# Strength Feedback block
def StrengthFeedback(UserPassword):
    if CheckCommonPassword(UserPassword):
        return "Password was found in a common list. Score: 0/7"

    strength, score = CheckPasswordStrength(UserPassword)

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Suggestions to improve your password:\n"
        if len(UserPassword) <= 8:
            feedback += "- Make your password longer (more than 8 characters). \n"
        if not any(c.isupper() for c in UserPassword):
            feedback += "- Include uppercase letters.\n"
        if not any(c.islower() for c in UserPassword):
            feedback += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in UserPassword):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in UserPassword):
            feedback += "- Add numbers.\n"

    return feedback

#print(CheckCommonPassword(UserPassword))
#print(CheckPasswordStrength(UserPassword))
print(StrengthFeedback(UserPassword))
