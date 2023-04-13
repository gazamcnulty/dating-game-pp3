import math
import random 

#consts
USER = None
ENDEARMENT = 5

choice = None
date = None

print(
'''
 there! Welcome to the Dating Game!
You have been given the chance to find true love. 
You must pick one of 3 hearthrobs , and then embark on a romantic date.
Your choices matter, each date has their own preferences,
and remember, lady luck is always watching!
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

print(
'''
Rules: This is a simple text based game. 
First you will be asked to enter your name. 
From there you will be given info about the dates and scenarios.
You will be offered choices of a, b, or c. 
These choices will decide the outcome of the date.
Please note, if you dont choose a, b, or c , it will default to option c
'''
)

USER = input("Please enter your name:")

print(
f'''Pleased to make your acquaintance {USER}\n
The dating world is a tempestuous place, but you're on the hunt for love.
There are 3 potential star crossed lovers on the horizon.
You've matched with all three, so lets get to know them!
''')

input("Are you ready to meet the first match? y/n :")

print('''
Henrietta\n

Profile : 
Henrietta is a 25 year old college student at Trinity College. 
She is currently completing her masters in computer science.
She doesn’t enjoy sports or dancing. 
She prefers long walks with a good podcast.
Henrietta likes reading science fiction novels and playing videogames.
She considers herself introverted but has a few close friends.
She doesn’t like people who are too silly or don’t take themselves seriously.
She likes people who are honest with her. 
She doesn’t drink alcohol but loves to drink coffee.
Henrietta is a vegetarian and her favourite food is Chana Masala.
''')

input("Are you ready to meet the second match? y/n :")

print(
'''
Francis:

Profile:
Francis is a 29 year old barman who works in a busy pub in Dublin city. 
He loves to work out at the gym and goes for a run every day. 
He’s not really into reading but likes playing multiplayer videogames.
Francis considers himself an extrovert. 
He likes to spend his free time hanging out with his friends. 
Francis likes getting to know people, he likes people who are up for a laugh.  
He enjoys watching some sporting events like UFC MMA and WWE. 
Francis loves to drink alcohol socially. 
He enjoys sampling the latest craft beers. 
His favourite food is Supermacs snack box with chicken and chips. 
''')

input("Are you ready to meet the third match? y/n :")

print(
'''
Sarah:

Profile:
Sarah is 34 year old marketing consultant who works in Dublin.
She like to go cycling on the weekends, but her real love is film and cinema.
Sarah has a vast collection of films on dvd.
She loves to go the Lighthouse Cinema and IFI Cinema. 
Her job is time consuming and demanding, she is friendly with coworkers.
She usually doesn’t have time for romance or catching up with friends.
She isn’t into a lot of sports but will watch the Rugby when its on.
Sarah likes people who aren’t needy.
They need to respect her autonomy and independence.
She understands that its ok to have time on your own.
Sarah doesn’t go to bars much.
She is partial to glass of cabernet sauvignon after a long day of work.
She is allergic to shellfish , her favourite food is lasagna.
''')

print(
''' 
One of these three captivating individuals could be your one true love!
But as cruel as cupid's arrow, you must choose one and forsake the others.
Who do you want to go on a date with?
a = Henrietta
b = Francis
c = Sarah
''')



date_choice = input("Please choose a, b, or c :")
print(choice)

if date_choice == 'a':
    date = 'Henrietta'
elif date_choice == 'b':
    date = 'Francis'
else:
    date = 'Sarah'
print(f"You've chosen to go on a date with {date}!")

print(
'''
We next need to decide when to go on the date.
Do you want to go on the date a) tomorrow , b) the weekend, c) next week?
''')

time_choice = input("Please choose a, b, or c :")

if time_choice == 'a':
    time = 'tomorrow'
elif time_choice == 'b':
    time = 'the weekend'
else:
    time = 'next week'
print(f"You've chosen to go on the date with {date} {time}!")

print(
f'''
The big day is here {USER}! Time to to on our date with {date}!
You have arranged to meet at the luas stop
just outside St.Stepehen's Green Park in Dublin city centre.
''')

rainy = '''
After your initial greetings at the luas stop by St.Stephens Green,
you are struck with torrential rains. 
Neither of you are wearing suitable clothing, 
it might be best to head somewhere close by to get out of the rain.
'''

sunny = '''
After your initial greetings at the luas stop by St.Stephens Green,
the clouds part to reveal a warm sunny skyline.
The sunshine feels good on your face and it puts both of you in a good mood.
No need to rush anywhere , its fine weather for a walk.
'''

snowy = '''
After your initial greetings at the luas stop by St.Stephens Green,
you are met with heavy snow beginning to fall.
While it is cold,
the crunching of snow under your shoes reminds you both fondly of christmas.
Its nice to be outside in the snow, just don’t freeze up!
'''

if time == 'tomorrow':
    weather = rainy
elif time == 'the weekend':
    weather = sunny
else:
    weather = snowy
print(weather)
