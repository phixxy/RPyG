from interaction import Interaction
from display import Display
import random
import json

class Combat:
    def __init__(self, player_instance, enemy_instance):
        self.player_instance = player_instance
        self.enemy_instance = enemy_instance
    
    def battle(player_instance, enemy_instance):
        while enemy_instance.health != 0:
            Display.battle_hud_message(player_instance=player_instance,enemy_instance=enemy_instance)
            player_action = Interaction.in_battle(player_instance)
            match player_action:
                case "ATTACK":
                      __class__._player_attack(player_instance, enemy_instance)
                case "HEAL":
                    player_instance.use_potion()
            ## End Battle If Enemy dies
            if enemy_instance.health == 0:
                break
            
            ## Follower Actions
            if player_instance.has_follower == True:
                follower_action = Interaction.in_battle(player_instance.follower_instance)
                match follower_action:
                    case "ATTACK":
                        __class__._follower_attack(player_instance.follower_instance, enemy_instance)
                    case "HEAL":
                        player_instance.follower_instance.use_potion()
            
            ## Enemy Attacks
            if player_instance.has_follower == True:
                set_target = random.randint(0,1)
                if set_target == 0:
                    target = player_instance
                elif set_target == 1:
                    target = player_instance.follower_instance
            else:
                target = player_instance
            
            __class__._enemy_attack(target, enemy_instance)
            ## Remove Follower if they die
            if player_instance.has_follower == True:
                if player_instance.follower_instance.health == 0:
                    player_instance.lose_follower(player_instance.follower_instance)
            ## End combat if player dies
            if player_instance.health == 0:
                break

        ## Display Victory Message if player does not die
        player_post_action = ""
        if player_instance.health != 0 and enemy_instance.health == 0:
            Display.defeated_message(enemy_instance)
            while player_post_action != "TRAVEL":
                player_post_action = Interaction.post_battle(player_instance)
                if player_post_action == "HEAL":
                    player_instance.use_potion()
                if player_post_action == "SAVE":
                    # Open the file in write mode. If the file doesn't exist, it will be created.
                    # If it does exist, it will be overwritten.
                    with open('savegame.rpygs', 'w') as file:
                        # Write some text to the file.
                        json.dump(player_instance.__dict__,file, indent=4)
                        exit()
                        # The file is automatically closed when you exit the 'with' block.

                    



    ## Hidden Methods
    def _player_attack(player_instance, enemy_instance):
        if __class__._check_for_critical(player_instance) == True:
            Display.player_critical_attack_message(player_instance)
            enemy_instance.damage(player_instance.attack_power * 2)
        else:
            Display.player_attack_message(player_instance)
            enemy_instance.damage(player_instance.attack_power)
            Display.actor_health_message(enemy_instance)

    def _enemy_attack(player_instance, enemy_instance):
        if __class__._check_for_critical(enemy_instance) == True:
            Display.actor_critical_attack_message(enemy_instance)
            player_instance.damage(enemy_instance.attack_power)
        else:
            Display.actor_attack_message(enemy_instance)
            player_instance.damage(enemy_instance.attack_power)
        Display.actor_health_message(player_instance) 

    def _follower_attack(follower_instance, enemy_instance):
        if __class__._check_for_critical(follower_instance) == True:
            Display.actor_critical_attack_message(follower_instance)
            enemy_instance.damage(follower_instance.attack_power * 2)
        else:
            Display.actor_attack_message(follower_instance)
            enemy_instance.damage(follower_instance.attack_power)
        Display.actor_health_message(enemy_instance)

    @staticmethod
    def _check_for_critical(combatant_instance):
        crit_check = random.randint(1,100)
        if crit_check <= combatant_instance.luck:
            return True
        else:
            return False