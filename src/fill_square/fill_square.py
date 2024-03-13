def fill_square(list):
    for component in list:
        if len(component) > len(list):
            list.append([None])
            fill_square(list)
        if len(component) != len(list):
            component.append(None)
            fill_square(list)
    return list