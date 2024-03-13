def herd_the_babies(string):
    string_letter_list = list(string)
    sorted_string_letter_list = sorted(string_letter_list, key=lambda x: (x.upper(), x))
    result = ''.join(sorted_string_letter_list)
    return result