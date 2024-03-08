def modify_bytearray(input_list, index, new_value):
    """Creates a bytearray from a list of integers and modifies one element."""
    byte_array = bytearray(input_list)
    if 0 <= index < len(byte_array):
        byte_array[index] = new_value
        return byte_array
    else:
        return None


if __name__ == '__main__':
    try:
        input_list_input = input("Enter a list of integers (e.g., 65 66 67): ")
        input_list = [int(num) for num in input_list_input.split()]
        index = int(input("Enter the index to modify: "))
        new_value = int(input("Enter the new value: "))
        modified_bytearray = modify_bytearray(input_list, index, new_value)
        if modified_bytearray is not None:
            print("\nResults:")
            print("Original list of integers:", input_list)
            print("Modified bytearray:", modified_bytearray)

    except ValueError:
        print("Invalid input. Please enter valid integers for the list")
