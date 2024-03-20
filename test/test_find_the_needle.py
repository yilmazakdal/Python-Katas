from src.find_the_needle.find_the_needle import find_the_needle

def test_returns_a_list():
    input_1 = {'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp"
        }
    }
}
    input_2 = "hello"
    expected = list
    result = type(find_the_needle(input_1, input_2))
    print(f"Result is: {result}")
    assert expected == result


def test_returns_empty_list_if_needle_is_not_present():
    input_1 = {'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp"
        }
    }
}
    input_2 = "sausages"
    expected = []
    result = find_the_needle(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result

def test_returns_key_location_of_needle_simple():
    input_1 = {'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp"
        }
    }
}
    input_2 = "Northcoders"
    expected = ['name', 'contactDetails.address.office', 'reviews.april.chris', 'reviews.may.louise']
    result = find_the_needle(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result

def test_returns_key_location_of_nested_needle():
    input_1 = {'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp"
        }
    }
}
    input_2 = "Chris"
    expected = ["staff.tutors"]
    result = find_the_needle(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result

def test_returns_key_location_of_nested_needle_again():
    input_1 = {'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp"
        }
    }
}
    input_2 = "Louise"
    expected = ["staff.support"]
    result = find_the_needle(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result

def test_returns_key_location_of_nested_needle_again():
    input_1 = {'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp"
        }
    }
}
    input_2 = "Gold"
    expected = ["contactDetails.address.office"]
    result = find_the_needle(input_1, input_2)
    print(f"Result is: {result}")
    assert expected == result