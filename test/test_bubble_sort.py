from src.bubble_sort.bubble_sort import (bubble_sort)

def test_return_new_list_when_single_number_is_given ():
    expected = [6]
    result = bubble_sort([6])
    print(f"Result is: {result}")
    assert expected == result
def test_return_new_list_when_two_numbers_are_given ():
    expected = [1,2]
    result = bubble_sort([2,1])
    print(f"Result is: {result}")
    assert expected == result
def test_return_new_list_when_more_than_two_numbers_are_given ():
    expected = [1,2,3,6]
    result = bubble_sort([2,1,3,6])
    print(f"Result is: {result}")
    assert expected == result
def test_return_new_list_when_negative_number_is_given ():
    expected = [-3,1,2,6]
    result = bubble_sort([2,1,-3,6])
    print(f"Result is: {result}")
    assert expected == result
def test_return_new_list_when_big_numbers_are_given ():
    expected = [50000,80000,100000,200000]
    result = bubble_sort([50000,200000,100000,80000])
    print(f"Result is: {result}")
    assert expected == result
def test_return_new_list_when_a_lot_of_numbers_are_given ():
    expected = [2,3,4,5,6,7,8,9,11,12,17,23,41]
    result = bubble_sort([4,8,3,5,9,12,11,7,6,23,17,41,2])
    print(f"Result is: {result}")
    assert expected == result