from src.vowel_shift.vowel_shift import vowel_shift

def test_returns_a_list():
    input = 0
    expected = list
    result = type(vowel_shift(input))
    print(f"Result is: {result}")
    assert expected == result