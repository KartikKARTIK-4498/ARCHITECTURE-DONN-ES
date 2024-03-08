def filter_high_grades(students_dict):
    high_grades_dict = {name: avg_grade for name, avg_grade in students_dict.items() if avg_grade >= 15}
    return high_grades_dict


if __name__ == '__main__':
    try:
        print("Enter a dictionary of students and their average grades ")
        students_input = input("(format: {'Name': grade, ...}): ")
        students_dict = eval(students_input)
        high_grades_result = filter_high_grades(students_dict)
        print("\nResults:")
        print("Original dictionary:", students_dict)
        print("Students with average grades >= 15:", high_grades_result)
    except (SyntaxError, TypeError):
        print("Invalid input. Please enter a valid dictionary format.")
