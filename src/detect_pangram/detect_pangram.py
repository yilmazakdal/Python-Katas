def detect_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower_string = string.lower()
    for letter in alphabet:
        if letter not in lower_string:
                return False
    return True
    
            
    
	
