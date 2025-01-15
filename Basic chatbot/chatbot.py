# chatbot.py

def get_bot_response(user_input):
    """
    Returns a response based on user input from a predefined dictionary.
    
    Args:
        user_input (str): The input provided by the user.
    
    Returns:
        str: The chatbot's response.
    """
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm a bot, so I don't have feelings, but thanks for asking!",
        "what is your name": "I'm ChatBot, your virtual assistant.",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure! I can respond to simple greetings and questions. Try asking me 'hello' or 'how are you'.",
        "thank you": "You're welcome! Happy to help!"
    }
    
    cleaned_input = user_input.lower().strip()
    
    if cleaned_input in responses:
        return responses[cleaned_input]
    else:
        return "I'm sorry, I didn't understand that. You can type 'help' to see what I can do."

def main():
    """
    Runs the chatbot application, interacting with the user until they choose to exit.
    """
    print("=== Welcome to ChatBot! ===")
    print("Type 'bye' to exit the conversation.")
    
    while True:
        user_input = input("\nYou: ")
        
        response = get_bot_response(user_input)
        
        print(f"ChatBot: {response}")
        
        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    main()
