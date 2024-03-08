def add_two_numbers():
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        print("Invalid input. Please enter valid integer numbers.")
        return

    result = num1 + num2

    print("\nResult:")
    print("Sum as integer:", result)
    print("Sum as float:", float(result))
    print("Sum as string:", str(result))
    return result


if __name__ == "__main__":
    add_two_numbers()
