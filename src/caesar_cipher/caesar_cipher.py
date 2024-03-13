def caesar(string, number):
    new_string = ''
    for letter in string:
        if letter.isalpha():
            new_string += chr((ord (letter) + number))
        else:
            new_string += letter  
    return new_string
