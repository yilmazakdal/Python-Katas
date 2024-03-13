from src.fill_square.fill_square import fill_square
def test_returns_a_list():
    input = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    expected = list
    result = type(fill_square(input))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_basic_square_matrix():
    input = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    expected = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]
    result = fill_square(input)
    print(f"Result is: {result}")
    assert len(result) == len(result[0])
    assert len(result) == len(result[1])
    assert len(result) == len(result[2])
def test_returns_basic_square_matrix_by_adding_none():
    input = [[1, 2, 3], [1, 2, 3], [1, 2]]
    expected = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, None]] 
    result = fill_square(input)
    print(f"Result is: {result}")
    assert result == expected
def test_returns_basic_square_matrix_by_adding_multiple_nones():
    input = [[1, 2, 3], [1, 2, 3], [1]]
    expected = [[1, 2, 3],
                [1, 2, 3],
                [1, None, None]]
    result = fill_square(input)
    print(f"Result is: {result}")
    assert result == expected
def test_returns_basic_square_matrix_by_adding_multiple_nones_to_multiple_components():
    input = [[1, 2, 3], [1, 2], [1]]
    expected = [[1, 2, 3],
                [1, 2, None],
                [1, None, None]]
    result = fill_square(input)
    print(f"Result is: {result}")
    assert result == expected
def test_returns_basic_square_matrix_by_adding_multiple_nones_to_multiple_components():
    input = [[1, 2, 3, 4], [1, 2], [1]]
    expected = [[1, 2, 3, 4],
                [1, 2, None, None],
                [1, None, None, None],
                [None, None, None, None]]
    result = fill_square(input)
    print(f"Result is: {result}")
    assert result == expected
def test_returns_basic_square_matrix_by_adding_multiple_nones_to_multiple_components_advanced():
    input = [[1, 2, 3, 4, 5], [1]]
    expected = [[1, 2, 3, 4, 5],
                [1, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]]
    result = fill_square(input)
    print(f"Result is: {result}")
    assert result == expected
def test_returns_basic_square_matrix_by_adding_multiple_nones_to_multiple_components_more_advanced():
    input = [[1, 2, 3, 4, 5]]
    expected = [[1, 2, 3, 4, 5],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]]
    result = fill_square(input)
    print(f"Result is: {result}")
    assert result == expected










