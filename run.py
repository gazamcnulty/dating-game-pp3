import time
import os
import sys

user = None
endearment = 5
date = None
date_time = None

choice = None
date = None

def input_error():
    os.system('clear')
    print(
    '''
    You typed in an invalid input.
    You need to choose a, b, or c
    Please review the question and try again
    '''
    )
    time.sleep(5)
    os.system('clear')

print(
'''
███ █┼█ ███ ┼┼ ██▄ ███ ███ ███ █┼┼█ ████ ┼┼ ████ ███ █▄┼▄█ ███
┼█┼ █▄█ █▄┼ ┼┼ █┼█ █▄█ ┼█┼ ┼█┼ ██▄█ █┼▄▄ ┼┼ █┼▄▄ █▄█ █┼█┼█ █▄┼
┼█┼ █┼█ █▄▄ ┼┼ ███ █┼█ ┼█┼ ▄█▄ █┼██ █▄▄█ ┼┼ █▄▄█ █┼█ █┼┼┼█ █▄▄
'''
)
time.sleep(4)


def new_game():
    print(
    '''
    Hello there! Welcome to the Dating Game!

    You have been given the chance to find true love. 
    You must pick one of 3 hearthrobs , and then embark on a romantic date.

    Your choices matter, each date has their own preferences,
    and remember, lady luck is always watching!
    ''')
    time.sleep(8)

    game_choice = input("Would you like to play? y / n ").lower().strip()
    os.system('clear')

    if game_choice == 'y':
        print("That's the spirit! Lets start with the rules.")
    elif game_choice == 'n':
        print(
        '''
        That's fine, no need to play if you're already winning.
        There's nothing wrong with being single as long as you're happy!
        If you ever change your mind, return here to play the dating game!

        '''
        )
        time.sleep(5)
        print("    GAME OVER")
        time.sleep(10)
        os.system('clear')
        sys.exit()
    else:
        input_error()
        new_game()


new_game()


def rules():
    global user
    print(
    '''
    Rules: This is a simple text based game. 
    First you will be asked to enter your name. 

    From there you will be given info about the dates and scenarios.

    You will be offered choices of a, b, or c. 
    These choices will decide the outcome of the date.
    '''
    )
    time.sleep(8)
    user = input("Please enter your name:")
    os.system('clear')

    print(f"Pleased to make your acquaintance {user}")
    time.sleep(4)
    os.system('clear')


rules()


def profiles():
    print(
    '''
    The dating world is a tempestuous place, but you're on the hunt for love.
    There are 3 potential star crossed lovers on the horizon.
    You've matched with all three, so lets get to know them!
    ''')

    time.sleep(8)
    os.system('clear')
    input("Are you ready to meet the first match? (press enter to continue: )")
    os.system('clear')

    print('''
    Henrietta

    Profile : 
    Henrietta is a 25 year old college student at Trinity College. 
    She is currently completing her masters in computer science.
    She doesn’t enjoy sports or dancing. 
    She prefers long walks with a good podcast.
    Henrietta likes reading science fiction novels and playing videogames.
    She also likes wearing cool clothes and following fashion.
    She considers herself introverted but has a few close friends.
    She doesn’t like people who are too silly or don’t take themselves seriously.
    She likes people who are honest with her. 
    She doesn’t drink alcohol but loves to drink coffee.
    Henrietta is a vegetarian and her favourite food is Chana Masala.
    ''')

    input("Are you ready to meet the second match? (press enter to continue: )")
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

    input("Are you ready to meet the third match? (press enter to continue: )")
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

    input(" (press enter to continue) :")
    os.system('clear')


profiles()


def date_who():
    global date
    print(
    f''' 
    One of these three captivating individuals could be your one true love!
    But as cruel as cupid's arrow, you must choose one and forsake the others.
    Who do you want to go on a date with {user}?
    a) Henrietta, b) Francis, c) Sarah
    ''')


    date_choice = input("Please choose a, b, or c :").lower().strip()

    if date_choice == 'a':
        date = 'Henrietta'
    elif date_choice == 'b':
        date = 'Francis'
    elif date_choice == 'c':
        date = 'Sarah'
    else:
        input_error()
        date_who()

    os.system('clear')
    print(f"You've chosen to go on a date with {date}!")
    time.sleep(4)
    os.system('clear')


date_who()


def date_when():
    global date_time
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
    elif time_choice == 'c':
        date_time = 'next week'
    else:
        input_error()
        date_when()
    
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
    The big day is here {user}!
    Time to to on our date with {date}!
    You have arranged to meet at the luas stop
    just outside St.Stepehen's Green Park in Dublin city centre.
    ''')
    time.sleep(4)
    os.system('clear')


    if date_time == 'tomorrow':
        print(
        '''
        After your initial greetings at the luas stop by St.Stephens Green,
        you are struck with torrential rains. 
        Neither of you are wearing suitable clothing, 
        it might be best to head somewhere close by to get out of the rain.
        '''
        )
    elif date_time == 'this weekend':
        print(
        '''
        After your initial greetings at the luas stop by St.Stephens Green,
        the clouds part to reveal a warm sunny skyline.
        The sunshine feels good on your face and it puts both of you in a good mood.
        No need to rush anywhere , its fine weather for a walk.
        '''
        )
    else:
        print(
        '''
        After your initial greetings at the luas stop by St.Stephens Green,
        you are met with heavy snow beginning to fall.
        While it is a little cold,
        the crunching of snow under your shoes reminds you both fondly of christmas.
        Its nice to be outside in the snow, just don’t freeze up!
        '''
        )
    time.sleep(4)
    os.system('clear')


    global endearment
    print(
    '''
    While you both seem in good form , you should decide what to do
    a ) go straight to the date venue
    b ) go for a stroll in St.Stephens Green Park
    c) go for a stroll in the shopping centre , grab coffees
    '''
    )

    first_steps = input("Please choose a, b, or c").lower().strip()
    print(f"{first_steps} {date_time}")
    os.system('clear')
    if first_steps == 'a' and date_time == 'tomorrow':
        print(
        f'''
        Good call , its not nice to be out in this rain, 
        best to get to the venue ASAP.
        {date} might get a bit wet but the weather isn't your fault
        No change to endearment score
        ''')
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'b' and date_time == 'tomorrow':
        print(
        f'''
        At your insistence, you and {date} go for a walk in the park.
        It is lashing rain, while you try to make smalltalk.
        {date} is unimpressed by your knowledge of the park's history,
        they seem annoyed and are soaked through to the bone.
        Maybe the park stroll wasn't the best idea...
        Minus 1 point from endearement score
        ''')
        endearment -= 1
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'c' and date_time == 'tomorrow':
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
        endearment += 1
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'a' and date_time == 'this weekend':
        print(
        f'''
        At your insistence, you and {date} head straight for the venue.
        {date} doesn't seem bothered by heading straight there
        but they comment that it seems like it would have been a nice day for a stroll
        No change to endearment score
        ''')
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'b' and date_time == 'this weekend':
        print(
        f'''
        At your insistence, you and {date} go for a walk in the park.
        The sun is shining, while you try to make smalltalk.
        {date} is impressed by your knowledge of the park's history,
        the fresh air and nice weather puts you both in a good mood.
        {date} seems happy you suggested it
        Plus 1 point to endearement score
        ''')
        endearment += 1
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'c' and date_time == 'this weekend':
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
        endearment -= 1
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'a' and date_time == 'next week':
        print(
        f'''
        At your insistence, you and {date} head straight for the venue.
        {date} doesn't seem bothered by heading straight there
        but they comment that it seems like it would have been a nice day for a stroll
        No change to endearment score
        ''')
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'b' and date_time == 'next week':
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
        endearment += 1
        print(f"Your endearment score is {endearment}")
    elif first_steps == 'c' and date_time == 'next week':
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
        endearment -= 1
        print(f"Your endearment score is {endearment}")
    else:
        input_error()
        date_when()


date_when()



input(" (press any button to continue) :")
os.system('clear')

print(
f'''
Time to head to the date venue. 

You've decided to go to an italian restaruant.
You and {date} arrive at the restaurant and
are met with a friendly greeting of the host. 
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


def menu_choice():
    global endearment
    print(
    f'''
    The menu has a lot of options , but the prices are rather expensive. 
    Oh no! 
    Your date doesn’t seem to be bothered by this
    as they confidently peruse the menu with interest. 
    {date} asks “so {user} what are you thinking of ordering?”
    '''
    )
    time.sleep(4)
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
        f'''
        {date} is beaming. 
        "No way I was going to order Lasagne too!
        Lasagne is my favourite food.
        I guess we have something in common {user}!"
        Plus 1 point to endearement score
        '''
        )
        endearment += 1
        print(f"Your endearment score is {endearment}")
    elif (meal_choice == 'b' or 'c') and date == 'Sarah':
        print(
        f'''
        You order your meal but {date} orders something
        completely different from you.
        You smile awkwardly at each other and 
        look around the room for something to talk about.
        No change to endearment score.
        '''
        )
        print(f"Your endearment score is {endearment}")  
    elif meal_choice == 'b' and date == 'Francis':
        print(
        f'''
        {date} is beaming. 
        "No way I was going to order meatballs too!
        Meaty dishes are my favourite,
        I guess we have something in common {user}!"
        Plus 1 point to endearement score
        '''
        )
        endearment += 1
        print(f"Your endearment score is {endearment}")
    elif (meal_choice == 'a' or 'c') and date == 'Francis':
        print(
        f'''
        You order your meal but {date} orders something
        completely different from you.
        You smile awkwardly at each other and 
        look around the room for something to talk about.
        No change to endearment score.
        '''
        )
        print(f"Your endearment score is {endearment}")  
    elif meal_choice == 'c' and date == 'Henrietta':
        print(
        f'''
        {date} is beaming. 
        "No way I was going to order veggie food too!
        I only eat vegetarian food,
        I guess we have something in common {user}!"
        Plus 1 point to endearement score
        '''
        )
        endearment += 1
        print(f"Your endearment score is {endearment}")
    elif (meal_choice == 'a' or 'b') and date == 'Henrietta':
        print(
        f'''
        You order your meal but {date} orders something
        completely different from you.
        You smile awkwardly at each other and 
        look around the room for something to talk about.
        No change to endearment score.
        '''
        )
        print(f"Your endearment score is {endearment}")  
    else:
        input_error()
        menu_choice()

    time.sleep(4)
    os.system('clear')


menu_choice()


def beverage_choice():
    global endearment
    print(
    f'''
    The waiter asks if you would like to order a drink.
    {date} says "I would love a drink!"
    What will you order?
    a) Beer b) Wine c) Dr.Pepper
    '''
    )
    time.sleep(4)

    drink_choice = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    print(drink_choice)

    if (drink_choice == 'a' or 'b') and date == 'Henrietta':
        print(
        f'''
        {date} orders a water, and proceeds to explain
        in a lengthy speech why they don't drink alcohol.
        You decide to keep your opinions to yourself.
        Minus 1 point from endearment score.
        '''
        )
        endearment -= 1
        print(f"your endearment score is {endearment}")
    elif drink_choice == 'a' and date == 'Francis':
        print(
        f'''
        {date} slams their fist down on the table in delight.
        "yeah now we're speaking my language!"
        "They have some nice craft beers, whats your favourite?"
        You and {date} begin chatting away about craft beer,
        you are bonding already!
        Plus 1 point to endearment score.
        '''    
        )
        endearment += 1
        print(f"your endearment score is {endearment}")
    elif drink_choice == 'b' and date == 'Francis':
        print(
        f'''
        Your drinks arrive in no time at all,
        you and {date} toast to the evening
        No change to endearment score
        '''
        )
        print(f"your endearment score is {endearment}")
    elif drink_choice == 'a' and date == 'Sarah':
        print(
        f'''
        Your drinks arrive in no time at all,
        you and {date} toast to the evening
        No change to endearment score
        '''
        )
        print(f"your endearment score is {endearment}")
    elif drink_choice == 'b' and date == 'Sarah':
        print(
        f'''
        {date} slams their fist down on the table in delight.
        "yeah now we're speaking my language!"
        "They have some excellent wine, whats your favourite?"
        You and {date} begin chatting away about wines
        you are bonding already!
        Plus 1 point to endearment score.
        '''    
        )
        endearment += 1
        print(f"your endearment score is {endearment}")
    elif drink_choice == 'c':
        print(
        f'''
        The music suddenly stops. 
        People around you gasp audibly.
        The waiter struggles to compose himself.
        "You ... you said... Dr.Pepper sir?"
        You begin to sweat profusely and nod nervously.
        The waiter looks like someone just ran over his dog.
        The air is thick with tension and fear.
        {date} is staring at the floor.
        Without saying a word, they stand up
        {date} puts on their jacket and walks out of the restaurant.
        You struggle to come to terms with what just happended,
        as the waiter finally brings down your beverage.
        "Your Dr.Pepper sir..." he snarls with utter contempt.
        You can barely contain your shame as you sip your drink.
        Maybe Dr.Pepper in a fancy italian restaurant was a bad idea.
            
        Minus all points from endearment score
        GAME OVER.
        '''
        )
        time.sleep(25)
        os.system('clear')
        sys.exit()
    else: 
        input_error()
        beverage_choice()
    time.sleep(10)
    os.system('clear')


beverage_choice()


def observation_chat():
    global endearment
    print(
    f'''
    You and {date} both smile at each other 
    in awkward silence for a moment. 
    Searching for something to say 
    you look more closely at your date 
    and ask about something you notice.
    What will you ask them?
    a)You look like you’re in great shape, do you exercise a lot?
    b)I like your outfit, do you have an interest in fashion?
    c)Has your nose ever been broken?
    '''
    )
    time.sleep(5)

    observation = input("please choose a, b, or c").lower().strip()
    os.system('clear')
    if observation == 'a' and date == 'Francis':
        print(
        f'''
        {date} is impressed you noticed.
        "You're damn right I do!
        I train hard every day, thanks for noticing!"
        {date} suddenly stands up and flexes their muscles
        they change between multiple poses like Hulk Hogan,
        to the stunned silence of nearby diners.
        You are impressed.
        Plus 1 point to endearment score
        '''
        )
        endearment += 1
        print(f"your endearment score is {endearment}")
    elif observation == 'b' and date == 'Francis':
        print(
        f'''
        {date} gives you a polite answer
        but it doesn't seem to be something they 
        are interested in discussing.
        You talk about your interests without getting too deep.
        Its hard to tell if {date} is having fun,
        or if they are just being polite.
        No change to endearment score.
        '''
        )
        print(f"your endearment score is {endearment}")
    elif observation == 'c' and date == 'Francis':
        print(
        f'''
        {date} looks dismayed.
        "Is it that obvious?
        A few months ago I was working a night shift in the pub
        and I refused to serve a customer who was way too drunk.
        Long story short they punched me in the face 
        and broke my nose.
        I had to get surgery on it, it looks bad doesn't it?"
        Despite your attempts to comfort them, 
        {date} looks forlorn and is bit quieter.
        Maybe that wasn't a good topic of conversation...
        Minus 1 point from endearment score.
        '''
        )
        endearment -= 1
        print(f"your endearment score is {endearment}")
    elif observation == 'a' and date == 'Sarah':
        print(
        f'''
        {date} is impressed you noticed.
        "You're damn right I do!
        I love to go cycling on the weekends.
        You and I should go for a cycle sometime!"
        {date} takes out their phone and pulls up some photos
        they show you a bunch of photos of them cycling
        and visiting different places.
        {date} seems adventurous.
        Plus 1 point to endearment score
        '''
        )
        endearment += 1
        print(f"your endearment score is {endearment}")
    elif observation == 'b' and date == 'Sarah':
        print(
        f'''
        {date} gives you a polite answer
        but it doesn't seem to be of interest to them.
        You talk about your interests without getting too deep.
        Its hard to tell if {date} is having fun,
        or if they are just being polite.
        No change to endearment score.
        '''
        )
        print(f"your endearment score is {endearment}")
    elif observation == 'c' and date == 'Sarah':
        print(
        f'''
        {date} is impressed you noticed.
        "That's pretty observant of you {user}.
        I was on a long cycle recently, went over a rock,
        and flipped right over the handlebars onto the ground.
        I smashed my nose but it didn't smash my determination!"
        {date} takes out their phone and pulls up some photos
        they show you a bunch of photos of them cycling
        and visiting different places.
        {date} seems adventurous.
        Plus 1 point to endearment score
        '''
        )
        endearment += 1
        print(f"your endearment score is {endearment}")
    elif observation == 'a' and date == 'Henrietta':
        print(
        f'''
        {date} looks dismayed.
        "OK there's no need to be mean.
        I know I'm not in great shape, 
        are you just trying to hurt my feelings?
        I know I'm not super athletic or anything
        I'm probably not as skinny as your other dates,
        not everyone has to be a supermodel ya know."
        Despite your attempts to comfort them, 
        {date} looks forlorn and is bit quieter.
        Maybe that wasn't a good topic of conversation...
        Minus 1 point from endearment score.
        '''
        )
        endearment -= 1
        print(f"your endearment score is {endearment}")
    elif observation == 'b' and date == 'Henrietta':
        print(
        f'''
        {date} is impressed you noticed.
        "You're damn right I do!
        I love wearing cool clothes.
        Check out some of these outfits I had on recently."
        {date} takes out their phone and pulls up some photos
        they show you a bunch of photos of them 
        wearing a wide variety of fashionable atire.
        {date} is enjoying talking about clothing.
        Plus 1 point to endearment score
        '''
        )
        endearment += 1
        print(f"your endearment score is {endearment}")
    elif observation == 'c' and date == 'Henrietta':
        print(
        f'''
        {date} gives you a polite answer
        but it doesn't seem to be of interest to them.
        You talk about your interests without getting too deep.
        Its hard to tell if {date} is having fun,
        or if they are just being polite.
        No change to endearment score.
        '''
        )
        print(f"your endearment score is {endearment}")
    else:
        input_error()
        observation_chat()

observation_chat()
time.sleep(15)
os.system('clear')


def talk_about_me():
    print(
    f'''
    As the conversation continues, {date} asks about you.
    “But what about you {user}, 
    tell me something about yourself. 
    How would you describe yourself?”
    What should you say?
    a) "I’m mad craic, 
    I love having a laugh with people and making memories"
    b) "I’m a bit shy , I have my hobbies,
    I’m a good friend once you get to know me"
    c) "I’m confident, I have a drive to succeed, 
    both in work and in relationships"
    '''
    )

    global endearment
    personality = input("please choose a, b, or c").lower().strip()
    os.system('clear')
    if (personality == 'a' or 'c') and date == 'Henrietta':
        endearment -= 1
        print(
        f'''
        {date} tries to smile politely, 
        but you can't help but notice that
        they roll their eyes at this.
        Maybe that's not the kind of person
        they vibe with...
        Minus 1 point from endearment score

        Your endearment score is {endearment}
        '''
        )
    elif personality == 'b' and date == 'Henrietta':
        endearment += 2
        print(
        f'''
        {date} looks at you with real fondness
        in their eyes.
        It feels like this is the first time 
        they've really seen you for who you are.
        "Wow {user}, I'm pretty similar myself" {date} replies,
        "I really value those kinds of qualities in someone"
        {date} reaches across the table and takes your 
        hand and holds it gently.
        Your heart is racing!
        Plus 2 points to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif personality == 'a' and date == 'Francis':
        endearment += 2
        print(
        f'''
        {date} lights up and smiles broadly.
        It seems like they can barely contain their 
        excitement as they excitedly reply
        "Stop, I'm the exact same! We're here to have fun right?
        I think you and I would get on like a house on fire"
        {date} reaches across the table and fist bumps you.
        Your heart is racing!
        Plus 2 points to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif (personality == 'b' or 'c') and date == 'Francis':
        endearment -= 1
        print(
        f'''
        {date} tries to smile politely, 
        but you can't help but notice that
        they roll their eyes at this.
        Maybe that's not the kind of person
        they vibe with...
        Minus 1 point from endearment score

        Your endearment score is {endearment}
        '''
        )
    elif personality == 'c' and date == 'Sarah':
        endearment += 2
        print(
        f'''
        {date} looks at you with real fondness
        in their eyes.
        It feels like this is the first time 
        they've really seen you for who you are.
        "Wow, I'm pretty similar myself" {date} replies,
        "I really value those kinds of qualities in someone"
        {date} reaches across the table and takes your 
        hand and holds it gently.
        Your heart is racing!
        Plus 2 points to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif (personality == 'a' or 'b') and date == 'Sarah':
        endearment -= 1
        print(
        f'''
        {date} tries to smile politely, 
        but you can't help but notice that
        they roll their eyes at this.
        Maybe that's not the kind of person
        they vibe with...
        Minus 1 point from endearment score

        Your endearment score is {endearment}
        '''
        )    
    else:
        input_error()
        talk_about_me()



talk_about_me()
time.sleep(15)
os.system('clear')


def eat_meal():
    global endearment
    print(
    '''
    Finally the food has arrived. 
    The waiter places your plates of food down on front of you, 
    the steam rising from the hot meal brings a delectable aroma.
    You and your date are both excited to tuck into the food, until - disaster!
    It seems the dish on front of {person} is not what they ordered.
    They appear to be a bit confused at first ,
    then disappointed when they realise what has happened.
    You both lock eyes. What do you say ?
    a)“Hey lets swap meals ,
    my dish looks really good I bet you’ll like it!”
    b)“You should let them know they’ve made a mistake,
    they need to bring you the correct meal!”
    c)“Leave this to me , I’ll get the waiter so we can sort this out”
    '''
    )
    dilemma = input("Please choode a, b, or c")
    if date == 'Henrietta' and dilemma == 'a' and (meal_choice == 'a' or 'b'):
        endearment -= 2
        print(
        f'''
        {date} is upset
        "That dish has meat in it, why would I eat that?
        You would rather me eat meat than send it back?
        What is wrong with you {user}?"
        Maybe you shouldn't have offered them this meal...
        Minus 2 points from endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Henrietta' and dilemma == 'a' and meal_choice == 'c':
        endearment += 2
        print(
        f'''
        {date} is moved by your generosity.
        "That's actually so sweet of you to offer. 
        Especially because you ordered a veggie dish too.
        You're really thoughtful {user}!"
        It seems like {date} really likes you!
        Plus 2 points to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Henrietta' and dilemma == 'b':
        endearment -= 1
        print(
        f'''
        {date} is embarrassed.
        "No its fine, I'll just eat this one, I won't make a fuss."
        You try to encourage her to raise the issue 
        but {date} isn't so keen.
        "Don't put me under pressure! It's my decision 
        whether I want to send it back or not."
        "If its so important to you {user},
        you could have just gotten the waiter and said it yourself!"
        Maybe that wasn't the right call...
        Minus 1 point from endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Henrietta' and dilemma == 'c':
        endearment += 2
        print(
        f'''
        You get the waiter's attention, and explain that
        they have brought the wrong order to {date}
        The staff apologies profusely and take it away.
        {date} is moved by your kindness.
        "That's actually so sweet of you to sort that out.
        I'm pretty shy and hate confrontation, so I never would have.
        You're really thoughtful {user}!"
        It seems like {date} really likes you!
        Plus 2 points to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Francis' and dilemma == 'a' and (meal_choice == 'a' or 'b'):
        endearment += 2
        print(
        f'''
        {date} is moved by your generosity.
        "That's actually so sweet of you to offer. 
        Especially because you ordered a meaty too.
        You're really thoughtful {user}!"
        It seems like {date} really likes you!
        Plus 2 points to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Francis' and dilemma == 'a' and meal_choice == 'c':
        endearment -= 1
        print(
        f'''
        {date} is less than keen.
        "Uh, thanks {user} but I'd rather not eat 
        a veggie meal like that, I need a bit of protein."
        "No its fine I'll just sort it with the waiter"
        Maybe you shouldn't have offered them that,
        Minus 1 point from endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Francis' and (dilemma == 'b' or 'c'):
        endearment += 1
        print(
        f'''
        {date} smiles in agreement.
        After a quick exchange with the waiter, 
        the erroneous dish is taken away.
        While they are sorting the correct meal, 
        you and {date} talk about how you need to send food back
        especially when its an expensive meal with a tip.
        {date} is glad you're the kind of person who 
        would get a problem sorted rather than roll over.
        Plus 1 point to endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Sarah' and dilemma == 'a':
        endearment -= 2
        print(
        f'''
        {date} is dumbfounded
        "I'm not going to eat someone elses dinner {user}."
        "I ordered my own meal, so that's what I'm getting!"
        "I can't believe you'd just meekly swap meals,
        instead of taking charge and getting the issue sorted."
        {date} rolls their eyes, and gets the waiter to fix the error.
        Maybe you shouldn't have suggested that.
        Minus 2 points from endearment score.

        Your endearment score is {endearment}
        '''
        )
    elif date == 'Sarah' and (dilemma == 'b' or 'c'):
        endearment += 1
        print(
        f'''
        {date} smiles in agreement.
        After a quick exchange with the waiter, 
        the erroneous dish is taken away.
        While they are sorting the correct meal, 
        you and {date} talk about how you need to send food back
        especially when its an expensive meal with a tip.
        {date} is glad you're the kind of person who 
        would get a problem sorted rather than roll over.
        Plus 1 point to endearment score.

        Your endearment score is {endearment}
        '''
        )


eat_meal()
time.sleep(15)
os.system('clear')


