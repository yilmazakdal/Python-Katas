from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case)

# make unit-test test_run=test/test_sentence_to_camel_case.py

def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_single_word_if_false():
    expected = 'this'
    result = sentence_to_camel_case('this', False)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_multiple_words_if_true():
    expected = "ThisSentence"
    result = sentence_to_camel_case('this sentence',True)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_multiple_words_if_false():
    expected = "thissentence"
    result = sentence_to_camel_case('this sentence',False)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_multiple_words_if_true():
    expected = "ThisBiggerStrangeSentence"
    result = sentence_to_camel_case('This Bigger strange Sentence',True)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_multiple_all_capital_words_if_true():
    expected = "WhyAreYouYelling"
    result = sentence_to_camel_case('WHY ARE YOU YELLING',True)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_a_multiple_words_with_numbers_if_true():
    expected = "These1Include2Numbers3"
    result = sentence_to_camel_case('these 1 include 2 numbers 3',True)
    print(f'Result is: {result}')
    assert result == expected



   