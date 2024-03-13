from src.create_counter.create_counter import(create_counter)

def test_increases_number():
    expected = 6
    counter = create_counter(5)
    up = counter['up']
    result= up()
    print(f'Result is: {result}')
    assert result == expected
def test_decreases_number():
    expected = 4
    counter = create_counter(5)
    down = counter['down']
    result= down()
    print(f'Result is: {result}')
    assert result == expected
def test_decreases_number_twice():
    expected = 3
    counter = create_counter(5)
    down = counter['down']
    down()
    result= down()
    print(f'Result is: {result}')
    assert result == expected
def test_increases_number_twice():
    expected = 7
    counter = create_counter(5)
    up = counter['up']
    up()
    result= up()
    print(f'Result is: {result}')
    assert result == expected
def test_increases_then_decreases_number():
    expected = 5
    counter = create_counter(5)
    up = counter['up']
    down =counter['down']
    up()
    result= down()
    print(f'Result is: {result}')
    assert result == expected