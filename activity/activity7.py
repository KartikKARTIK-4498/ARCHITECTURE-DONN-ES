def reverse_tuples_order(list_of_tuples):
    try:
        reversed_list = [tuple(reversed(tpl)) for tpl in list_of_tuples]
        return reversed_list
    except (SyntaxError, TypeError):
        return "error"


if __name__ == "__main__":
    try:
        tuples_input = input("Enter a list of tuples(1, 2, 3): ")
        list_of_tuples = eval(tuples_input)
        reversed_result = reverse_tuples_order(list_of_tuples)
        print("Original list of tuples:", list_of_tuples)
        print("List of tuples with reversed order:", reversed_result)
    except (SyntaxError, TypeError):
        print("Invalid input. Please enter a valid list of tuples.")
