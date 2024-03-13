from src.alphabet_position.alphabet_position import alphabet_position

def test_returns_the_position_for_one_letter ():
    input = 'b'
    expected = '2'
    result = alphabet_position(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_position_for_one_word ():
    input = 'abc'
    expected = '1 2 3'
    result = alphabet_position(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_position_for_more_than_one_word ():
    input = 'abc def'
    expected = '1 2 3 4 5 6'
    result = alphabet_position(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_position_for_more_than_one_word_with_non_alphabeticals ():
    input = "The sunset sets at twelve o' clock."
    expected = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    result = alphabet_position(input)
    print(f"Result is: {result}")
    assert expected == result