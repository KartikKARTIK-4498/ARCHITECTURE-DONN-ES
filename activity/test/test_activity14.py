from activity.activity14 import filter_high_grades

def test_filter_high_grades_empty_dict():
    result = filter_high_grades({})
    assert result == {}

def test_filter_high_grades_no_high_grades():
    students_dict = {"Arjun": 12, "Priya": 14, "Rohan": 13}
    result = filter_high_grades(students_dict)
    assert result == {}

def test_filter_high_grades_some_high_grades():
    students_dict = {"Arjun": 17, "Priya": 14, "Rohan": 19}
    result = filter_high_grades(students_dict)
    assert result == {"Arjun": 17, "Rohan": 19}

def test_filter_high_grades_all_high_grades():
    students_dict = {"Arjun": 18, "Priya": 20, "Rohan": 15}
    result = filter_high_grades(students_dict)
    assert result == {"Arjun": 18, "Priya": 20, "Rohan": 15}
