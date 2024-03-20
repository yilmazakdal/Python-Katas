from src.calculate_binary_score.calculate_binary_score import calculate_binary_score
def test_returns_a_string():
    input = [1]
    expected = str
    result = type(calculate_binary_score(input))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_odds_win_for_one_odd_number():
    input = [3]
    expected = "odds win"
    result = calculate_binary_score(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_evens_win_for_one_even_number():
    input = [20]
    expected = "evens win"
    result = calculate_binary_score(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_tie_for_one_and_two():
    input = [1, 2]
    expected = "tie"
    result = calculate_binary_score(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_odd_for_multiple_numbers():
    input = [1, 2, 3, 4, 5]
    expected = "odds win"
    result = calculate_binary_score(input)
    print(f"Result is: {result}")
    assert expected == result





