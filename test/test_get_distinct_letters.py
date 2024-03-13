from src.get_distinct_letters.get_distinct_letters import (
    get_distinct_letters)

def test_returns_two_strings_when_they_are_different():
    expected = 'dk'
    result = get_distinct_letters('k','d')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_empty_string_when_they_are_same():
    expected = ''
    result = get_distinct_letters('a','a')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_unique_letters_when_there_are_two_words():
    expected = 'dehrw'
    result = get_distinct_letters('hello', 'world')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_unique_letters_when_words_are_capital():
    expected = 'DEHRW'
    result = get_distinct_letters('HELLO', 'WORLD')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_when_numbers_included():
    expected = '12dehrw'
    result = get_distinct_letters('hel3lo2', 'wo3rl1d')
    print(f'Result is: {result}')
    assert result == expected