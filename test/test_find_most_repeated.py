from src.find_most_repeated.find_most_repeated import find_most_repeated

def test_returns_a_dict():
    list = ['Joe',  'David', 'Joe']
    expected = {'elements':['Joe'],'repeats':2}
    result = find_most_repeated(list)
    print(f"Result is: {result}")
    assert expected == result