from src.get_century.get_century import(get_century)


def test_returns_when_negative_number_given():
    expected = 'Invalid year'
    result = get_century(-455)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_when_year_ends_with_00():
    expected = '2nd'
    result = get_century(200)
    print(f'Result is: {result}')
    assert result == expected
def test_returns_when_year_not_ending_with_00():
    expected = '21st'
    result = get_century(2001)
    print(f'Result is: {result}')
    assert result == expected