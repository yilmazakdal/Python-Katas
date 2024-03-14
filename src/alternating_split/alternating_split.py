def encrypt(str, n):
    new_empty_string = ""
    while n > 0:
        for i, num in enumerate(str):
            if i % 2 == 1:
                new_empty_string += num
        for i, num in enumerate(str):
            if i % 2 == 0:
                new_empty_string += num
        n -= 1
        str = new_empty_string
        new_empty_string = ""
    return str
