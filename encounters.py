import random
from encounter_rest import RestEncounters
from encounter_enemy import EnemyEncounters
from encounter_special import SpecialEncounters
from encounter_mystery import MysteryEncounters

def check_for_encounter(player_instance,step:int):

    if step not in [25,50,75,99,100]:
        encounter_check = random.uniform(0, 1)

        if 0 <= encounter_check < 0.125:  # First 12.5% range
            EnemyEncounters.enemy_encounter(player_instance)
            
        elif 0.125 <= encounter_check < 0.25:  # Second 12.5% range
            RestEncounters.rest_encounter(player_instance)
            
        elif 0.25 <= encounter_check < 0.30:  # 5% Chance
            MysteryEncounters.mystery_encounter(player_instance)
    else:              
        match step:
            case 25:
                SpecialEncounters.friendly_keep_visit(player_instance)
            case 50:
                SpecialEncounters.midway_boss(player_instance)
            case 75:
                SpecialEncounters.enemy_keep_visit(player_instance)
            case 99:
                SpecialEncounters.penultimate_boss(player_instance)
            case 100:
                SpecialEncounters.final_boss(player_instance)
            case _:
                print("""
                        The world goes black and You awaken in a cart, with your hands bound. 
                        
                        A man calls to you and says:
                        
                        'Hey You! Finally Awake!
                        """)