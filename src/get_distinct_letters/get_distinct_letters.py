def get_distinct_letters(str1,str2):
	if str1 == str2:
		return ''
	unique= set(str1).symmetric_difference(set(str2))
	joined_words = ''.join(unique)
	sorted_letters = ''.join(sorted(joined_words))
	return sorted_letters



	
