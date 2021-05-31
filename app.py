import constants


def clean_data(local_players):
    """Read existing player data from CONSTANTS into lists nested in dictionaries"""
    clean_players = []
    for player in local_players:

        #  clean experience variable
        if player['experience'] == 'YES':
            experience = True
        else:
            experience = False

        #  clean guardian variable
        guardians = player['guardians'].split(" and ")

        #  clean height variable
        height = int(player['height'][:2])

        #  add clean player data to return variable
        clean_players.append({
            'name': player['name'],
            'guardians': guardians,
            'experience': experience,
            'height': height
        })

    return clean_players


def balance_teams(local_teams, local_players):
    """Assigns players into teams so the teams are evenly balanced on numbers and experienced vs non-experienced"""

    balanced_teams = {}

    for local_team in local_teams:
        balanced_teams[local_team] = []

    #  First sort by experience
    local_players_exp = []
    local_players_noexp = []

    for player in local_players:
        if player['experience']:
            local_players_exp.append(player)
        else:
            local_players_noexp.append(player)

    local_players_sorted = local_players_exp + local_players_noexp

    while len(local_players_sorted) > 0:
        for team_name in balanced_teams:
            balanced_teams[team_name].append(local_players_sorted.pop(0))

    return balanced_teams


def show_menu():
    print("---- MENU ----\n")
    print("Here are your choices:\n")
    print("   1) Display Team Stats")
    print("   2) Quit")

    #  Ask for option input
    option = input("\nEnter an option (1/2): ")

    #  Loop until the entry is valid
    while (option != '1') and (option != '2'):
        print("\nSelection must be 1 or 2. Try again.")
        option = input("Enter an option (1/2): ")

    if option == '1':
        print("\nSELECT A TEAM TO VIEW\n")
        for i, team in enumerate(teams, 1):
            print(f'   {i}) {team}')

        selection = input("\nEnter an option (1/2/3): ")
        while (selection != '1') and (selection != '2') and (selection != '3'):
            print("\nSelection must be 1, 2 or 3. Try again.")
            selection = input("Enter an option (1/2/3): ")

        if selection == '1':
            display_stats(teams['Panthers'], "Panthers")
        elif selection == '2':
            display_stats(teams['Bandits'], "Bandits")
        elif selection == '3':
            display_stats(teams['Warriors'], "Warriors")
        local_choice = input("\nPress any key to continue, or EXIT to stop program: ")
        local_choice = local_choice.upper()
        return local_choice
    else:
        return "EXIT"


def display_stats(local_team, team_name):
    print("\n-----")
    print(team_name.upper())
    print("-----\n")
    total_players = len(local_team)

    exp_players = 0
    noexp_players = 0
    total_height = 0
    players_list = []
    guardians_list = []

    for player in local_team:
        total_height = total_height + player['height']
        players_list.append(player['name'])
        all_guardians = ", ".join(player['guardians'])
        guardians_list.append(all_guardians)
        if player['experience']:
            exp_players = exp_players + 1
        else:
            noexp_players = noexp_players + 1

    team_height = round(total_height/total_players, 2)

    print(f'Total players: {total_players}')
    print(f'Total experienced: {exp_players}')
    print(f'Total inexperienced: {noexp_players}')
    print(f'Average height: {team_height}')

    print("Players on team:")
    players_str = ", ".join(players_list)
    print(players_str)

    print("\nTeam Guardians: ")
    guardians_str = ", ".join(guardians_list)
    print(guardians_str)


# Make sure all main calls to my program is protected inside Dunder Main
if __name__ == "__main__":

    #  Grab the data and clean it
    players = clean_data(constants.PLAYERS)

    #  Sort players into teams accordingly
    teams = balance_teams(constants.TEAMS, players)
    #  Start text
    print("\n└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print("BASKETBALL TEAM STATS TOOL\n")
    choice = show_menu()
    while choice != "EXIT":
        choice = show_menu()

    print("\nThanks for using the BASKETBALL TEAM STATS TOOL, goodbye!")
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
