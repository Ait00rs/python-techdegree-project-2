import constants
import random


# copying lists created data from constants.py would not be modify or mutate.
teams = constants.TEAMS
players = constants.PLAYERS


"""
Clean up data:
clear_data() function cleans data from the original constants.py
data collection. Experience converted to boolean: True if YES or
False if NO. Height converted to an integer.
"""


def clear_data():
    for data in players:
        data['height'] = int(data['height'][:2])
        data['guardians'] = data['guardians'].split(' and ')
        if data['experience'] == 'NO':
            data['experience'] = False
        else:
            data['experience'] = True

    return players


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
    while len(players) != 0 and len(team) < 6:
        team.append((players.pop(random.randrange(len(players)))))
    return team


"""
Display teams:
teams_list() function displays teams in a list.
"""


def teams_list():
    for index, item in enumerate(teams, 1):
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


# menu() function displays menu


def menu():
    print('     === MENU ===    ')
    print(' Here are your options:')
    print('     1. Show Teams')
    print('     2. Quit')


# Basketbal Team Stats tool starts here
if __name__ == '__main__':
    print("""
--------------------------
BASKETBALL TEAM STATS TOOL
--------------------------
""")

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
        user_selection = int(input("\n Please select between option 1 or 2: "))
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
                        input("\n Please select a team and enter team number: "))
                except ValueError:
                    print(" Oh no! Please choose between 1, 2 or 3. Try again...")
                    continue
                else:
                    if user_team_selection > 3 or user_team_selection < 1:
                        print(" Oh no! Please choose between 1, 2 or 3. Try again...")
                        continue
                    # below code-blocks loading of team stats based on users selection
                    elif user_team_selection == 1:
                        print(f'\n Team: {teams[0]} Stats:')
                        print(' ---------------------')
                        print(f' Total players: {len(team_pan)}')
                        print('\n Player on Team:')
                        print(f' {players_list(team_pan)}')
                    elif user_team_selection == 2:
                        print(f'\n Team: {teams[1]} Stats:')
                        print(' ---------------------')
                        print(f' Total players: {len(team_war)}')
                        print('\n Player on Team:')
                        print(f' {players_list(team_war)}')
                    elif user_team_selection == 3:
                        print(f'\n Team: {teams[2]} Stats:')
                        print(' ---------------------')
                        print(f' Total players: {len(team_ban)}')
                        print('\n Player on Team:')
                        print(f' {players_list(team_ban)}')
                    break
    # after team stats are printed, prompting user to continue/quit
    next_team = input("\n Would you like to continue? [y]es/[n]o: ")
    if next_team.lower() == "y":
        menu()
    else:
        print('\n Quiting....')
        break
