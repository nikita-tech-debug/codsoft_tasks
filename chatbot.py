print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I am fine! Thank you for asking.")

    elif "your name" in user_input:
        print("Bot: My name is Rule-Based Chatbot.")

    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")