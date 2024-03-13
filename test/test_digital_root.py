from src.digital_root.digital_root import digital_root

def test_returns_integer_number ():
    input = 16
    expected = int
    result = type(digital_root(input))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_number_if_number_is_one_digit ():
    input = 6
    expected = 6
    result = digital_root(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_number_if_number_is_more_than_one_digit ():
    input = 345
    expected = 3
    result = digital_root(input)
    print(f"Result is: {result}")
    assert expected == result