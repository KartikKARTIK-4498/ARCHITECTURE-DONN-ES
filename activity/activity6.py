def tuple_with_most_elements(list_of_tuples):
    if not list_of_tuples:
        return None 

    max_length = 0
    max_tuple = None

    for tpl in list_of_tuples:
        if len(tpl) > max_length:
            max_length = len(tpl)
            max_tuple = tpl

    return max_tuple

if __name__ == '__main__':
    tuples_input = input("Enter a list of tuples (e.g., (1, 2, 3), ('a', 'b')): ")
    list_of_tuples = eval(tuples_input)
    result = tuple_with_most_elements(list_of_tuples)
    print("List of tuples:", list_of_tuples)
    print("Tuple with the most elements:", result)