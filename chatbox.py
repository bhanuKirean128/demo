import random


def greet():
    return "Hello! How can I help you today?"


def respond_to_question(user_input):
    responses = {
        "hi": "Hi nice to meet you!",
        "hello": "Hi! Hello how can i assist you?",
        "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!",
        "your name": "I am a Python chatbot.",
        "default": "I'm sorry, I don't understand that. Can you ask something else?"
    }

    # Convert the input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()

    # Check if the user input matches any predefined questions/commands
    return responses.get(user_input, responses["default"])


def chat():
    print("ellisa: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("ellisa: Goodbye!")
            break

        response = respond_to_question(user_input)
        print("ellisa:", response)


# Start the chatbot
if __name__ == "__main__":
    chat()
