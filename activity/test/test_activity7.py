from activity.activity7 import reverse_tuples_order

def test_reverse_tuples_order_empty_list():
    list_of_tuples = []
    result = reverse_tuples_order(list_of_tuples)
    assert result == []

def test_reverse_tuples_order_single_empty_tuple():
    list_of_tuples = [()]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [()]

def test_reverse_tuples_order_single_tuple():
    list_of_tuples = [(1, 2, 3)]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [(3, 2, 1)]

def test_reverse_tuples_order_multiple_tuples():
    list_of_tuples = [(1, 2), ('a', 'b', 'c'), (True, False, True, False)]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [(2, 1), ('c', 'b', 'a'), (False, True, False, True)]

def test_reverse_tuples_order_mixed_data_types():
    list_of_tuples = [(1, 'two', 3), ('a', 'b', 'c', 'd'), (True, False)]
    result = reverse_tuples_order(list_of_tuples)
    assert result == [(3, 'two', 1), ('d', 'c', 'b', 'a'), (False, True)]
