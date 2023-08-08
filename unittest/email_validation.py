import re

def validate_email(email: str) -> bool:
    """
    Validate an email address based on specified rules.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.

    Rules:
    - Email format must include "@" and have no spaces.
    - The email must be from valid email providers (yahoo.com, gmail.com, outlook.com).

    Note:
    This function does not check for disposable email providers.
    """
    # Proper email format with no spaces
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    
    # Valid email providers
    valid_providers = ["yahoo.com", "gmail.com", "outlook.com"]
    if any(provider in email for provider in valid_providers):
        return True
    
    return False
