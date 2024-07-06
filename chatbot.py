import random

def greet():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    return random.choice(greetings)

def chatbot_response(user_input):
    user_input = user_input.lower()
    greetings = ['hello', 'hi', 'hey', 'hola', 'greetings']
    if user_input in greetings:
        return greet()
    else:
        return "Sorry, I didn't understand that."

def main():
    print("Chatbot: " + greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'what is the day today?':
            print("Chatbot: saturday")

        elif user_input.lower() == 'what is your name?':
            print("Chatbot: my name is chatai")

        elif user_input.lower() == 'when was this chatai created?':
            print("Chatbot: Today")
        
        elif user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: " + chatbot_response(user_input))

if __name__ == "__main__":
    main()
