from activity.activity16 import find_intersection

def test_find_intersection_empty_sets():
    result = find_intersection(set(), set())
    assert result == set()

def test_find_intersection_empty_set1():
    set2 = {1, 2, 3}
    result = find_intersection(set(), set2)
    assert result == set()

def test_find_intersection_empty_set2():
    set1 = {1, 2, 3}
    result = find_intersection(set1, set())
    assert result == set()

def test_find_intersection_no_intersection():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    result = find_intersection(set1, set2)
    assert result == set()

def test_find_intersection_some_intersection():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = find_intersection(set1, set2)
    assert result == {3, 4}

def test_find_intersection_all_intersection():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = find_intersection(set1, set2)
    assert result == {3, 4}
