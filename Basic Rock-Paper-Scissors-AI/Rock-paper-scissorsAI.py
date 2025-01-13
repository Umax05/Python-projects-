import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user_input in choices:
            return user_input
        elif user_input == 'quit':
            return 'quit'
        else:
            print("Invalid input. Please try again.")

def get_ai_choice():
    return random.choice(choices)

def determine_winner(user, ai):
    if user == ai:
        return "It's a tie!"
    elif (
        (user == 'rock' and ai == 'scissors') or
        (user == 'paper' and ai == 'rock') or
        (user == 'scissors' and ai == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    ai_score = 0
    ties = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break

        ai_choice = get_ai_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {ai_choice}")

        result = determine_winner(user_choice, ai_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            ai_score += 1
        else:
            ties += 1

        print(f"Scores => You: {user_score}, Computer: {ai_score}, Ties: {ties}\n")

    print("\nThanks for playing!")
    print(f"Final Scores => You: {user_score}, Computer: {ai_score}, Ties: {ties}")

if __name__ == "__main__":
    play_game()