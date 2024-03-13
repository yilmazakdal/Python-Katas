from src.caesar_cipher.caesar_cipher import (caesar)

def test_shift_one_letter_up ():
    input = 'd'
    expected = 'e'
    result = caesar(input,1)
    print(f"Result is: {result}")
    assert expected == result
def test_shift_two_letters_up ():
    input = 'dd'
    expected = 'ee'
    result = caesar(input,1)
    print(f"Result is: {result}")
    assert expected == result
def test_shift_two_separate_words_up ():
    input = 'hello world'
    expected = 'ebiil tloia'
    result = caesar(input,-3)
    print(f"Result is: {result}")
    assert expected == result
def test_shift_more_separate_words_up_with_non_alphabetical_letters_in ():
    input = 'hello world5!'
    expected = 'ebiil tloia5!'
    result = caesar(input,-3)
    print(f"Result is: {result}")
    assert expected == result