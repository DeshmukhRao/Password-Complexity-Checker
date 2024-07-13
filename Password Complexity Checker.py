import re

def assess_password_strength(password):
    """
    Assess the strength of a given password based on several criteria.

    Parameters:
    password (str): The password to be assessed.

    Returns:
    str: Feedback on the password's strength.
    """
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count how many criteria are met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Determine strength based on criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Generate feedback message
    feedback = f"Password strength: {strength}\n"
    if not length_criteria:
        feedback += "- Consider making your password longer (at least 8 characters).\n"
    if not lowercase_criteria:
        feedback += "- Add lowercase letters.\n"
    if not uppercase_criteria:
        feedback += "- Add uppercase letters.\n"
    if not digit_criteria:
        feedback += "- Add numbers.\n"
    if not special_char_criteria:
        feedback += "- Add special characters (e.g., !@#$%^&*()).\n"

    return feedback

def main():
    """
    The main function that prompts the user to input a password and assesses its strength.
    """
    password = input("Enter a password to assess its strength: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
