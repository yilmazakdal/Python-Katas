from src.lengthen_date.lengthen_date import(lengthen_date)


def test_returns_a_formatted_date():
    expected = 'Tuesday 21st March 2017'
    result = lengthen_date('21.03.2017')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_when_day_less_than_10():
    expected = 'Tuesday 4th October 1977'
    result = lengthen_date('04.10.1977')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_invalid_month():
    expected = 'Invalid date'
    result = lengthen_date('12.40.1977')
    print(f'Result is: {result}')
    assert result == expected
def test_returns_invalid_day():
    expected = 'Invalid date'
    result = lengthen_date('42.08.1977')
    print(f'Result is: {result}')
    assert result == expected