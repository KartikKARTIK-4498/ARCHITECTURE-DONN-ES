def right_rotate_list(input_list, rotation):
    try:
        length = len(input_list)
        rotation = rotation % length
        rotated_list = input_list[-rotation:] + input_list[:-rotation]
        return rotated_list
    except:
        return "error"

if __name__ == '__main__':
    input_list = input("Enter a list of numbers (separated by spaces): ").split()
    input_list = [int(num) for num in input_list]
    rotation = int(input("Enter the number of positions to right-rotate: "))
    rotated_result = right_rotate_list(input_list, rotation)
    print("Original list:", input_list)
    print("Right-rotated list:", rotated_result)
