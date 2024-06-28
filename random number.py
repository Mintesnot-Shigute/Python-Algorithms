import random


def guess_number():
    print("Welcome to the Number Guessing Game!")
##
    while True:
        secret_number = random.randint(1, 100)
        attempts = 0

        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()

        if difficulty not in ['easy', 'medium', 'hard']:
            print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")
            continue

        if difficulty == 'easy':
            max_attempts = 10
        elif difficulty == 'medium':
            max_attempts = 7
        else:
            max_attempts = 5

        print(f"\nYou have {max_attempts} attempts to guess the number between 1 and 100.")

        while attempts < max_attempts:
            user_input = input("Enter your guess: ")

            try:
                user_guess = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        if attempts == max_attempts and user_guess != secret_number:
            print(f"\nGame over! You reached the maximum attempts. The correct number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break


def main():
    guess_number()


if __name__ == "__main__":
    main()
