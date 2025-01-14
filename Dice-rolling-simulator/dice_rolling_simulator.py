import random

DEFAULT_NUM_DICE = 1
DEFAULT_SIDES = 6

def roll_die(sides=DEFAULT_SIDES):
    """Simulate rolling a single die."""
    return random.randint(1, sides)

def roll_dice(num_dice=DEFAULT_NUM_DICE, sides=DEFAULT_SIDES):
    """Simulate rolling multiple dice."""
    return [roll_die(sides) for _ in range(num_dice)]

def dice_rolling_simulator():
    """Main function to run the Dice Rolling Simulator."""
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            # Get the number of dice from the user
            num_dice_input = input(f"Enter the number of dice to roll (default {DEFAULT_NUM_DICE}): ")
            num_dice = int(num_dice_input) if num_dice_input else DEFAULT_NUM_DICE
            
            # Get the number of sides from the user
            sides_input = input(f"Enter the number of sides per die (default {DEFAULT_SIDES}): ")
            sides = int(sides_input) if sides_input else DEFAULT_SIDES
        except ValueError:
            print("Please enter valid integers for number of dice and sides.\n")
            continue
        
        # Roll the dice and calculate the total
        results = roll_dice(num_dice, sides)
        total = sum(results)
        
        # Display the results
        print(f"\nYou rolled: {results}")
        print(f"Total: {total}\n")
        
        # Ask the user if they want to roll again
        again = input("Do you want to roll again? (y/n): ").lower()
        if again != 'y':
            break
    
    print("Thanks for using the Dice Rolling Simulator! Goodbye!")

if __name__ == "__main__":
    dice_rolling_simulator()