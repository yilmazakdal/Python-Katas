
def get_century(year):
    if year <= 0:
        return 'Invalid year'
    
    if year % 100 == 0:
        century= int(year/100)
    else:
        century = int(year/100) +1

    suffix = suffixes(century)
    return f'{century}{suffix}'

def suffixes(number):
    suffix = ["th", "st", "nd", "rd"]
    if number % 10 in [1, 2, 3] and number not in [11, 12, 13]:
        return suffix[number % 10]
    else:
        return suffix[0]
    




