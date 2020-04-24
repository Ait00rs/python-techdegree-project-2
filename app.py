import constants
import copy
import random


# copying data from constants.py so that original data would not be modified.
my_teams = copy.deepcopy(constants.TEAMS)
my_players = copy.deepcopy(constants.PLAYERS)


"""
Clean up data:
clear_data() function cleans data from the original constants.py
data collection. Experience converted to boolean: True if YES or
False if NO. Height converted to an integer.
"""


def clear_data():
    for data in my_players:
        data['height'] = int(data['height'][:2])
        data['guardians'] = data['guardians'].split(' and ')
        if data['experience'] == 'NO':
            data['experience'] = False
        else:
            data['experience'] = True

    return my_players


"""
Team balancing:
player_balance() function assigns players to each team so that all three teams
are evenly balanced by the total number of players.

Using Methods: randrange() + pop() from
https://www.geeksforgeeks.org/python-remove-random-element-from-list/
"""
team_pan = []
team_war = []
team_ban = []


def player_balance(team):
    while len(my_players) != 0 and len(team) < 6:
        team.append((my_players.pop(random.randrange(len(my_players)))))
    return team


"""
Display teams:
teams_list() function displays teams in a list.
"""


def teams_list():
    for index, item in enumerate(my_teams, 1):
        print(f'     {index}. {item}')


"""
Display players list:
players_list() function displays selected team players in a list.
"""


def players_list(selected_team):
    selected_player_list = []
    for player in selected_team:
        if player['name']:
            selected_player_list.append((player['name']))

    return ", ".join(selected_player_list)


"""
Display the stats:
team_stats() displaying selected team stats
"""


def team_stats(team_position_in_list, balanced_team):
    print(f'\n Team: {my_teams[team_position_in_list]} Stats:')
    print(' ---------------------')
    print(f' Total players: {len(balanced_team)}')
    print('\n Player on Team:')
    print(f' {players_list(balanced_team)}')

# tool_name() function prints out tool name


def tool_name():
    print("""
--------------------------
BASKETBALL TEAM STATS TOOL
--------------------------
     === MENU ===
""")


# menu() function displays menu


def menu():
    print(' Here are your options:')
    print('     1. Show Teams')
    print('     2. Quit')


# Basketbal Team Stats tool starts here
if __name__ == '__main__':
    # tool_name() function prints out tool name
    tool_name()

    # calling menu() function to load menu to the user
menu()

# calling below functions to clean data and assig players to each team
clear_data()
player_balance(team_pan)
player_balance(team_war)
player_balance(team_ban)

# starting loop to evaluate user selection from menu
while True:
    try:
        # prompting user to select an option from menu
        user_selection = int(
            input("\n Please select between option 1 or 2 and press ENTER to continue: "))
    except ValueError:
        print(" Oh no! That's not a valid value. Try again...")
    else:
        # option 2 quits tool
        if user_selection == 2:
            print('\n Quiting....')
            break
        #  option 1 loads team list
        if user_selection == 1:
            while True:
                # teams_list() loading team list
                teams_list()
                try:
                    # prompting the user to pick a team and handling errors if any
                    user_team_selection = int(
                        input("\n Please select a team and enter team number and press ENTER to continue: "))
                except ValueError:
                    print(" Oh no! Please choose between 1, 2 or 3. Try again...")
                    continue
                else:
                    if user_team_selection > 3 or user_team_selection < 1:
                        print(" Oh no! Please choose between 1, 2 or 3. Try again...")
                        continue
                    # displaying selected team stats
                    elif user_team_selection == 1:
                        team_position_in_list = 0
                        balanced_team = team_pan
                        team_stats(team_position_in_list, balanced_team)
                    elif user_team_selection == 2:
                        team_position_in_list = 1
                        balanced_team = team_war
                        team_stats(team_position_in_list, balanced_team)
                    elif user_team_selection == 3:
                        team_position_in_list = 2
                        balanced_team = team_ban
                        team_stats(team_position_in_list, balanced_team)
                    break
    # after team stats are displayed, prompting user to continue
    input('\n Press ENTER to continue...')
    print('')
    menu()
