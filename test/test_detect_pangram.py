from src.detect_pangram.detect_pangram import detect_pangram

def test_returns_a_boolean():
    input = 'Hello'
    expected = bool
    result = type(detect_pangram(input))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_false_for_a_word():
    input = 'Hello'
    expected = False
    result = detect_pangram(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_true_for_a_pangram():
    input = "The quick brown fox jumps over the lazy dog."
    expected = True
    result = detect_pangram(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_false_for_not_a_pangram():
    input = "The brown fox jumps over the lazy dog."
    expected = False
    result = detect_pangram(input)
    print(f"Result is: {result}")
    assert expected == result