# --- Define your functions below! ---


# --- Put your main program below! ---
print(
'''
Hi! My  name is Anna!
What is your name?
'''
)
name = input() 
print("Hi", name , "nice to meet you!")

def main():
    while True:
        answer = input("Tell me something ")
        if (answer == "hello"):
            print("Hello to you too")
        elif (answer == "bye"):
            print("See you soon")
            break
        else:
            answer = input("Tell me something else.")
main()
