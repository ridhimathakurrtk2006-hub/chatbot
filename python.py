def chatbot():
    print("Hello! I am a simple chatbot. Type 'quit' to exit.")

    while True:
        user_input = input("You: ").lower().strip()  #normalize input

        #exit condition 

        if user_input == "quit":
            print("chatbot: Goodbye! Have a great day!")
            break

        #greeting

        elif "hello" in user_input or "hi" in user_input:
            print("chatbot: Hi there! How can I help you?")

        #asking name

        elif "Your name" in user_input: 
            print("chatbot: I'm a rule-based chatbot created with python. ") 


        #time-related response

        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H : %M : %S") 
            print(f"chatbot: The current time is {current_time}.") 

        #simple math
        
                 