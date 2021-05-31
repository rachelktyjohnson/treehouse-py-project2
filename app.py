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
        height = player['height'][:2]

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


# Make sure all main calls to my program is protected inside Dunder Main
if __name__ == "__main__":

    #  Grab the data and clean it
    players = clean_data(constants.PLAYERS)

    #  Sort players into teams accordingly
    teams = balance_teams(constants.TEAMS, players)

    #  Start text
    print("\n└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print("BASKETBALL TEAM STATS TOOL\n")
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
    else:
        print("\nThanks for using the BASKETBALL TEAM STATS TOOL, goodbye!")
        print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
