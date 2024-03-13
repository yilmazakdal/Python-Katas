def digital_root(num):
    stringified = str(num)
    # "123"
    splitted = list(stringified)
    # ['1','2','3']
    total = 0
    for number in splitted:
        total += int(number)
    if total>= 10:
        return digital_root(total)
    return total

  