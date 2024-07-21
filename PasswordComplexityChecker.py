import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[@$!%*?&#]', password) is not None

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])
    
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    feedback = {
        "length_criteria": "Met" if length_criteria else "Not Met",
        "uppercase_criteria": "Met" if uppercase_criteria else "Not Met",
        "lowercase_criteria": "Met" if lowercase_criteria else "Not Met",
        "number_criteria": "Met" if number_criteria else "Not Met",
        "special_character_criteria": "Met" if special_character_criteria else "Not Met",
        "overall_strength": strength
    }
    
    return feedback

# Take password input from the user
password = input("Enter your password: ")
feedback = assess_password_strength(password)

print("\nPassword Strength Feedback:")
for key, value in feedback.items():
    print(f"{key}: {value}")
