from src.justify_line.justify_line import justify_line

def test_returns_string ():
    input_1 = 'foo foo foo foo'
    input_2 = 16
    expected = str
    result = type(justify_line(input_1,input_2))
    print(f"Result is: {result}")
    assert expected == result

def test_returns_string_with_extra_space ():
    input_1 = 'foo foo foo foo'
    input_2 = 20
    expected = 'foo  foo foo foo'
    result = justify_line(input_1,input_2)
    print(f"Result is: {result}")
    assert expected == result
