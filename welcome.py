from interaction import Interaction
from display import Display

def welcome():
    print("Welcome to RPyG, a text based RPG in Python", end="\n\n")

    mode_choices = ["AUTO", "MANUAL"]
    mode_message = """
Please Select your Game mode:
Options are : Manual & Auto


Note: All Prompts in this game are case insensitive

"""
    game_mode = Interaction.validate_input(mode_choices, mode_message)
    Interaction.global_game_mode = game_mode

    
def player_start():
    player_name = ""
    player_name_message = """
Now before your Journey Can Begin Please enter the name of your Character


Note: Case is respected but names longer than 32 Characters will be truncated

"""
    if Interaction.global_game_mode == "MANUAL":
            player_name = Interaction._sanitize(str(input(f"{player_name_message}"))[:32])
    else:
            player_name = "The Protagonist"
    return player_name



def multiplayer_start(): ## Unused for now, pending other changes to the gameplay
    players = []
    count_choices = ["1","2","3","4"]
    count_message = """
Choose the number of players:
1
2
3
4

    """
    player_count = int(Interaction.validate_input(count_choices, count_message))
    Interaction.global_player_count = player_count

    player_name_message = """
Now before your Journey Can Begin Please enter the name of your Character


Note: Case is respected but names longer than 32 Characters will be truncated

"""

    if Interaction.global_game_mode == "MANUAL":
        for count in range(0,Interaction.global_player_count):
            player_name = str(input(f"{player_name_message}"))[:32]
            players.append(player_name)
    else:
         for count in range(0,Interaction.global_player_count):
            players.append(f"The Protagonist{count}")

    return players