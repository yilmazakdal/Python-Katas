from src.roman_numeral_encoder.roman_numeral_encoder import roman_numeral_encoder

def test_encode_a_number_less_than_10 ():
    input = 2
    expected = 'II'
    result = roman_numeral_encoder(input)
    print(f"Result is: {result}")
    assert expected == result
def test_encode_a_very_big_number ():
    input = 3456
    expected = 'MMMCDLVI'
    result = roman_numeral_encoder(input)
    print(f"Result is: {result}")
    assert expected == result
def test_encode_a_very_big_number ():
    input = 3456
    expected = 'MMMCDLVI'
    result = roman_numeral_encoder(input)
    print(f"Result is: {result}")
    assert expected == result