def sentence_to_camel_case(arg1, arg2):
    words = arg1.split()
    result = []
    for word in words:
        if arg2:
            capitalised = word[0].upper() + word[1:].lower()
            result.append(capitalised)
        else:
            result.append(word[0].lower()+word[1:])
    return (''.join(result))
