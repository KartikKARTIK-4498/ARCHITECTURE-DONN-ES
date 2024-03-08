def decode_message(encoded_message):
    try:
        numbers = encoded_message.split()
        decoded_message = ''.join(chr(int(num)) for num in numbers)
        return decoded_message

    except:
        return "Invalid"

if __name__ == "__main__":
    encoded_message = input("Enter the encoded message (space-separated ASCII values): ")
    decoded_result = decode_message(encoded_message)
    print("Decoded message:", decoded_result)