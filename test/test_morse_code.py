from src.morse_code.morse_code import morse_code
def test_returns_a_string():
    input = "...."
    expected = str
    result = type(morse_code(input))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_morse_code_for_a_letter():
    input = "...."
    expected = 'H'
    result = morse_code(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_morse_code_for_a_short_word():
    input = ".... .."
    expected = 'H'
    result = morse_code(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_morse_code_for_a_two_words():
    input = "--. --- --- -..    -- --- .-. -. .. -. --."
    expected = 'GOOD MORNING'
    result = morse_code(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_morse_code_for_a_three_words():
    input = "--. --- --- -..    -- --- .-. -. .. -. --.    -. --- .-. - .... -.-. --- -.. . .-. ..."
    expected = 'GOOD MORNING NORTHCODERS'
    result = morse_code(input)
    print(f"Result is: {result}")
    assert expected == result