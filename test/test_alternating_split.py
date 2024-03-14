from src.alternating_split.alternating_split import encrypt
def test_returns_a_string():
    input_1 = "012345"
    input_2 = 1
    expected = str
    result = type(encrypt(input_1, input_2))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_simple_encrypted_result():
    input_1 = "012345"
    input_2 = 1
    expected = "135024"
    result = encrypt(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_simple_encrypted_result_twice():
    input_1 = "012345"
    input_2 = 2
    expected = "304152"
    result = encrypt(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_simple_encrypted_result_three_times():
    input_1 = "012345"
    input_2 = 3
    expected = "012345"
    result = encrypt(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result