from src.extract_domain_name.extract_domain_name import (extract_domain_name)


def test_extract_the_domain_from_basic ():
    input = "https://www.reddit.com/"
    expected = 'reddit.com'
    result = extract_domain_name(input)
    print(f"Result is: {result}")
    assert expected == result
def test_extract_the_domain_with_path ():
    input = "https://github.com/northcoders/de-py-katas"
    expected = 'github.com'
    result = extract_domain_name(input)
    print(f"Result is: {result}")
    assert expected == result
def test_extract_the_domain_with_parameter_value ():
    input = "https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO9Mrw2_v6AhXtTEEAHWYIBi8Q_AUoAXoECAIQAw&biw=1440&bih=764&dpr=2"
    expected = 'google.com'
    result = extract_domain_name(input)
    print(f"Result is: {result}")
    assert expected == result
def test_extract_the_domain_with_different_top_level_domain ():
    input = "https://www.bbc.co.uk/news"
    expected = 'bbc.co.uk'
    result = extract_domain_name(input)
    print(f"Result is: {result}")
    assert expected == result
def test_extract_the_domain_with_different_top_level_domain ():
