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
f'''Pleased to make your acquaintance {USER}

The dating world is a tempestuous place, but you're on the hunt for love.
There are 3 potential star crossed lovers on the horizon.
You've matched with all three, so lets get to know them!
''')

input("Are you ready to meet the first match? y/n :")

print('''
Henrietta

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
Francis

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
Sarah

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
a) Henrietta, b) Francis, c) Sarah
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
While it is a little cold,
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

print(
'''
While you both seem in good form , you should decide what to do
a ) go straight to the date venue
b ) go for a stroll in St.Stephens Green Park
c) go for a stroll in the shopping centre , grab coffees
'''
)

first_steps = input("What would you like to do?")

if first_steps == 'a' and weather == rainy:
    print(
    f'''
    Good call, its not nice to be out in this rain, 
    best to get to the venue ASAP.
    {date} might get a bit wet but the weather isn't your fault
    No change to endearment score
    ''')
elif first_steps == 'b' and weather == rainy:
    print(
    f'''
    At your insistence, you and {date} go for a walk in the park.
    It is lashing rain, while you try to make smalltalk.
    {date} is unimpressed by your knowledge of the park's history,
    they seem annoyed and are soaked through to the bone.
    Maybe the park stroll wasn't the best idea...
    Minus 1 point from endearement score
    ''')
    ENDEARMENT -= 1
    print(ENDEARMENT)
elif first_steps == 'c' and weather == rainy:
    print(
    f'''
    You suggest a stroll around the shopping centre, 
    before heading straight to the venue.
    You and {date} grab some take away coffees,
    make small talk and stroll around.
    Its a little awkward but it was a good idea
    to get out of the rain. 
    {date} seems impressed with your initiative
    Plus 1 point to endearement score
    ''')
    ENDEARMENT += 1
    print(ENDEARMENT)
elif first_steps == 'a' and weather == sunny:
    print(
    f'''
    At your insistence, you and {date} head straight for the venue.
    {date} doesn't seem bothered by heading straight there
    but they comment that it seems like it would have been a nice day for a stroll
    No change to endearment score
    ''')
elif first_steps == 'b' and weather == sunny:
    print(
    f'''
    At your insistence, you and {date} go for a walk in the park.
    The sun is shining, while you try to make smalltalk.
    {date} is impressed by your knowledge of the park's history,
    the fresh air and nice weather puts you both in a good mood.
    {date} seems happy you suggested it
    Plus 1 point to endearement score
    ''')
    ENDEARMENT += 1
    print(fENDEARMENT)
elif first_steps == 'c' and weather == sunny:
    print(
    f'''
    You suggest a stroll around the shopping centre, 
    before heading straight to the venue.
    You and {date} grab some take away coffees,
    make small talk and stroll around.
    Its a bit stuffy in the shopping centre unlike outside,
    the weather is so nice and the fresh air is refreshing,
    {date} seems disappointed you're not outdoors
    Minus 1 point from endearment score
    ''')
    ENDEARMENT -= 1
    print(ENDEARMENT)
elif first_steps == 'a' and weather == snowy:
    print(
    f'''
    At your insistence, you and {date} head straight for the venue.
    {date} doesn't seem bothered by heading straight there
    but they comment that it seems like it would have been a nice day for a stroll
    No change to endearment score
    ''')
elif first_steps == 'b' and weather == snowy:
    print(
    f'''
    At your insistence, you and {date} go for a walk in the park.
    Its a bit cold but the gentle snowfall is breathtaking
    {date} is impressed by your knowledge of the park's history,
    the blanket of snow reminds you of christmas
    it puts the both of you in a good mood
    {date} seems happy you suggested the walk in the park
    Plus 1 point to endearement score
    ''')
    ENDEARMENT += 1
    print(ENDEARMENT)
elif first_steps == 'c' and weather == snowy:
    print(
    f'''
    You suggest a stroll around the shopping centre, 
    before heading straight to the venue.
    You and {date} grab some take away coffees,
    make small talk and stroll around.
    Its warm indoors so its a relief from the cold,
    but you're not getting to see much snowfall
    {date} seems disappointed you're not outdoors in the snow
    Minus 1 point from endearment score
    ''')
    ENDEARMENT -= 1
    print(ENDEARMENT)
else:
    print(
    f'''
    At your insistence, you and {date} head straight for the venue.
    {date} doesn't seem bothered by heading straight there
    but they comment that it seems like it would have been nice
    to stroll around or grab a coffee somewhere first
    No change to endearment score
    ''')



