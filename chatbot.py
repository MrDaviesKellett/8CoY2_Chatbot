# simple chatbot

name = input("What should I call you? ")
chatbotName = input("Who am I? ")
print(f"I am {chatbotName}")


# _ means I don't care
for i in range(3): # do something 3 times
    # print(i) # 0, 1, 2

    print(f"I'm asking for the {i + 1} time are you sure your name is {name}?")
    ans = input("")
