def calculate_binary_score(list):
    """
    Calculate the binary score based on the given list of numbers.
    Parameters:
    lst (list): A list of numbers.
    Returns:
    str: The result indicating whether odds win, evens win, or it’s a tie.
    """
    odd_counter = sum(1
                      for num in list if num % 2 == 1
                      for char in str(binary_function(num))
                      if char == '1')
    even_counter = sum(1
                       for num in list
                       if num % 2 == 0
                       for char in str(binary_function(num))
                       if char == '0')
    if odd_counter > even_counter:
        return 'odds win'
    elif even_counter > odd_counter:
        return "evens win"
    else:
        return "tie"
def binary_function(number):
    return bin(number).lstrip('-0b')
