def crack_code(code):
    """
    Check if the four most common letters before the brackets in the given code
    are in alphabetical order within the brackets.

    Args:
    code (str): The code string to be checked.

    Returns:
    bool: True if the code is valid, False otherwise.
    """
    
    unique_letters = sorted(set(letter for letter in code[:-6] if letter.isalpha()))
    result = ''.join(unique_letters[:4])
    return result == code[-5:-1]