from activity.activity5 import right_rotate_list

def test_right_rotate_list_empty_list():
    input_list = []
    rotation = 3
    result = right_rotate_list(input_list, rotation)
    assert result == "error"

def test_right_rotate_list_single_element():
    input_list = [42]
    rotation = 2
    result = right_rotate_list(input_list, rotation)
    assert result == [42]

def test_right_rotate_list_rotation_greater_than_length():
    input_list = [1, 2, 3, 4, 5]
    rotation = 7
    result = right_rotate_list(input_list, rotation)
    assert result == [4, 5, 1, 2, 3]

def test_right_rotate_list_rotation_equal_to_length():
    input_list = [1, 2, 3, 4, 5]
    rotation = 5
    result = right_rotate_list(input_list, rotation)
    assert result == [1, 2, 3, 4, 5]

def test_right_rotate_list_mixed_data_types():
    input_list = ['a', 'b', 'c', 'd', 'e']
    rotation = 2
    result = right_rotate_list(input_list, rotation)
    assert result == ['d', 'e', 'a', 'b', 'c']

def test_right_rotate_list_negative_rotation():
    input_list = [10, 20, 30, 40, 50]
    rotation = -2
    result = right_rotate_list(input_list, rotation)
    assert result == [30, 40, 50, 10, 20]
