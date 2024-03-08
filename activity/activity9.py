def display_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        return spaces + stars


if __name__ == '__main__':
    try:
        height = int(input("Enter the height of the pyramid: "))
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        display_pyramid(height)

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter +VE.")
