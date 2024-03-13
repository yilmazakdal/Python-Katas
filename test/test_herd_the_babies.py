from src.herd_the_babies.herd_the_babies import (herd_the_babies)

def test_returns_str_with_capital_first():
    expected = 'Aa'
    result = herd_the_babies('aA')
    assert result == expected

def test_returns_parent_letter_followed_by_child_letter_followed_by_next_parent():
    expected = 'AaB'
    result = herd_the_babies('aBA')
    assert result == expected

def test_returns_parent_letter_followed_by_many_child_letters_followed_by_next_parent():
    expected = 'AaaaaB'
    result = herd_the_babies('aBaaAa')
    assert result == expected

def test_returns_multiple_parent_child_letters():
    expected = 'AaBbbCcc'
    result = herd_the_babies('bbaBccAC')
    assert result == expected