import random

def guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 0
        print("\nI'm thinking of a number between 1 and 100.")

        while True:
            guess = input("Enter your guess (or 'q' to quit): ")
            if guess.lower() == 'q':
                print("Thanks for playing! Goodbye!")
                return  

            try:
                guess = int(guess)
                attempts += 1
            except ValueError:
                print("Invalid input! Please enter a number or 'q' to quit.")
                continue

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    guessing_game()
