from src.years_of_growth.years_of_growth import (years_of_growth)

def test_returns_an_integer():
    expected = int
    result = type(years_of_growth(1000, 2000, 2, 12))
    print(f'Result is: {result}')
    assert result == expected

def test_returns_correct_number_of_years_to_reach_target():
    expected = 25
    result = years_of_growth(1000, 2000, 2, 12)
    print(f'Result is: {result}')
    assert result == expected

def test_with_little_growth_rate_and_no_migration():
    expected = 10
    result = years_of_growth(1000, 1100, 1, 0)
    print(f'Result is: {result}')
    assert result == expected