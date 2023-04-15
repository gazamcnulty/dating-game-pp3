import time
import os

#consts
USER = None
ENDEARMENT = 5

choice = None
date = None

print(
'''
Hello there! Welcome to the Dating Game!

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
input(" (press any button to continue) :")
os.system('clear')

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
time.sleep(8)
USER = input("Please enter your name:")
os.system('clear')

print(f"Pleased to make your acquaintance {USER}")
time.sleep(4)
os.system('clear')

print(
'''

The dating world is a tempestuous place, but you're on the hunt for love.
There are 3 potential star crossed lovers on the horizon.
You've matched with all three, so lets get to know them!
''')

time.sleep(8)
os.system('clear')
input("Are you ready to meet the first match? (press any button to continue) :")
os.system('clear')

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

input("Are you ready to meet the second match? (press any button to continue) :")
os.system('clear')

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

input("Are you ready to meet the third match? (press any button to continue) :")
os.system('clear')

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

input(" (press any button to continue) :")
os.system('clear')

print(
''' 
One of these three captivating individuals could be your one true love!
But as cruel as cupid's arrow, you must choose one and forsake the others.
Who do you want to go on a date with?
a) Henrietta, b) Francis, c) Sarah
''')


date_choice = input("Please choose a, b, or c :").lower().strip()

if date_choice == 'a':
    date = 'Henrietta'
elif date_choice == 'b':
    date = 'Francis'
else:
    date = 'Sarah'

os.system('clear')
print(f"You've chosen to go on a date with {date}!")
time.sleep(4)
os.system('clear')

print(
'''
We next need to decide when to go on the date.
Do you want to go on the date a) tomorrow , b) the weekend, c) next week?
''')

time_choice = input("Please choose a, b, or c :").lower().strip()

if time_choice == 'a':
    date_time = 'tomorrow'
elif time_choice == 'b':
    date_time = 'this weekend'
else:
    date_time = 'next week'

os.system('clear')
print(
f'''
You've chosen to go on the date with {date} {date_time}!
'''
)
time.sleep(4)
os.system('clear')

print(
f'''
The big day is here {USER}!
Time to to on our date with {date}!
You have arranged to meet at the luas stop
just outside St.Stepehen's Green Park in Dublin city centre.
''')
time.sleep(10)
os.system('clear')

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

if date_time == 'tomorrow':
    weather = rainy
elif date_time == 'this weekend':
    weather = sunny
else:
    weather = snowy
print(weather)
time.sleep(10)
os.system('clear')

print(
'''
While you both seem in good form , you should decide what to do
a ) go straight to the date venue
b ) go for a stroll in St.Stephens Green Park
c) go for a stroll in the shopping centre , grab coffees
'''
)

first_steps = input("Please choose a, b, or c").lower().strip()
os.system('clear')

if first_steps == 'a' and weather == rainy:
    print(
    f'''
    Good call, its not nice to be out in this rain, 
    best to get to the venue ASAP.
    {date} might get a bit wet but the weather isn't your fault
    No change to endearment score
    ''')
    print(f"Your endearment score is {ENDEARMENT}")
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
    print(f"Your endearment score is {ENDEARMENT}")
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
    print(f"Your endearment score is {ENDEARMENT}")
elif first_steps == 'a' and weather == sunny:
    print(
    f'''
    At your insistence, you and {date} head straight for the venue.
    {date} doesn't seem bothered by heading straight there
    but they comment that it seems like it would have been a nice day for a stroll
    No change to endearment score
    ''')
    print(f"Your endearment score is {ENDEARMENT}")
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
    print(f"Your endearment score is {ENDEARMENT}")
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
    print(f"Your endearment score is {ENDEARMENT}")
elif first_steps == 'a' and weather == snowy:
    print(
    f'''
    At your insistence, you and {date} head straight for the venue.
    {date} doesn't seem bothered by heading straight there
    but they comment that it seems like it would have been a nice day for a stroll
    No change to endearment score
    ''')
    print(f"Your endearment score is {ENDEARMENT}")
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
    print(f"Your endearment score is {ENDEARMENT}")
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
    print(f"Your endearment score is {ENDEARMENT}")
else:
    print(
    f'''
    At your insistence, you and {date} head straight for the venue.
    {date} doesn't seem bothered by heading straight there
    but they comment that it seems like it would have been nice
    to stroll around or grab a coffee somewhere first
    No change to endearment score
    ''')
    print(f"Your endearment score is {ENDEARMENT}")

input(" (press any button to continue) :")
os.system('clear')

print(
f'''
Time to head to the date venue. 

You've decided to go to an italian restaruant.
You and {date} arrive at the restaurant and are met with a friendly greeting of the host. 
Your booking is confirmed and they bring you to the table.

Its an old fashioned italian restaurant,
with old furniture and paintings on the wall, 
candlelight casting dancing shadows across square tables with green tablecloth.
You can see the busy kitchen from here, 
as well as a gentleman playing piano and singing in italian. 

The music augments the already romantic atmosphere. 
You both sit down and the host places menus on front of you.
'''
)
input(" (press any button to continue) :")
os.system('clear')

print(
f'''
The menu has a lot of options , but the prices are rather expensive. 
Oh no! 
Your date doesn’t seem to be bothered by this
as they confidently peruse the menu with interest. 
{date} asks “so what are you thinking of ordering?”
'''
)
time.sleep(15)
os.system('clear')

print(
'''
What meal will you order from the menu?
a) Lasagna b)Spaghetti and meatballs c)Veggie pasta
'''
)

meal_choice = input("Please choose a, b, or c: ").lower().strip()
os.system('clear')

if meal_choice == 'a' and date == 'Sarah':
    print(
    '''
    Sarah is beaming. 
    "No way I was going to order Lasagne too!
    Lasagne is my favourite food.
    I guess we have something in common!"
    Plus 1 point to endearement score
    '''
    )
    ENDEARMENT += 1
    print(f"Your endearment score is {ENDEARMENT}")
elif meal_choice == 'b' and date == 'Francis':
    print(
    '''
    Francis is beaming. 
    "No way I was going to order meatballs too!
    Meaty dishes are my favourite,
    I guess we have something in common!"
    Plus 1 point to endearement score
    '''
    )
    ENDEARMENT += 1
    print(f"Your endearment score is {ENDEARMENT}")
elif meal_choice == 'c' and date == 'Henrietta':
    print(
    '''
    Henrietta is beaming. 
    "No way I was going to order veggie food too!
    I only eat vegetarian food,
    I guess we have something in common!"
    Plus 1 point to endearement score
    '''
    )
    ENDEARMENT += 1
    print(f"Your endearment score is {ENDEARMENT}")
else:
    print(
    f'''
    You order your meal but {date} orders something
    completely different from you.
    You smile awkwardly at each other and 
    look around the room for something to talk about.
    No change to endearment score.
    '''
    )
    print(f"Your endearment score is {ENDEARMENT}")
    time.sleep()
