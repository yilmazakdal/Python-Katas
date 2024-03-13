from src.multiplication_table.multiplication_table import multiplication_table

def test_returns_a_list():
    input = 0
    expected = list
    result = type(multiplication_table(input))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_an_empty_list():
    input = 0
    expected = []
    result = multiplication_table(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_one_times_table():
    input = 1
    expected = [[0, 1], [1, 1]]
    result = multiplication_table(input)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_three_times_table():
    input = 3
    expected = [
  [0, 1, 2, 3],
  [1, 1, 2, 3],
  [2, 2, 4, 6],
  [3, 3, 6, 9]
]
    result = multiplication_table(input)
    print(f"Result is: {result}")
    assert expected == result