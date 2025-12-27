import re

def check_password_strength(password):
    strength_points = 0

    # Length check
    if len(password) >= 8:
        strength_points += 1

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        strength_points += 1

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        strength_points += 1

    # Number check
    if re.search(r"[0-9]", password):
        strength_points += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1

    # Strength evaluation
    if strength_points <= 2:
        return "Weak Password"
    elif strength_points == 3 or strength_points == 4:
        return "Medium Password"
    else:
        return "Strong Password"


if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print("Password Strength:", result)
