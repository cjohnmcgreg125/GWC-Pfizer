#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.py","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

for word in f:
    if test_password == word in f:
        print("you have a weak password")
        break
    else:
        print("you have a strong password")
        break
