from src.traverse_students.traverse_students import find_partner

def test_returns_a_list():
    expected = list
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['right']
    result = type(find_partner(students,directions))
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_to_the_right():
    expected = ['David']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['right']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_to_the_left():
    expected = ['Verity']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['left']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_to_the_right_and_left():
    expected = ['Joe']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['right','left']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_to_the_right_and_two_left():
    expected = ['Verity']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['right','left','left']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_to_the_six_right():
    expected = ['Joe']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['right','right','right','right','right','right']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_to_the_seven_right():
    expected = ['David']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity']]
    directions = ['right','right','right','right','right','right','right']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_one_down():
    expected = ['Hev']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity'],
                ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan']]
    directions = ['down']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_one_up():
    expected = ['Joe']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity'],
                ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan']]
    directions = ['up']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_different_directions():
    expected = ['Alex']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity'],
                ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan'],
                ['Joe', 'Jack', 'William', 'James',  'Yilmaz', 'Simon']]
    directions = ['down','right','right','up']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result
def test_returns_the_student_from_multiple_rows_with_different_directions():
    expected = ['Alex']
    students = [['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity','Jim'],
                ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan','Jane'],
                ['Joe', 'Jack', 'William', 'James',  'Yilmaz', 'Simon','Doe']]
    directions = ['down','right','right','up']
    result = find_partner(students,directions)
    print(f"Result is: {result}")
    assert expected == result