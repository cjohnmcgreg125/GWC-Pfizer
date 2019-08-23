##age = int(input("How old will are you?"))
##
##def yearold():
##    yearsleft = int(100 - age)
##    year100 = int(yearsleft + 2019)
##    print("it is going to be", year100 ,"when you turn 100!")
##yearold()



inputWords = input("Type in a word")

def reverseWords():  
    inputWords = input.split()   
    newword=inputWords[-1::-1]  
    output = ' '.join(inputWords)

reverseWords()

def palindrome():
    if inputWords == newword:
        print(word, "is a palindrome!")
    else:
        print(word, "is NOT a palindrome!")
        
palindrome()
