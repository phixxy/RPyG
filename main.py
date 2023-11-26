import pickle
from actors.actor_player import Player
from message.message import Message
from interaction.interaction import Interaction
from encounters.encounter import check_for_encounter
from welcome import welcome, player_start, get_start_type

welcome()
if Interaction.global_game_mode == "MANUAL":
    match get_start_type():
        case "LOAD":
            with open('savegame.rpygs', 'rb') as file:
                # Write some text to the file.
                player_instance = pickle.load(file) #(maybe some way to make that safer or add a checksum or hash could be fun)
                print(f"Successfully Loaded Save Game for: {player_instance.name}")
        case "NEW":
            player_name = player_start()
            player_instance = Player(name=player_name)
else:
    player_instance = Player(name="The Protagonist")



while player_instance.progress < 100:
    player_instance.progress += 1
    Message.player_progress_message(player_instance)
    check_for_encounter(player_instance)
    if player_instance.health == 0:
        print(f"{player_instance.name} has fallen in combat after {player_instance.progress * 10} miles" , end='\n\n')
        break




Message.post_game_recap(player_instance)


### TODO expand merchant system

### TODO expand enemy system
    ### TODO Multi Enemy Encouters

### TODO add Defend & Dodge Options to combat

### Add interaction to rest encounters

### Remove direct prints from rest and mystery encounters

### Template and Json-ize rest and mystery encounters
### Move display functions into smaller sub classes (like encounters)
### Move interaction functions into smaller sub classes

### IDEA Centralize json stores in story directory?