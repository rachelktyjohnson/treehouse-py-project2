import constants


def clean_data(local_players):
    """Read existing player data from CONSTANTS into lists nested in dictionaries"""
    clean_players = []
    for player in local_players:

        if player['experience'] == 'YES"':
            experience = True
        else:
            experience = False

            guardians = player['guardians'].split(" and ")

        height = player['height'][:2]

        clean_players.append({
            'name': player['name'],
            'guardians': guardians,
            'experience': experience,
            'height': height
        })

    return clean_players


# Make sure all main calls to my program is protected inside Dunder Main
if __name__ == "__main__":
    print("Script starts here!")
    players = clean_data(constants.PLAYERS)
    print(players)
