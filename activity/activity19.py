def iterate_and_increment(byte_array):
    for i, element in enumerate(byte_array):
        print(f"Element {i + 1}: {element}")
        byte_array[i] += 1


if __name__ == '__main__':
    try:
        input_list_input = input("Enter a list of integers (e.g., 65 66 67): ")
        input_list = [int(num) for num in input_list_input.split()]

        # Create a bytearray from the list
        byte_array = bytearray(input_list)

        # Display and increment the elements of the bytearray
        print("\nResults before increment:")
        iterate_and_increment(byte_array)

        # Display the modified bytearray
        print("\nResults after increment:")
        for i, element in enumerate(byte_array):
            print(f"Modified Element {i + 1}: {element}")

    except ValueError:
        print("Invalid input. Please enter valid integers for the list.")
