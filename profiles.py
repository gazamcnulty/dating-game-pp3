import time
import os
import sys
import random


# Here I will store character profiles in dictionaries.

match_1 = {
    "date_name": "Henrietta",
    "vocation": "college student at Trinity College",
    "age": "25",
    "personality":
    '''
    She doesn’t enjoy sports or dancing.
    She prefers long walks with a good podcast.
    Henrietta likes reading science fiction novels
     and playing videogames.
    She also likes wearing cool clothes and following fashion.
    She considers herself introverted however she
    has a few close friends who mean a lot to her.
    ''',
    "likes": '''
    She doesn’t like people who are too silly or
    don’t take themselves seriously.
    She likes people who are honest with her.
    ''',
    "food_preference": "vegetarian",
    "drink_preference": "non-alcoholic",
    "dessert_preference": "Coffee",
}


match_2 = {
    "date_name": "Francis",
    "vocation": " barman who works in a busy pub in Dublin city",
    "age": "29",
    "personality":
    '''
    He loves to work out at the gym and goes for a run every day.
    He’s not really into reading but likes
    playing multiplayer videogames.
    Francis considers himself an extrovert.
    ''',
    "likes": '''
    He likes to spend his free time hanging out with his friends.
    Francis likes getting to know people, he
    likes people who are up for a laugh.
    He enjoys watching some sporting events like UFC MMA and WWE.
    ''',
    "food_preference": "anything with meat / protein",
    "drink_preference": "craft beers",
    "dessert_preference": "chocolate",
}


match_3 = {
    "date_name": "Sarah",
    "vocation": "marketing consultant who works in Dublin.",
    "age": "34",
    "personality":
    '''
    She like to go cycling on the weekends, but
    her real love is film and cinema.
    Sarah has a vast collection of films on dvd.
    She loves to go the Lighthouse Cinema and IFI Cinema.
    Her job is time consuming and demanding,
    she is friendly with coworkers.
    She usually doesn’t have time for romance or catching up with friends.
    ''',
    "likes": '''
    She isn’t into a lot of sports but will watch the Rugby when its on.
    Sarah likes people who aren’t needy.
    They need to respect her autonomy and independence.
    She understands that its ok to have time on your own.
    Sarah doesn’t go to bars much.
    ''',
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
    os.system('cls')
    input("(press enter to continue: )")
    os.system('clear')
    os.system('cls')
    print(
        f'''
        The first match is {match_1["date_name"]}.

        {match_1["date_name"]} is a {match_1["vocation"]}

        {match_1["date_name"]} is {match_1["age"]} years old.

        {match_1["date_name"]}'s personality can be described
        as follows - {match_1["personality"]}

        {match_1["date_name"]}'s likes can be
        described as follows -{match_1["likes"]}

        {match_1["date_name"]}'s favourite food type
        is {match_1["food_preference"]}

        {match_1["date_name"]}'s favourite drink type
        is {match_1["drink_preference"]}

        {match_1["date_name"]}'s favourite thing to have
        after a meal is {match_1["dessert_preference"]}
        '''
        )

    input("Meet your second match? (press enter to continue: )")
    os.system('clear')
    os.system('cls')
    print(
        f'''
        The second match is {match_2["date_name"]}.

        {match_2["date_name"]} is a {match_2["vocation"]}

        {match_2["date_name"]} is {match_2["age"]} years old.

        {match_2["date_name"]}'s personality can be described
        as follows - {match_2["personality"]}

        {match_2["date_name"]}'s likes can be described
        as follows -{match_2["likes"]}

        {match_2["date_name"]}'s favourite
        food type is {match_2["food_preference"]}

        {match_2["date_name"]}'s favourite drink type is

        {match_2["drink_preference"]}

        {match_2["date_name"]}'s favourite thing to have
        after a meal is {match_2["dessert_preference"]}
        '''
        )
    input("Meet your third match? (press enter to continue: )")
    os.system('clear')
    os.system('cls')
    print(
        f'''
        The third match is {match_3["date_name"]}.

        {match_3["date_name"]} is a {match_3["vocation"]}

        {match_3["date_name"]} is {match_3["age"]} years old.

        {match_3["date_name"]}'s personality can be described
        as follows - {match_2["personality"]}

        {match_3["date_name"]}'s likes can be described
        as follows -{match_3["likes"]}

        {match_3["date_name"]}'s favourite
        food type is {match_3["food_preference"]}

        {match_3["date_name"]}'s favourite
        drink type is {match_3["drink_preference"]}

        {match_3["date_name"]}'s favourite thing to have
        after a meal is {match_3["dessert_preference"]}
        '''
        )
    input(" (press enter to continue) :")
    os.system('clear')
    os.system('cls')