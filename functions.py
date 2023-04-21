import time
import os
import sys
import random

endearment = 3
date_time = None
meal_choice = None


"""
below are functions to be imported into
run.py file
"""


def input_error():
    os.system('clear')
    print(
        '''
        You typed in an invalid input.
        You need to choose a, b, or c
        Please review the question and try again
        ''')
    time.sleep(5)
    os.system('clear')


def new_game():
    '''
    Welcomes player, introduces the Dating Game.
    Gives player choice y / n to play the game.
    'y' triggers rules() 'n' prints flavour text and ends game
    input validation rejects any answer besides 'y' or 'n'
    '''
    print('''
    Hello there! Welcome to the Dating Game!

    You have been given the chance to find true love.
    You must pick one of 3 hearthrobs , and
    then embark on a romantic date.

    Your choices matter, each date has their own preferences,
    and remember, lady luck is always watching!
    ''')
    game_choice = input("Would you like to play? y / n ").lower().strip()
    os.system('clear')
    if game_choice == 'y':
        print("That's the spirit! Lets start with the rules.")
        time.sleep(3)
        os.system('clear')
    elif game_choice == 'n':
        print(
            '''
            That's fine, no need to play if you're already winning.
            There's nothing wrong with being single as long as you're happy!
            If you ever change your mind, return here to play the dating game!
            '''
        )
        print("    GAME OVER")
        input(" (press enter to clear/exit) :")
        os.system('clear')
        sys.exit()
    else:
        input_error()
        new_game()


def rules():
    '''
    Explains game rules, allows user to enter their name.
    '''
    global user
    print(
        '''
        This is a simple text based game.
        First you will be asked to enter your name.
        From there you will be given context + info about
        the various dates and scenarios.

        You start the game with an 'endearment' score of 3.

        If you can bring the score to 10 by the end of the date,
        you secure a second date and win the game!
        Be warned, some choices can have disastourous
        consequences and result in immediate game over.

        These choices will decide the outcome of the date.
        When asked, please type 'a' , 'b' or 'c',
        followed by 'enter' to confirm
        '''
    )
    time.sleep(3)
    user = input("Please enter your name:")
    os.system('clear')

    print(f"Pleased to make your acquaintance {user}")
    time.sleep(4)
    os.system('clear')


def date_who():
    '''
    Introduces the 3 date matches and allows user to choose
    which person they want to date
    input validation rejects any answer besides 'a' 'b' or 'c' ,
    if another answer is given the function loops
    '''
    os.system('clear')
    global date
    print(
        f'''
        One of these three captivating individuals could be your one true love!
        But as cruel as cupid's arrow, you must choose
        one and forsake the others.

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
    time.sleep(5)
    os.system('clear')


def date_when():
    '''
    Asks user to choose when to go on date, assigns the
    time choice to weather pattern which will affect date.
    '''
    global endearment
    global date_time
    print(
        '''
        We next need to decide when to go on the date.

        When do you want to go on the date?

        a) tomorrow
        b) the weekend
        c) next week?
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
    time.sleep(5)
    os.system('clear')

    print(
        f'''
        The big day is here {user}!

        Time to to on our date with {date}!

        You're starting endearment score is {endearment}
        ''')
    time.sleep(5)
    os.system('clear')
    print(
        f'''
        You have arranged to meet {date} at the luas stop
        just outside St.Stepehen's Green Park in Dublin city centre.
        ''')
    input(" (press enter to continue) :")
    os.system('clear')

    if date_time == 'tomorrow':
        print(
            '''
            After your initial greetings at the luas stop by
             St.Stephens Green,
            you are struck with torrential rains.
            Neither of you are wearing suitable clothing,
            it might be best to head somewhere close by to
            get out of the rain.
            '''
            )
    elif date_time == 'this weekend':
        print(
            '''
            After your initial greetings at the luas stop by
            St.Stephens Green,
            the clouds part to reveal a warm sunny skyline.
            The sunshine feels good on your face and it puts
            both of you in a good mood.
            No need to rush anywhere , its fine weather for a walk.
            '''
            )
    else:
        print(
            '''
            After your initial greetings at the luas stop by
            St.Stephens Green,
            you are met with heavy snow beginning to fall.
            While it is a little cold,
            the crunching of snow under your shoes
            reminds you both fondly of christmas.
            Its nice to be outside in the snow, just don’t freeze up!
            '''
            )
    input(" (press enter to continue) :")
    os.system('clear')


def date_start():
    '''
    Asks user to choose what to do at the start of the date.
    Depending on weather, different choices affect score.
    '''
    global endearment
    global date_time
    print(
        '''
        While you both seem in good form , you should decide
        what to do first

        a ) go straight to the date venue
        b ) go for a stroll in St.Stephens Green Park
        c) go for a stroll in the shopping centre , grab coffees
        '''
        )

    first_steps = input("Please choose a, b, or c").lower().strip()
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
            but they comment that it seems like it would have been
            a nice day for a stroll.

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
            but they comment that it seems like
            it would have been a nice day for a stroll.

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
    input(" (press enter to continue) :")
    os.system('clear')


def menu_choice():
    '''
    Describes setting, asks user to choose meal,
    point given for ordering the same as the date.
    '''
    global endearment
    global meal_choice
    print(
        f'''
        Time to head to the date venue.
        You've decided to go to an italian restaruant.
        You and {date} arrive at the restaurant and
        are met with a friendly greeting of the host.

        Your booking is confirmed and they bring you to the table.
        Its an old fashioned italian restaurant,
        with old furniture and paintings on the wall,
        candlelight casting dancing shadows across
         square tables with green tablecloth.
        You can see the busy kitchen from here,
        as well as a gentleman playing piano and singing in italian.
        The music augments the already romantic atmosphere.

        You both sit down and the host places menus on front of you.
        '''
        )
    input(" (press enter to continue) :")
    os.system('clear')
    print(
        f'''
        The menu has a lot of options , but the prices are rather expensive.
        Oh no!
        Your date doesn’t seem to be bothered by this
        as they confidently peruse the menu with interest.

        {date} asks “so {user} what are you thinking of ordering?”
        '''
        )
    time.sleep(5)

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
    input(" (press enter to continue) :")
    os.system('clear')


def beverage_choice():
    '''
    Asks user to order drink, point given if they choose
    same as the date, (no right answer here for Henrietta),
    triggers instant game over if user chooses Dr.Pepper
    '''
    global endearment
    print(
        f'''
        The waiter asks if you would like to order a drink.
        {date} says "I would love a drink!"
        ''')
    time.sleep(5)
    print('''
        What will you order?

        a) Beer b) Wine c) Dr.Pepper
        ''')
    drink_choice = input("Please choose a, b, or c :").lower().strip()
    os.system('clear')
    if drink_choice == 'c':
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
            '''
            )
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    elif (drink_choice == 'a' or 'b') and date == 'Henrietta':
        print(
            f'''
            {date} orders a 7-up, and proceeds to explain
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
    else:
        input_error()
        beverage_choice()
    input(" (press enter to continue) :")
    os.system('clear')


def observation_chat():
    '''
    Asks user to choose something about their date's
    appearance to ask about. points given if the observation
    reflects the date's interests, points deducted if
    the date is offended
    '''
    global endearment
    print(
        f'''
        You and {date} both smile at each other
        in awkward silence for a moment.
        Searching for something to say
        you look more closely at your date
        and ask about something you notice.''')
    time.sleep(5)
    print('''What will you ask them?

        a)You look like you’re in great shape, do you exercise a lot?
        b)I like your outfit, do you have an interest in fashion?
        c)Has your nose ever been broken?
        '''
        )

    observation = input("please choose a, b, or c :").lower().strip()
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
            but it doesn't seem to be something they
            are interested in discussing.
            You talk about your interests without getting too deep.
            Its hard to tell if {date} is having fun,
            or if they are just being polite.

            No change to endearment score.
            '''
            )
        print(f"your endearment score is {endearment}")
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
            but it doesn't seem to be something they
            are interested in discussing.
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
    input(" (press enter to continue) :")
    os.system('clear')


def talk_about_me():
    '''
    Asks user to describe their own personality
    points given if it matches date's personality
    '''
    print(
        f'''
        As the conversation continues, {date} asks about you.
        “But what about you {user},
        tell me something about yourself.
        How would you describe yourself?”''')

    time.sleep(5)
    print('''What should you say?

        a) "I’m mad craic,
        I love having a laugh with people and making memories"
        b) "I’m a bit shy , I have my hobbies,
        I’m a good friend once you get to know me"
        c) "I’m confident, I have a drive to succeed,
        both in work and in relationships"
        ''')

    global endearment
    personality = input("please choose a, b, or c").lower().strip()
    os.system('clear')
    if date == 'Henrietta' and personality == 'b':
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
    elif date == 'Henrietta' and (personality == 'a' or 'c'):
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
    elif date == 'Francis' and personality == 'a':
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
    elif date == 'Francis' and (personality == 'b' or 'c'):
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
    elif date == 'Sarah' and personality == 'c':
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
    elif date == 'Sarah' and (personality == 'a' or 'b'):
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
    input(" (press enter to continue) :")
    os.system('clear')


def eat_meal():
    '''
    Asks user to choose how to address the date being
    given the wrong food order. Gain lose points depending
    on date's personality / response to choice
    '''
    global endearment
    print(
        f'''
        Finally the food has arrived.
        The waiter places your plates of food down on front of you,
        the steam rising from the hot meal brings a delectable aroma.
        You and your date are both excited
        to tuck into the food, until - disaster!
        It seems the dish on front of {date} is not what they ordered.
        They appear to be a bit confused at first ,
        then disappointed when they realise what has happened.''')

    time.sleep(5)
    print('''You both lock eyes. What do you say ?

        a)“Hey {date} lets swap meals ,
        my dish looks really good I bet you’ll like it!”
        b)“You should let them know they’ve made a mistake,
        they need to bring you the correct meal!”
        c)“Leave this to me , I’ll get the waiter so we can sort this out”
        ''')
    dilemma = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if date == 'Henrietta' and dilemma == 'a' and meal_choice == 'c':
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
    elif date == 'Henrietta' and dilemma == 'a' and (meal_choice == 'a'
                                                     or 'b'):
        endearment -= 2
        print(
            f'''
            {date} is upset
            "That dish has meat in it, why would I eat that?
            You would rather me eat meat than send it back?
            What is wrong with you {user}?"
            Maybe you shouldn't have offered them this meal...

            Minus 2 points from endearment score.

            Your current endearment score is {endearment}
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

            Your current endearment score is {endearment}
            '''
            )
    elif date == 'Henrietta' and dilemma == 'c':
        endearment += 2
        print(
            f'''
            You get the waiter's attention, and explain that
            they have brought the wrong order to {date}
            The staff apologise profusely and take it away.
            {date} is moved by your kindness.
            "That's actually so sweet of you to sort that out.
            I'm pretty shy and hate confrontation, so I never would have.
            You're really thoughtful {user}!"
            It seems like {date} really likes you!

            Plus 2 points to endearment score.

            Your current endearment score is {endearment}
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
    elif date == 'Francis' and dilemma == 'a' and (meal_choice == 'a' or 'b'):
        endearment += 2
        print(
            f'''
            {date} is moved by your generosity.
            "That's actually so sweet of you to offer.
            Especially because you ordered a meaty dish too.
            You're really thoughtful {user}!"
            It seems like {date} really likes you!

            Plus 2 points to endearment score.

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
    else:
        input_error()
        eat_meal()
    input(" (press enter to continue) :")
    os.system('clear')


def choking():
    '''
    1 of 5 possible scenarios , from random_encounter()
    points given for 2 possible right choices,
    instant game over for the wrong choice
    '''
    global endearment
    print(
        f'''
        As you're about to begin a scintilating conversation
        regarding Star Trek and the inconsistencies of
        warp speed in starships, you hear a nearby shriek.
        A gentleman at a nearby table appears to be choking!
        He jumps up and starts gesturing histrionically,
        while his companions shout for someone to help.
        "We need to do something!" says {date}''')

    time.sleep(5)
    print('''What will you do?

        a) Attempt the heimlich manoevre on the choking man.
        b) Run outside and shout for a doctor
        c) Throw some pepper under his nostrils to make him sneeze
        ''')
    choke_response = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if choke_response == 'a':
        endearment += 1
        print(
            f'''
            You quickly leap into action, sprinting towards the man
            you grab him from behind and expertly perform
            the heimlich manoeuvre.
            After 3 mighty thrusts, a piece of bread flies out
            you've saved him and he can breathe easy again!
            Everyone claps with relief, while {date} smiles at you.
            "That was the right call {user} you're
            great under pressure. You helped save a life!"
            {date} is impressed.

            Plus 1 point to endearment score.
            '''
            )
    elif choke_response == 'b':
        endearment += 1
        print(
            f'''
            You instruct {date} to call an ambulance,
            while you run outside and shout for a doctor.
            Luckily a person passing by is a doctor,
            they follow you in and perform first aid on the man.
            The piece of food is extricated and he is able to breathe again.
            Everyone claps with relief, while {date} smiles at you.
            "That was the right call {user} you're
            great under pressure. You helped save a life!"
            {date} is impressed.

            Plus 1 point to endearment score.
            '''
            )
    elif choke_response == 'c':
        print(
            f'''
            Thinking quickly, you grab a pepper shaker and
            leap into action.
            You skillfully dart over and fire a cloud
            of pepper, right into the choking mans nose.
            A perfectly executed manoevre, the mans nostrils are
            completely covered in pepper.
            As you stand there trimphantly, you realise that
            everyone else is staring at you in disbelief.
            {date} screams at you
            "Why the hell did you do that {user}???"
            With a smug grin, you humbly explain the idea
            that pepper will cause the gentleman to sneeze violently.
            {date} is beside themselves.
            "but the food is stuck in his throat ,
            not inside his nose you idiot!"
            The realisation dawns on you, while the poor man
            continues to choke and gasp while also sneezing repeatedly.
            He collapses to the floor, dead as a doorknob.
            The silence in the room is heavy.
            You slowly raise your head and lock eyes with {date}
            "Do you want to split the bill or?"

            Unfortunately it appears this date is over.
            '''
            )
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    else:
        input_error()
        choking()
    input(" (press enter to continue) :")
    os.system('clear')


def singing():
    '''
    1 of 5 possible scenarios , from random_encounter()
    points given for 2 possible right choices,
    instant game over for the wrong choice
    '''
    global endearment
    print(
        f'''
        The gentleman playing piano is
        producing a beautiful seranade,
        {date} comments on how beautiful the music is.

        After a moment the musician stands up and approaches your table
        "The two of you seem to be having a lovely evening.
        Would you like to make a request?"
        {date} nods excitedly
        "absolutely , {user} what sond would you like to hear?"''')
    time.sleep(5)
    print('''What song will you choose?

        a) In the air tonight
        b) The book of love
        c) Master of Puppets''')
    song_choice = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if song_choice == 'a':
        print(
            f'''
            The musician nods approvingly and begins the song.
            As Phil Collins' classic power balad
            echoes between the walls of the restaurant,
            you are distracted from the date and focused on the music.

            The musician is so intense, sweat covering his furrowed brow.
            You nod along getting more and more into the music,
            completely ignoring your date.

            By the time the drum solo kicks in prior to the chorus
            you are on your feat air drumming along.
            You and the musician belt out the chorus
            " I can feeeeeel it, cooomin in the air tonight....
            hold on! "

            This is the most intense musical experience you have ever had.
            You've never enjoyed a song this much before.
            As the final notes play out, you drop to your knees
            and scream a primal roar.

            The other patrons stand and give a standing ovation
            to the musician and to yourself.
            You stand up with tears in your eyes, and grab the musician
            in a tight bearhug.

            You turn back to the table, {date} is gone.

            They musn't be a fan of Phil Collins.
            '''
            )
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    elif song_choice == 'b':
        endearment += 2
        print(
            f'''
            The musician nods approvingly and begins the song.
            As Stephin Merritt's classic loves song echoes
            through the halls of the restaurant,
            {date} begins to sob.

            "Its just such a beautiful song" they cry.
            You don't really know what to say.
            You decide to hold {date}'s hand and smile,
            without saying anything.

            {date} is very glad you played this song.
            It seems like love is in the books!

            Plus 2 points to endearment score.

            Your current endearment score is {endearment}
            '''
            )
    elif song_choice == 'c':
        endearment += 10
        print(
            f'''
            The musician is perplexed, appears weary, but nods.
            He disappears into another room ,
            he is gone for so long you begin to wonder if he forgot.

            {date} laughs at you for making such a request,
            though they admit they are a fan of Metallica.

            Then from out of nowhere , he musician emerges again,
            electric guitar strapped on shoulder and an amp under his arm.
            The next 8 minutes and 35 seconds are a blur.

            He gives it his all, absolutely screaming into the microphone.
            Despite the restaurant managers pleading,
            the musician will not stop.
            He has been consumed by the spirit of rock and no one is safe.

            At first {date} can't believe it, but within moments
            they are singing along as well.
            This seems to be a lot more interesting than dinner.
            You and {date} are moshing along like you have nothing to live for.

            Unfortunately the head banging is so intense,
            {date} literally smashes their head into the table.

            The results follow shortly:
            A minor concussion , some short term memory loss and...
            a second date!!!
            {date} had such a good time, they want to bring you to a gig.

            A local rock band is playing next weekend,
            {date} is eager to rock out with you once more.
            Hopefully this one won't result in a head injury.

            Plus 10 points to endearment score.
            '''
            )
        input(" (press enter to continue) :")
        game_victory()
    else:
        input_error()
        singing()
    input(" (press enter to continue) :")
    os.system('clear')


def robbery():
    '''
    1 of 5 possible scenarios , from random_encounter()
    points given for 2 possible right choices,
    instant game over for the wrong choice
    '''
    global endearment
    print(
        f'''
        As you are enjoying your meal,
        a hooded figure crashes through the door.
        He bellows "THIS IS A ROBBERY!"
        Nearby patrons scream and panic,
        while you and {date} scramble under the table.
        This is a dangerous situation, {date} is scared.''')
    time.sleep(5)
    print('''What should you do?

        a) Don't take any action , let the robber
        do what he wants so you can both stay safe.
        b) This is the moment you've been waiting for.
        Challenge the scoundrel in single combat.
        c) Look more closely at the robber,
        for some kind of detail or info that can help.
        ''')
    robbery_choice = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if robbery_choice == 'a':
        endearment += 1
        print(
            f'''
            The robber fleeces the restaurant of all valuables.
            He empties the cash registers, takes jewellery and wallets.
            {date} pleads for a moment not to hand over their ring
            but eventually they relent and offer it up.

            You hand over your wallet while the robber sneers at you.
            After a 5 minute ordeal that felt like eternity,
            the ne'er do well is gone.

            You and {date} are glad to be safe, but understandably shook.
            While it doesn't feel right to continue the date,
            you offer to walk {date} out.

            Outside the luas you both share an awkward laugh,
            then a brief hug.
            Despite everything, {date} is glad you're safe
            What a strange way to end the evening...

            Plus 1 point to endearment score
            '''
            )
        input(" (press enter to continue) :")
        end_check()
    elif robbery_choice == 'b':
        print(
            f'''
            When the robber demands your wallet, you respond
            with an incredulous guffaw.
            "Filth! You'll not take a euro from me.
            As a matter of fact, you won't be stealing anything!
            Put up your dukes thug, I challenge you to battle!"

            People around you gasp audibly.
            The air is thick with tension and fear.
            The robber's eyes narrow, this isn't his first fight.

            He calmly approaches you, grabs you by your ears,
            and then body slams you into a fish tank.

            When you eventually regain consiousness, 20 minutes have passed.

            The nice waiter explains the robber got all the goods,
            and fled the scene.
            Whats worse is he ridiculed you as while you were KO'd.
            {date} was embarrassed by your antics and also
            so impressed by the bravado of the robber, they left too!
            The last thing the other patrons saw was
            {date} back of the robber's motorcycle!

            {date} stole your heart , the robber stole your wallet.

            What a strange way to end the evening...
            '''
            )
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    elif robbery_choice == 'c':
        endearment += 1
        print(
            f'''
            As the robber moves from table to table grabbing what he can,
            you look closely at him.
            Just as he comes up to you, you both lock eyes and behold
            at each other.

            Staring him in the face , it hits you.
            You struggle to speak.

            " ... Dad? "
            The robber's eyes widen.
            " ... {user}? "

            You haven't seen each other in years!
            Before you know it you're both hugging and crying.
            Even {date} can't help but get a little emotional.

            Before you get a chance to talk , the manager
            says he's calling the police.
            Your dad rushes to escape , but not before
            taking one last look at you.
            "I'll see you again soon {user} , I promise."
            And with that he is gone.

            {date} doesn't really know what to say ,
            so they just sit back down and continue eating their food.
            No one wants their dad butting in on a date,
            but {date} still seems keen!

            Plus 1 point to endearment score.

            Your current endearment score is {endearment}
            ''')
        input(" (press enter to continue) :")
    else:
        input_error()
        robbery()
    input(" (press enter to continue) :")
    os.system('clear')


def rodent():
    '''
    1 of 5 possible scenarios , from random_encounter()
    points given for 2 possible right choices,
    instant game over for the wrong choice
    '''
    global endearment
    print(
        f'''
        Just as you're about to launch into a fascinating
        anecdote related to parmesan cheese,
        a patron nearby shrieks with terror.
        "It's a rat!"
        Sure enough, you see the rodent sprinting across the floor.
        {date} is disgusted and the waiter is mortified.''')
    time.sleep(5)
    print('''What should you do?

        a) Throw your knife at the rat
        b) Throw your complaint at the manager
        c) Throw your money on the table and leave
        ''')
    rodent_response = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if date == 'Henrietta' and rodent_response == 'a':
        print(f'''
            Like a cold hearted assasin , your throw the knife
            directly at the disease carrying creature.
            {date} emits a blood curdling scream.
            "You murdered an innocent rat, how could you!"
            {date} is so upset they get up and leave the restaurant.

            You knew {date} was a vegetarian, but you
            didn't think she cared for rats too?

            Maybe you're the true rat.

            ''')
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    elif (date == 'Francis' or 'Sarah') and rodent_response == 'a':
        endearment += 2
        print(f'''
            Like a cold hearted assasin , your throw the knife
            directly at the disease carrying creature.
            Unfortunately you overestimated and the throw misses,
            smashing directly into the aquarium.

            The rat is joined by various fish as the contents
            of the destroyed tank spill onto the floor.
            When everything is cleaned up, the waiter tells you
            they have added a €400 surplus charge to your bill
            to cover the cost of the aquarium.

            {date} is understandably mortified.

            Minus 2 points from endearment score.

            Your current endearment score is {endearment}
            ''')
    elif rodent_response == 'b':
        endearment += 1
        print(f'''
            You will not stand for rodents interrupting romance.
            {date} looks on while you march up to the manager
            and deliver an emphatic complaint about the situation.
            The manager repeatedly apologises, he even
            offers to comp the cost of your drinks free of charge.
            Nice! {date} is impressed too.

            Plus 1 point to endearment score.

            Your current endearment score is {endearment}
            ''')
    elif rodent_response == 'c':
        endearment += 3
        print(f'''
            You will not stand for rodents interrupting romance.
            {date} looks on while you throw money on the table.
            "C'mon, we're leaving"
            You and {date} quickly exit the establishment,
            while the manager follows apologising repeatedly.
            You decide to go to a nearby café for a coffee before
            letting the date end too early.
            The bizarre situation has actually broken the ice a bit,
            now you and {date} are chatting and laughing like old friends.
            Before you know it you're swapping stories, telling jokes,
            and gazing into each other's eyes.
            You wait and wait, then when the time is right,
            you steal a kiss!
            {date}'s face turns red but they can't stop smiling either.
            Maybe the rat was a blessing after all?
            You walk {date} to the luas stop to bring your date to a close.

            Plus 3 points to endearment score, thanks to rat-bro.

            Your current endearment score is {endearment}
            ''')
        input(" (press enter to continue) :")
        os.system('clear')
        goodbye()
    else:
        input_error()
        rodent()
    input(" (press enter to continue) :")
    os.system('clear')


def argument():
    '''
    1 of 5 possible scenarios , from random_encounter()
    points given for 2 possible right choices,
    points lost for wrong choice
    '''
    global endearment
    print(f'''
        Just as you're summoning up the courage to tell
        {date} about the size of your Pokémon card collection,
        a nearby table erupts in shouts.
        It seems like the other couple are having a fierce argument!''')
    time.sleep(5)
    print('''What should you do?

        a) Mind your own business
        b) Offer to mediate their discussion
        c) Tell them to shut up
        ''')
    argument_action = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if argument_action == 'a':
        endearment += 2
        print(
            f'''
            You wisely decide not to encroach on the
            other couples business.
            If you were in their shoes, you wouldn't want
            a complete stranger coming up and butting in.
            You and {date} share a knowing glance ,
            you can't help but laugh at the awkward situation.
            "Well" says {date} "at least we're not at the
            stage where we're screaming at each other in
            restaurants eh?"

            With a smirk you reply "give it time"
            I see a long lasting relationship on the cards,
            trust me there'll be plenty of screaming arguments
            between us in many restaurants.
            {date} laughs , they also seem keen that
            you envision a relationship, jokingly or not.

            Plus 2 points to endearment, thanks to
            the dysfunctional couple at the next table.

            Your current endearment score is {endearment}
            '''
            )
    elif argument_action == 'b':
        endearment -= 1
        print(
            f'''
            You gallantly approach the couple, arms outstretched
            hands open in friendship and peace.
            "My friends, what is the trouble here?
            Maybe I could offer a balanced view , to help
            mediate your discussion?
            The lady at the table immediately throws a glass of wine
            in your face.
            She then turns back to her partner and resumes
            the argument with renewed vigour.
            You return to the table with your tail between your legs.
            {date} keeps their eyes on their food.
            At least the wine she threw tasted nice.

            Minus 1 point from endearment score.

            Your current endearment score is {endearment}
            '''
            )
    elif argument_action == 'c':
        endearment += 1
        print(
            f'''
            You've taken as much as you can take.
            Fed up, fuming, you confront the other couple
            "Will you people shut up? I get you can't
            afford couple's therapy , but that doesn't
            give you the right to ruin everyone elses meal!"

            The couple are shocked and offended, which
            causes them to direct their anger away from each
            other and aim it at you!

            "Who do you think you are, how dare you!"
            As you worry if this will upset {date},
            you're surprised to find them standing next to you,
            shouting right back at the couple.
            "{user} is right , you guys should get out of here!"

            The four of you are lobbing insults at each other
            until the staff manage to seperate you.
            The other couple leaves, other patrons thank you
            for calling them out on their behaviour.
            {date} is impressed and you're glad they had your back.

            Plus 1 point to endearment score.

            Your current endearment score is {endearment}
            '''
            )
    else:
        input_error()
        argument()
    input(" (press enter to continue) :")
    os.system('clear')


def random_encounter():
    '''
    generates random number between 0 - 6, which then
    triggers 1 of 5 possible random scenarios.
    each scenario has instant game over and game victory
    possibilities, as well as usual point gain/loss
    '''
    global endearment
    print(
        f'''
        You and {date} continue to eat and drink,
        enjoying your meal in companiable silence.

        '''
        )
    chance = random.randint(1, 5)
    if chance == 1:
        choking()
    elif chance == 2:
        singing()
    elif chance == 3:
        robbery()
    elif chance == 4:
        rodent()
    elif chance == 5:
        argument()


def spontaneous():
    '''
    asks user to choose spontaneous action, can gaing points
    or result in instant game over depending on the date
    wrong choice
    '''
    global endearment
    print(
        f'''
        After some time has passed, you and
        {date} are almost finished your food.
        you think to yourself, "Hmm I wonder if this date is going well?"
        "in any case, I can’t coast on good luck. I need
        to keep the good vibes going. Maybe I can do something else … "''')
    time.sleep(5)
    print('''What will you do ?
        a) Call the waiter over and order an expensive bottle of champagne
        b) Pierce a chunk of food, and guide the fork towards your date’s mouth
        c) Lean over to your date and whisper in their ear “ I have a bomb”
        ''')
    spontaneous_decision = input("Please choose a, b, or c")
    os.system('clear')
    if date == 'Henrietta' and spontaneous_decision == 'a':
        print(
            f'''
            You beckon the waiter over and order
            the finest bottle of champagne they have on offer.
            At this stage it looks like {date} is
            ready to burst into tears.
            "I told you I don't drink alcohol, why
            would you order that?
            Do you expect me to just sit here
             and watch you drink champagne?"
            Before you can answer, {date} gets up and leaves.
            Right as you're thinking about where it all went wrong,
            you hear the signature 'pop' of the
            champagne bottle being opened.
            Shame to let some bubbly go to waste.
            You finish your meal, enjoy some champagne and ,
            ya know what? You had an ok night all things considered!
            Probably!
            ?
            Maybe an entire bottle of champagne is a lot for
            just one person...
            You stumble out the door , while the waiter
            chases you down asking for payment.
            ''')
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    elif (date == 'Francis' or 'Sarah') and spontaneous_decision == 'a':
        endearment += 1
        print(
            f'''
            You beckon the waiter over and order
            the finest bottle of champagne they have on offer.
            {date} is into this!
            Before you know it, you hear the signature 'pop' of the
            champagne bottle being opened.
            You and {date} share a toast and drink some
            excellent champagne.
            It gives you both a nice buzz and leads
            to some scintilating conversation and funny stories.
            Champagne is always a good call.
            Plus 1 point to endearment score.
            Your current endearment score is {endearment}
            ''')
    elif spontaneous_decision == 'b':
        endearment += 1
        print(
            f'''
            You decide it would be a great idea to try and
            feed your date, by bringing a fork of food to their mouth.
            While they initially appear shocked , {date} actually
            laughs and then accepts the piece of food. Its tasty!
            But then - {date} returns the gesture!
            Now {date} is guiding a fork of their food to your mouth!
            Well this is cute!
            Plus 1 point to endearment score.
            Your current endearment score is {endearment}
            ''')
    elif spontaneous_decision == 'c':
        print(
            f'''
            You decide it would be a great idea to try and
            convince your date that you have an explosive device with you.
            You lean over the table towards {date}
            they close their eyes and purse their lips ,
            expecting a kiss?
            Instead you whisper in their ear "I have a bomb"
            Acting quickly , {date} immediately screams for help.
            Before you can explain that it was a joke,
            you are tackled to the ground by an off duty police officer.
            As the cuffs are slipped on your wrists, you wonder if this
            means you don't have to pay for dinner.
            -  6 months later -
            It seems like you're finally going to get out of prison!
            Your solicitor has managed to convince the judge
            that you probably aren't a ring leader of a local
            terrorist cell, that exclusively targets italian bistros.
            It was all a simple misunderstanding.
            Maybe you'll give {date} a call? Although they probably
            have your number blocked at this stage.
            ''')
        input(" (press enter to continue) :")
        os.system('clear')
        game_failure()
    else:
        input_error()
        spontaneous()
    input(" (press enter to continue) :")
    os.system('clear')


def dessert():
    '''
    asks user to choose dessert, points given if
    they order what their date would have wanted
    '''
    global endearment
    print(
        f'''
        As you finish up your food, you and {date} smile,
        and agree that the food was worth the wait.
        The waiter comes to take away the food and
        asks if you would like anything for desert.''')
    time.sleep(5)
    print('''What will you do?
        a) Order ice cream
        b) Order chocolate cake
        c) Order coffee
        ''')
    dessert_choice = input("Please choose a, b, or c").lower().strip()
    os.system('clear')
    if date == 'Henrietta' and dessert_choice == 'c':
        endearment += 1
        print(
            f'''
            {date} is absolutely delighted .
            "My favourite, thank you so much
            for ordering it {user}!"
            You and {date} share a dessert and discuss some
            of your other favourite foods.
            Possibly something for the next dinner date?
            Plus 1 point to endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif date == 'Henrietta' and (dessert_choice == 'a' or 'b'):
        endearment -= 1
        print(
            f'''
            {date} doesn't say anything , but they seem dissappointed.
            Maybe you ordered the wrong thing?
            At least the date is nearly over...
            Minus 1 point from endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif date == 'Francis' and dessert_choice == 'b':
        endearment += 1
        print(
            f'''
            {date} is absolutely delighted .
            "My favourite, thank you so much
            for ordering it {user}!"
            You and {date} share a dessert and discuss some
            of your other favourite foods.
            Possibly something for the next dinner date?
            Plus 1 point to endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif date == 'Francis' and (dessert_choice == 'a' or 'c'):
        endearment -= 1
        print(
            f'''
            {date} doesn't say anything , but they seem dissappointed.
            Maybe your ordered the wrong thing?
            At least the date is nearly over...
            Minus 1 point from endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif date == 'Sarah' and dessert_choice == 'a':
        endearment += 1
        print(
            f'''
            {date} is absolutely delighted .
            "My favourite, thank you so much
            for ordering it {user}!"
            You and {date} share a dessert and discuss some
            of your other favourite foods.
            Possibly something for the next dinner date?
            Plus 1 point to endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif date == 'Sarah' and (dessert_choice == 'b' or 'c'):
        endearment -= 1
        print(
            f'''
            {date} doesn't say anything , but they seem dissappointed.
            Maybe your ordered the wrong thing?
            At least the date is nearly over...
            Minus 1 point from endearment score.
            Your current endearment score is {endearment}
            '''
            )
    else:
        input_error()
        dessert()
    input(" (press enter to continue) :")
    os.system('clear')


def bill():
    '''
    asks user how to approach paying the bill
    slight points amount differences depending on the date,
    points lost if user tries to run
    '''
    global endearment
    print(
        f'''
        Finally , the meal is drawing to a close.
        The waiter brings the bill for payment.
        This is the classic dilemma,
        an inevitable moment for any date.
        The bill is placed right in the middle of the table,
        equal distance between you and {date}.
        You both smile and open your mouths to speak at the same time,
        then laugh. {date} lets you go first,
        “I’m sorry what were you going to say?”''')
    time.sleep(5)
    print('''What should you say?
        a) “Shall we split the bill  50 / 50 ?”
        b) “Let me pay for the meal, I insist”
        c) “Grab your jacket, get ready to run”
        ''')
    bill_choice = input("Please choose a, b, or c")
    os.system('clear')
    if date == 'Francis' and bill_choice == 'a':
        endearment += 1
        print(
            f'''
            You suggest splitting the bill 50 / 50.

            {date} is delighted to hear that.
            "That's a relief , i was worried you would
            want me to pay ha ha!"
            "All jokes aside, I think its best to
            split the bill down the middle, I'm glad you agree."
            {date} is happy with this.
            Plus 1 point to endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif (date == 'Henrietta' or 'Sarah') and bill_choice == 'a':
        print(
            f'''
            You suggest splitting the bill 50 / 50.
            {date} nods in agreement and takes out some cash to pay.
            They seem to agree that splitting the bill is the
            best thing to do, but you can't help but feel
            as though they're not happy about it.
            No change to endearment score.
            Your current endearment score is {endearment}
            '''
            )
    elif bill_choice == 'b':
        print(
            f'''
            You offer to pay the bill yourself.
            {date} tries to decline and insist that
            they should split the bill.
            After some convincing, {date} capitulates
            and thanks you for being so generous.
            You take a chance and say
            "Well since I'm paying on this date, you can
            pay on the next date!"
            {date} smiles at this , but they don't confirm
            or deny your assertion.
            We'll see ...
            Plus 2 points to endearment score.
            Your current endearment score is {endearment}

            '''
            )
    elif bill_choice == 'c':
        endearment -= 3
        print(
            f'''
            You lower your head and look intently at {date}
            "Grab your jacket , get ready to run"
            {date} seems to think you're kidding, they
            let out an awkward laugh while you scout out the exit.
            "Ok , on 3. 1 ... 2 ... 3!"
            You're up and out like a flash , sprinting towards the door.
            You dodge around a clueless staff member, and
            leap over a table like an olympian.
            You burst out the door and tear down the street.
            After rounding the corner you trip over a small dog.
            The dog regards you as a threat and leaps into an attack.
            You run back in the opposite direction , the dog
            nipping at your heels as you go.
            As you head back in the opposite direction you run
            face first into {date}, causing you, {date} and the dog
            to fall over into a pile.
            While the dog is biting you in the face, {date}
            shouts that she had to pay the bill.
            You suspect that this wasn't the best way to end
            the date.
            Minus 3 points from endearment score.
            Your current endearment score is {endearment}
            '''
            )
    else:
        input_error()
        bill()
    input(" (press enter to continue) :")
    os.system('clear')


def goodbye():
    '''
    asks user to choose how to say goodbye
    if endearment is 8 points or more, they can kiss
    and gain more points
    if user tries to prolong date, it generates
    random number. 1 in 5 chance of saying yes and
    gain more points
    '''
    global endearment
    print(
        f'''
        With that , its time to wrap up the date.
        You walk {date} back to the luas stop, you
        both chat about the evening.
        It's hard to tell how much {date} likes you,
        but you'll never know unless you take a chance.
        The luas display shows it will be here in
        two minues, its now or never!''')
    time.sleep(5)
    print('''What should you say?
        a) "I'm really glad I met you"
        b) "Kiss me you fool"
        c) "Lets not end the date, cmon lets grab a drink!"
        ''')
    goodbye_chance = input("Please choose a, b, or c")
    os.system('clear')
    if goodbye_chance == 'a':
        endearment += 1
        print(
            f'''
            You put your arm on {date}'s shoulder and
            say with sincerity
            "I'm really glad I met you {date}"
            {date} looks at you and smiles warmly
            "you're an interesting person {user}, I
            can safely say that!
            And ... yeah I'm glad I met you too.
            You and {date} embrace in a tender hug,
            before they get on the luas.
            As the luas heads off down the track, you
            stop to recall the events of the date.
            How well do you think it went?
            I wonder if there will be a second date...
            Endearment score plus 1

            '''
            )
    elif goodbye_chance == 'b' and endearment >= 8:
        print(f'''
            You put your arm on {date}'s shoulder and
            say with sincerity
            "Kiss me you fool"
            {date} looks at you and smiles warmly
            "you're an interesting person {user},
            I won't forget you any time soon."
            You watch as {date} gets on the luas...
            ''')
        print(f'''
            ... Suddenly, as you're about to walk away, {date}
            runs out towards you and pulls you in for a kiss!
            yes!!!
            {date} laughs and runs back to squeeze through the
            doors of the luas before they close.
            That was a nice way to end a first date!
            But will there be a second date?...
            ''')
    elif goodbye_chance == 'b' and endearment < 8:
        endearment += 1
        print(
            f'''
            You put your arm on {date}'s shoulder and
            say with sincerity
            "Kiss me you fool"
            {date} looks at you and smiles warmly
            "you're an interesting person {user},
            I won't forget you any time soon.
            I think there are some things I like about you,
            but I don't think I want to kiss you right now."
            You and {date} embrace in a tender hug,
            before they get on the luas.
            As the luas heads off down the track, you
            stop to recall the events of the date.
            How well do you think it went?
            I wonder if there will be a second date...
            Endearment score plus 1
            '''
            )
    elif goodbye_chance == 'c':
        print(
            f'''
            You stammer out a final plea
            "Don't get on the luas! Lets not allow
            the date to end here, why don't we go grab a
            drink or a coffee somewhere?
            {date} turns and looks you in the eye
            ''')
        chance = random.randint(0, 6)
        if chance == 3:
            endearment += 3
            print(
                f'''
                {date} answers you
                "Ya know what? Why not? Lets keep the date going
                a bit longer, how much worse can it get right?"
                You and {date} share a laugh and turn back towards town,
                looking for a bar or café to spend more time together.
                As the night progresses, the situation has actually
                broken the ice a bit,
                now you and {date} are chatting and laughing like old friends.
                Before you know it you're swapping stories, telling jokes,
                and gazing into each other's eyes.
                You wait and wait, then when the time is right,
                you steal a kiss!
                {date}'s face turns red but they can't stop smiling either.
                You walk {date} to the luas stop to bring your date to a close.
                Plus 3 points to endearment score.
                ''')
            end_check()
        else:
            endearment += 1
            print(
                f'''
                {date} answers you
                "I'm sorry {user} I don't think
                going for a drink is a good idea right now.
                The date's wrapped up, lets call it a night.
                {date} looks at you and smiles warmly
                "you're an interesting person {user},
                I won't forget you any time soon."
                You and {date} embrace in a tender hug,
                before they get on the luas.
                As the luas heads off down the track, you
                stop to recall the events of the date.
                How well do you think it went?
                I wonder if there will be a second date...
                Endearment score plus 1
                '''
                )
            end_check()
    else:
        input_error()
        goodbye()
    input(" (press enter to continue) :")
    os.system('clear')


def end_check():
    '''
    checks endearment score , triggers game_victory if 10 or higher,
    triggers game_failure() if less than 10
    '''
    global endearment
    if endearment >= 10:
        game_victory()
    else:
        game_failure()


def game_victory():
    '''
    prints victory text congratulating user
    triggers system exit
    '''
    global endearment
    print(
        f'''
        The date has wrapped up , how do you think it went?
        Your final endearment score was {endearment}...
        Congratulations {user}, you did it!
        {date} has agreed to a second date with you.
        Dating isn't always easy, it can be a minefield sometimes.
        In this scenario, you trusted your instincts,
        you made some tough decisions , and ultimately won the game.
        You should be proud of your victory,
        give yourself a round of applause!
        After building such good first impression,
        the second date should be a piece of cake.
        You and {user} have a bright future ahead of you.
        Well done, and thanks for playing!
        GAME OVER

        '''
        )
    input(" (press enter to clear/exit) :")
    os.system('clear')
    sys.exit()


def game_failure():
    '''
    prints failure text offering commiseration and advice
    triggers system exit
    '''
    global endearment
    print(
        f'''
        The date has wrapped up , how do you think it went?
        Your final endearment score was {endearment}...
        Unfortunately you struck out {user},
        {date} has declined your offer of a second date.
        Don't feel too bad {user}, it just wasn't a match.
        When 2 people are unsuccesful in romance ,
        it is not a failure in character or effort.
        It is simply a fact that these 2 individuals are not compatible.
        Therefore it seen as a victory for both parties,
        it means one or both of you was aware enough,
        had the perception to see it wasn't a good fit.
        Your reward is the freedom to try again,
        to seek out love in any and all places.
        Let the events of this date spur you forward {user},
        have courage, compassion, and empathy in all of
        your future romances.
        And most importantly remember,
        you must learn to love yourself
        before you can learn to love someone else.
        Well done, and thanks for playing!
        GAME OVER
        '''
        )
    input(" (press enter to clear/exit) :")
    os.system('clear')
    sys.exit()
