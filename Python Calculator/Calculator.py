# calculator.py

def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract two numbers and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide two numbers and return the result. Handle division by zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == '1':
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of division: {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()