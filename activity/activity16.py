def find_intersection(set1, set2):
    return set1.intersection(set2)


if __name__ == '__main__':
    try:
        set1_input = input("Enter the first set (format: {1, 2, 3}): ")
        set2_input = input("Enter the second set (format: {3, 4, 5}): ")

        set1 = set(eval(set1_input))
        set2 = set(eval(set2_input))
        intersection_result = find_intersection(set1, set2)
        print("\nResults:")
        print(f"First set: {set1}")
        print(f"Second set: {set2}")
        print(f"Intersection of the sets: {intersection_result}")

    except (SyntaxError, TypeError):
        print("Invalid input. Please enter valid sets ")
