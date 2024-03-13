def find_most_repeated(lst):
    if not lst:
        return {'elements': [], 'repeats': None}
    
    counts = {}
    max_count = 0
    most_repeated = []

    for element in lst:
        counts[element] = counts.get(element, 0) + 1
        if counts[element] > max_count:
            max_count = counts[element]
            most_repeated = [element]
        elif counts[element] == max_count:
            most_repeated.append(element)

    if max_count <= 1:
        return {'elements': [], 'repeats': None}
    else:
        return {'elements': most_repeated, 'repeats': max_count}




    
