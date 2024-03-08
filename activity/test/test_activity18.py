from activity.activity18 import modify_bytearray

def test_modify_bytearray_valid_index():
    input_list = [65, 66, 67, 68]
    index = 2
    new_value = 69
    result = modify_bytearray(input_list, index, new_value)
    assert result == bytearray([65, 66, 69, 68])

def test_modify_bytearray_invalid_index():
    input_list = [65, 66, 67, 68]
    index = 5
    new_value = 69
    result = modify_bytearray(input_list, index, new_value)
    assert result is None

def test_modify_bytearray_negative_index():
    input_list = [65, 66, 67, 68]
    index = -2
    new_value = 69
    result = modify_bytearray(input_list, index, new_value)
    assert result is None

def test_modify_bytearray_empty_list():
    input_list = []
    index = 0
    new_value = 69
    result = modify_bytearray(input_list, index, new_value)
    assert result is None
