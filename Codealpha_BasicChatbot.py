def chatbot():
    print("Simple Chatbot Started! (type 'bye' to exit)")
    print("Type 'help' to see available commands.\n")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello!")

        elif user == "good morning":
            print("Bot: Good Morning!")

        elif user == "good afternoon":
            print("Bot: Good Afternoon!")

        elif user == "good evening":
            print("Bot: Good Evening!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user in ["who made you", "who created you", "who made u"]:
            print("Bot: I was created using Python.")

        elif user == "what can you do":
            print("Bot: I can chat with you and answer simple questions.")

        elif user == "where are you from":
            print("Bot: I live inside your computer!")

        elif user == "are you a robot":
            print("Bot: Yes, I am a simple chatbot.")

        elif user == "tell me a joke":
            print("Bot: Why did the computer go to school? Because it wanted to improve its bytes!")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "sorry":
            print("Bot: No problem!")

        elif user == "i am sad":
            print("Bot: I hope things get better soon.")

        elif user == "i am happy":
            print("Bot: That's great to hear!")

        elif user == "help":
            print("Bot: You can say hello, how are you, who made you, tell me a joke, thank you, bye and more.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()