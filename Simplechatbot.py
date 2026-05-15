print("Simple Chatbot")

while True:
    user=input("You: ")
    
    if user.lower()=="hello":
        print("Bot: Hi")
    
    elif user.lower()=="how are you":
        print("Bot: I am fine")
        
    elif user.lower()=="bye":
        print("Bot: Goodbye")
        break
    
    else:
        print("Bot: Sorry, I don't understand")