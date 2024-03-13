from src.get_frequencies.get_frequencies import (get_frequencies)

def test_returns_dict_when_given_one_letter():
    expected = {'a':1}
    result = get_frequencies('a')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_dict_when_given_repetead_letters_in_one_word():
    expected = {'h':1,'e':1,'l':2,'o':1}
    result = get_frequencies('hello')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_dict_when_multiple_words_given():
    expected = {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}
    result = get_frequencies('hello world')
    print(f'Result is: {result}')
    assert result == expected