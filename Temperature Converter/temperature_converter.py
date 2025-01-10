# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

def display_menu():
    """Display the conversion options."""
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def get_temperature(prompt):
    """Get a valid temperature from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

def main():
    """Main function to run the temperature converter."""
    while True:
        display_menu()
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            celsius = get_temperature("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
        elif choice == '2':
            fahrenheit = get_temperature("Enter temperature in Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        
        elif choice == '3':
            celsius = get_temperature("Enter temperature in Celsius: ")
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C is equal to {kelvin:.2f}K")
        
        elif choice == '4':
            kelvin = get_temperature("Enter temperature in Kelvin: ")
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K is equal to {celsius:.2f}°C")
        
        elif choice == '5':
            fahrenheit = get_temperature("Enter temperature in Fahrenheit: ")
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F is equal to {kelvin:.2f}K")
        
        elif choice == '6':
            kelvin = get_temperature("Enter temperature in Kelvin: ")
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin}K is equal to {fahrenheit:.2f}°F")
        
        elif choice == '7':
            print("Thank you for using the Temperature Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()