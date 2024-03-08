def out_of_stock_products(product_database):
    out_of_stock_list = [product_id for product_id, product_info in product_database.items() if product_info['quantity'] == 0]

    sorted_out_of_stock = sorted(out_of_stock_list, key=lambda x: (product_database[x]['price'], x), reverse=True)
    return sorted_out_of_stock


if __name__ == '__main__':
    try:
        database_input = input("Enter the product database (format: {1: {'price': 10, 'quantity': 5}, ...}): ")
        product_database = eval(database_input)
        out_of_stock_result = out_of_stock_products(product_database)
        print("\nResults:")
        print("Product database:", product_database)
        print("Out-of-stock products (sorted by price and ID):", out_of_stock_result)

    except (SyntaxError, TypeError):
        print("Invalid input. Please enter a valid product database format.")
