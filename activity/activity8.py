import random


def guess_the_number():
    try:
        secret_number = random.randint(1, 100)
        max_attempts = 5
        attempts = 0
        print("Welcome to the Guess the Number game!")
        print("Guess the mystery number b/w 1 and 100")
        print(f"You have {max_attempts} attempts.")

        while attempts < max_attempts:
            try:
                user_guess = int(input("Enter your guess: "))
                if user_guess == secret_number:
                    print("Congratulations! You guessed!")
                    print(f"the correct number {secret_number}!")

                    return True
                elif user_guess < secret_number:
                    print("Try a larger number.")
                else:
                    print("Try a smaller number.")

                attempts += 1
                remaining_attempts = max_attempts - attempts
                print(f"You have {remaining_attempts} attempts remaining.\n")

            except Exception as e:
                raise Exception(f"Attempt {attempts}, {e}")

    except Exception as e:
        return f"error: {e}"

    else:
        print(f"Sorry,The correct number was {secret_number}.")
        return False


if __name__ == "__main__":
    guess_the_number()
