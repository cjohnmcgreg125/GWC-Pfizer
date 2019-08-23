print( '''
Welcome to this long, lame ass survey. 
''')
userlist = []

while True:
    
       response = {}
       
       response['1'] = input("1. What is your name?")
       response['2'] = input("2. What is your date of birth? (MM/DD/YYYY)")
       response['3'] = input("3. What is your age?")
       response['4'] = input("4. Where do you call home? (City, State, Country)")
       response['5'] = input("5. How many people live in your home?")
       response['6'] = input("6. How many hours per week do you spend on the phone?")
       response['7'] = input("7. Name the app, program, or website that you use most frequently.")
       response['8'] = input("8. Which would you pick: being world-class attractive, a genius or famous for doing something great?")
       response['9'] = input("9. If you could change one thing about yourself, what would it be?")
       response['10'] = input("10. What's the most beautiful place you've ever been?")
       response['11'] = input("11. Which historical figure would you like to be?")
       response['12'] = input("12. What would you do if you were invisible for a day?")
       response['13'] = input("13.Who would play you in a movie of your life?")
       response['14'] = input("14. If you could be an Olympic athlete, in what sport would you compete?")
       response['15'] = input("15. Cake or pie?")
       response['16'] = input("16. If you could travel anywhere in the world, where would it be?")
       response['17'] = input("17. What fictional character do you wish you could meet?")
       response['18'] = input("18. If you had to pick a new name for yourself, what name would you pick?")
       response['19'] = input("19. Would you rather be the most popular kid in school or the smartest kid in school?")
       response['20'] = input("20. If you could be anywhere else right now, where would it be?")
       response['21'] = input("21. What is your favorite Disney movie?")
       response['22'] = input("22. If someone made a movie of your life would it be a drama, a comedy, a romantic-comedy, action film, or science fiction?")
       userlist.append(response) 

       print(response)
       print(userlist)

       if input("Do you want the program to stop?") == "yes":
           break
       
       
 
