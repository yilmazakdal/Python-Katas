from src.crack_code.crack_code import crack_code
def test_returns_a_boolean():
    input = "ddd-aaa-z-y-x-123(adxy)"
    expected = bool
    result = type(crack_code(input))
    print(f"Result is: {result}")
    assert expected == result

def test_returns_a_true_for_decrypted_input():
    input = "ddd-aaa-z-y-x-123(adxy)"
    expected = True
    result = crack_code(input)
    print(f"Result is: {result}")
    assert expected == result

def test_returns_a_false_for_decrypted_input():
    input = "fff-gg-xx-ss-y(fgsy)"
    expected = False
    result = crack_code(input)
    print(f"Result is: {result}")
    assert expected == result