import math
import random 

#consts
USER = None
ENDEARMENT = 5

choice = None
date = None

print(
'''Hello there! Welcome to the Dating Game!
You have been given the chance to find true love. 
You must pick one of 3 hearthrobs , and then embark on a romantic date.
Your choices matter, they each have their own preferences, and lady luck is always watching!
''')

print(
    '''
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀

''')

USER = input("Please enter your name:")

print(
f'''Pleased to make your acquaintance {USER}\n
The dating world is a tempestuous place, but you're on the hunt for love.
There are 3 potential star crossed lovers on the horizon. You've matched with all 3, so lets get to know them!
''')

input("Are you ready to meet the first match? y/n :")

print('''
Henrietta\n

Profile : 
Henrietta is a 25 year old college student at Trinity College , currently completing her masters in computer science.
She doesn’t enjoy sports or dancing, she prefers long walks with a good podcast.
Henrietta likes reading science fiction novels and playing videogames.
She considers herself introverted but has a few close friends.
She doesn’t like people who are too silly or don’t take themselves seriously.
She likes people who are honest with her. She doesn’t drink alcohol but loves to drink coffee.
Henrietta is a vegetarian and her favourite food is Chana Masala.
''')

input("Are you ready to meet the second match? y/n :")

print('''
Francis:

Profile:
Francis is a 29 year old barman who works in a busy pub in Dublin city. He loves to work out at the gym and goes for a run every day. He’s not really into reading but likes playing multiplayer videogames. Francis considers himself an extrovert and likes to spend his free time hanging out with his friends. Francis likes getting to know people, he likes people who are up for a laugh.  He enjoys watching some sporting events like UFC mixed martial arts and WWE pro wrestling. Francis loves to drink alcohol socially and he enjoys sampling the latest craft beers. His favourite food is Supermacs snack box with chicken and chips. 
''')

input("Are you ready to meet the third match? y/n :")

print('''
Sarah:

Profile:
Sarah is 34 year old marketing consultant who works in Dublin. She like to go cycling on the weekends, but her real love is film and cinema. Sarah has a vast collection of films on dvd, she loves to go the Lighthouse Cinema and IFI Cinema. Her job is time consuming and demanding, although she is outgoing with coworkers, she usually doesn’t have a lot of time for romance or catching up with friends. She isn’t into a lot of sports but will watch the Rugby when its on and support Ireland in the six nations. Sarah likes people who aren’t needy, they respect her autonomy and independence and understand that its ok to have time on your own. Sarah doesn’t go to bars much but she is partial to glass of cabernet sauvignon after a long day of work. She is allergic to shellfish , her favourite food is lasagna.
''')

print(''' 
One of these three captivating individuals could be your one true love! But as cruel as cupid's arrow, you must choose one and forsake the others. Who do you want to go on a date with?
a = Henrietta
b = Francis
c = Sarah
''')



choice = input("Please choose a, b, or c")
print(choice)

if 'a' in choice:
    date = 'Henrietta'
elif 'b' in choice:
    date = 'Francis'
elif 'c' in choice:
    date = 'Sarah'
else:
    print(''' Woops looks like you didn't choose a, b, or c. Not to worry , we will choose for you!''')
    date = 'Sarah'

print(
    f'''The big day is here {USER}! Time to to on our date with {date}''')
