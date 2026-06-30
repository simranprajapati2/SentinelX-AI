import re

def validate_password(password):


 if len(password) < 8:
    return False, "Password must be at least 8 characters."

 if not re.search(r"[A-Z]", password):
    return False, "Password needs one uppercase letter."

 if not re.search(r"[a-z]", password):
    return False, "Password needs one lowercase letter."

 if not re.search(r"\d", password):
    return False, "Password needs one number."

 if not re.search(r"[!@#$%^&*]", password):
    return False, "Password needs one special character."

 return True, "Strong Password"

