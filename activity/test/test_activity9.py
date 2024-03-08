from activity.activity9 import display_pyramid

def test_display_pyramid_height_1():
    result = display_pyramid(1)
    expected_output = "*"
    assert result == expected_output

def test_display_pyramid_height_0():
    result = display_pyramid(0)
    expected_output = None
    assert result == expected_output
