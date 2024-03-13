from src.count_bits.count_bits import count_bits

def test_returns_the_number_of_1s_from_binary ():
    input = 9
    expected = 2
    result = count_bits(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_number_of_1s_from_binary_from_larger_input ():
    input = 1234
    expected = 5
    result = count_bits(input)
    print(f"Result is: {result}")
    assert expected == result