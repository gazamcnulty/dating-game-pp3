'''
Imports
'''
import functions
import profiles


print(
    '''
    ███ █┼█ ███ ┼┼ ██▄ ███ ███ ███ █┼┼█ ████ ┼┼ ████ ███ █▄┼▄█ ███
    ┼█┼ █▄█ █▄┼ ┼┼ █┼█ █▄█ ┼█┼ ┼█┼ ██▄█ █┼▄▄ ┼┼ █┼▄▄ █▄█ █┼█┼█ █▄┼
    ┼█┼ █┼█ █▄▄ ┼┼ ███ █┼█ ┼█┼ ▄█▄ █┼██ █▄▄█ ┼┼ █▄▄█ █┼█ █┼┼┼█ █▄▄
    '''
    )

def main():
    '''
    Holds all function calls
    '''

    functions.new_game()
    functions.rules()
    profiles.profile_function()
    functions.date_who()
    functions.date_when()
    functions.date_start()
    functions.menu_choice()
    functions.beverage_choice()
    functions.observation_chat()
    functions.talk_about_me()
    functions.eat_meal()
    functions.random_encounter()
    functions.spontaneous()
    functions.dessert()
    functions.bill()
    functions.goodbye()

main()
