# Update this text to match your story.
start = '''
You wake up and find that you aren't in the bed that you had fallen alseep in only hours ago;
the world around you that you have been so used to has vanished.
The world around gives off an aura of mysticality and wonder.
You close your eyes again and pinch yourself to find a way to wake up from this dream that seems all to real.
"Hey! Hey you! Are you alright?!" A voice comes from above and you open your eyes to look at a human-like creature standing above you.
"Thank the gods, YOU'RE ALIVE!"
He had bluish-black hair tied back, fair skin, and eyes that shine like the moon.
"Welcome to Astratera, a magical mystical world filled with power that exceeds other realms. My name Sebastian. You are not from around here, are you?"
'''

print(start)

print("Type 'yes' to nod head or 'no' to shake head.") # Update to match your story. 
user_input = input()
if user_input == "yes":
    story1 = '''
     "Oh, so you must need help!"
    You nod head even more rapidly.
    "Okay, so you must know that there are goblins, orcs, and so MANY OTHER DANGEROUS THINGS"
    Your eyes widen in fear. "But don't worry, I'll be here to guide and to help you..... PICK A WEAPON!!!!"
    '''
    print("You nod your head to say yes.") # Update to match your story.
    print(story1)
elif user_input == "no":
    print("You shook your head to say no.") # Update to match your story.
    story2 = '''          
    "Oh, well then you don't need my help after all. Adios!"
    Sebastian skips away happily as you sit on the cold hard floor, watching him leave farther and farther away from you.
    You are now left alone in this realm forever
    GAME OVER.
    '''
print(story2)

print("Type 'a' to obtain a sword or 'b' to a bow and arrows.")
user_input = input()
if user_input == "a":
     print("You obtain Shadowsteel, a powerful sword with a dark history.")
storya = '''
    You fight many monsters and then eventually become evil.
    GAME OVER
'''
print(storya)
if user_input == "b":
    print("You obtain Courier, Kiss of Dismay.")
storyb = '''
    "Yes, that's a wonderful choice! It truly is a beautiful weapon!" He fawns over the weapon with his eyes wide.
    Many years go by, you fight many monsters and bring goodness back to this realm with your weapon. One day, you come across a portal that can take you back home.
'''
print(storyb)
print("Type 'stay' to stay here or 'leave' to go back home.")
user_input = input()
if user_input == "stay":
    print("You have chosen to stay in this world of magic and power. game end")
elif user_input == "leave":
        print("You have chosen to leave and you woke up in your bed, back in your warm home, it's only the morning after the last. game end")
    # Continue code to finish story.
 
