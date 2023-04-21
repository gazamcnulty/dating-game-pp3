# imports
import os

# Here I will store character profiles in dictionaries.

match_1 = {
    "date_name": "Henrietta",
    "vocation": "college student at Trinity College",
    "age": "25",
    "personality":
    '''She doesn’t enjoy sports or dancing.
    She prefers long walks with a good podcast.
    She also likes wearing cool clothes and following fashion.
    She considers herself introverted however she
    has a few close friends who mean a lot to her.''',
    "likes":'''
    She doesn’t like people who are too silly
    She likes people who are honest with her.''',
    "food_preference": "vegetarian",
    "drink_preference": "non-alcoholic",
    "dessert_preference": "Coffee",
}


match_2 = {
    "date_name": "Francis",
    "vocation": " barman who works in a busy pub in Dublin city",
    "age": "29",
    "personality":
    '''He loves to work out at the gym every day.
    He’s not really into reading but likes videogames.
    Francis considers himself an extrovert.''',
    "likes":
    '''He likes to spend his free time hanging out with his friends.
    Francis likes getting to know people, he's always up for a laugh.
    He enjoys watching some sporting events like UFC MMA and WWE.''',
    "food_preference": "anything with meat / protein",
    "drink_preference": "craft beers",
    "dessert_preference": "chocolate",
}


match_3 = {
    "date_name": "Sarah",
    "vocation": "marketing consultant who works in Dublin.",
    "age": "34",
    "personality":
    '''She likes to go cycling on the weekends
    Sarah has a vast collection of films on dvd.
    She loves to go the Lighthouse Cinema and IFI Cinema.
    Her job is time consuming and demanding.
    She doesn’t have much time for romance or catching up with friends.''',
    "likes":
    '''She isn’t into a lot of sports but will watch
    the Rugby when its on.
    Sarah likes people who aren’t needy.
    They need to respect her autonomy and independence.
    She understands that its ok to have time on your own.''',
    "food_preference": "lasagne",
    "drink_preference": "cabernet sauvignon",
    "dessert_preference": "ice cream",
}

# Here I will store the function to read and display profiles


def profile_function():
    print(
        '''
        The dating world is a tempestuous place,
        but take heart! You're on the hunt for love.
        There are 3 potential star crossed lovers on the horizon.
        You've matched with all three, so lets get to know them!
        ''')

    input("Are you ready to meet the first match? (press enter to continue: )")
    os.system('clear')
    print(
        f'''
        The first match is {match_1["date_name"]}.
        {match_1["date_name"]} is a {match_1["vocation"]}
        {match_1["date_name"]} is {match_1["age"]} years old.

        personality: {match_1["personality"]}

        likes: {match_1["likes"]}

        favourite food type is {match_1["food_preference"]}
        favourite drink type is {match_1["drink_preference"]}
        favourite thing to have after a meal is {match_1["dessert_preference"]}
        '''
        )

    input("Meet your second match? (press enter to continue: )")
    os.system('clear')
    print(
        f'''
        The second match is {match_2["date_name"]}.
        {match_2["date_name"]} is a {match_2["vocation"]}
        {match_2["date_name"]} is {match_2["age"]} years old.

        personality: {match_2["personality"]}

        likes : {match_2["likes"]}

        favourite food type is {match_2["food_preference"]}
        favourite drink type is {match_2["drink_preference"]}
        favourite thing to have
        after a meal is {match_2["dessert_preference"]}
        '''
        )
    input("Meet your third match? (press enter to continue: )")
    os.system('clear')
    print(
        f'''
        The third match is {match_3["date_name"]}.
        {match_3["date_name"]} is a {match_3["vocation"]}
        {match_3["date_name"]} is {match_3["age"]} years old.

        personality: {match_3["personality"]}

        likes: {match_3["likes"]}

        favourite food type is {match_3["food_preference"]}
        favourite drink type is {match_3["drink_preference"]}
        favourite thing to have 
        after a meal is {match_3["dessert_preference"]}'''
        )
    input(" (press enter to continue) :")
    os.system('clear')