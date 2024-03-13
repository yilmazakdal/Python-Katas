def count_bits(integer):
    binary = bin(integer)
    stripped_binary = binary.lstrip('-0b')
    print(stripped_binary)
    string_stripped_binary = str(stripped_binary)
    bit_counter = 0
    for char in string_stripped_binary:
        if char == '1':
            bit_counter += 1
    return bit_counter