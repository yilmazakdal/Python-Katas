from src.reduce_by_steps.reduce_by_steps import reduce_by_steps

def test_returns_multiply_function():
    def multiply(num1,num2):
        return num1 * num2
    numbers = [5, 5]
    initial_value = 1
    expected = 25
    result = reduce_by_steps(multiply, numbers, initial_value)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_make_sentence():
    def make_sentence(str1,str2):
        return f"{str1} {str2}"
    words = ['Let\'s', 'get', 'down', 'to', 'business']
    initial_value = ''
    expected = " Let's get down to business"
    result = reduce_by_steps(make_sentence, words, initial_value)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_addition():
    def addition(num1,num2):
        return num1+num2
    list_numbers = [1,2,3,4,5]
    initial_value = 0
    expected = 15
    result = reduce_by_steps(addition, list_numbers, initial_value)
    print(f"Result is: {result}")
    assert expected == result
