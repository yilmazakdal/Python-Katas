def get_frequencies(word):
	dictionary = {}
	for letter in word:
		if letter != ' ':
			if letter in dictionary:
				dictionary[letter] += 1
			else: 
				dictionary[letter] =1 
	return dictionary
			
    

	
