import random
from enemy import Enemy
from combat import Combat

class Encounters:
    def __init__(self, player_instance, step:int):
        self.player_instance = player_instance

    @staticmethod
    def print_health(player_instance):
        print(f"Your Health is now {player_instance.health}")   

    @staticmethod
    def check_for_encounter(player_instance,step:int):

        if step not in [25,50,75,99,100]:
            encounter_check = random.uniform(0, 1)

            if 0 <= encounter_check < 0.125:  # First 12.5% range
                EnemyEncounters.enemy_encounter(player_instance)
                __class__.print_health(player_instance)
                
            elif 0.125 <= encounter_check < 0.25:  # Second 12.5% range
                RestEncounters.rest_encounter(player_instance)
                __class__.print_health(player_instance)
                
            elif 0.25 <= encounter_check < 0.30:  # 5% Chance
                MysteryEncounters.mystery_encounter(player_instance)
                __class__.print_health(player_instance)
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

    
class RestEncounters(Encounters):
    def __init__(self, player_instance):
        super().__init__(player_instance)
    
    @classmethod
    def rest_encounter(self ,player_instance):
        rest_chance = random.randint(0,3)
        if rest_chance == 0 or 1:
            player_instance.heal(5)
            print("You Find a Tavern and Rest for a short time")
        elif rest_chance == 2:
            player_instance.heal(7)
            print("You Find an Inn and Rest for the evening")
        elif rest_chance == 3:
            player_instance.heal(9)
            print("You Find the King's Vassal's Keep, and take a day to rest.")
            while player_instance.potions > 9 and player_instance.gold != 0:
                player_instance.gold -= 25
                player_instance.potions += 1
                print(f"You purchase a potion. You now have {player_instance.potions}")


class EnemyEncounters(Encounters):
    def __init__(self, player_instance):
        super().__init__(player_instance)
    
    @classmethod
    def enemy_encounter(self, player_instance):
        enemy_chance = random.randint(0,4)
        if enemy_chance == 0 or 1:
            small_enemy = Enemy(name="Feral Imp", health=8, strength=1, intellect=3, attack_name="fireball")
            print(f"You encounter a {small_enemy.name}!")
            enemy_instance = small_enemy
        elif enemy_chance == 2 or 3:
            medium_enemy = Enemy(name="Dire Wolf", health=15, strength=5, intellect=3, attack_name="Wolf Bite")
            print(f"You encounter a {medium_enemy.name}!")
            enemy_instance = medium_enemy
        elif enemy_chance == 4:
            large_enemy = Enemy(name="Cave Troll", health=30, strength=10, intellect=1, attack_name="Club Smash")
            print(f"You encounter a {large_enemy.name}!")
            enemy_instance = large_enemy

        Combat.combat(player_instance, enemy_instance)



class MysteryEncounters(Encounters):
    def __init__(self, player_instance):
        super().__init__(player_instance)
    
    @classmethod
    def mystery_encounter(self, player_instance):
        print("You Encounter A Strange Figure!")
        mystery_chance = random.randint(0,1)
        if mystery_chance == 0:
            player_instance.heal(3)
            print("The Figure heals you and vanishes into the darkness!")
        else:
            player_instance.damage(3)
            print("The Figure blasts you with an Arcane Bolt and vanishes into a Flash of Light!", end="\n\n")

class SpecialEncounters(Encounters):
    def __init__(self, player_instance, step: int):
        super().__init__(player_instance, step)

    @classmethod
    def friendly_keep_visit(self, player_instance):
        print("You are welcomed to the Friendly Keep")
        print("You are fully rested and have a full stock of potions", end="\n\n")
        player_instance.heal(30)
        player_instance.potions = 5

    @classmethod
    def midway_boss(self, player_instance):
        wizard = Enemy(name="Cobolus The Wizard",health=15, strength=4, intellect=8, attack_name="Arcane Firestorm")
        print(f"You encounter {wizard.name}!")
        enemy_instance = wizard
        Combat.combat(player_instance, enemy_instance)

    @classmethod
    def enemy_keep_visit(self, player_instance):
        print("You must traverse Algolon's Keep!")
        sub_step = 0
        while sub_step < 10:
            sub_step += 1
            print(sub_step)
            dungeon_chance = random.randint(0,5)
            match dungeon_chance:
                case 0:
                    player_instance.potions += 2
                    player_instance.heal(2)
                    print("You find a Store Room with some food & potions")
                case 1:
                    sub_step += 2
                    print("You find a Secret Passage!")
                case 4:
                    mage = Enemy(name="Acolyte of Algolon", health=8, strength=3, intellect=7, attack_name="Arcane Bolt")
                    print(f"You encounter an {mage.name}!")
                    enemy_instance = mage
                    Combat.combat(player_instance, enemy_instance)
            if player_instance.health == 0:
                break
        print("At the end of the Keep you encounter Algolon's Arch Mage!")
        arch_mage = Enemy(name="Algolon's Arch Mage", health=20, strength=4, intellect=10, attack_name="Arcane Lightning")
        enemy_instance = arch_mage
        Combat.combat(player_instance, enemy_instance)

    @classmethod
    def penultimate_boss(self, player_instance):
        great_wizard = Enemy(name="The Great Wizard Algolon", health=25, strength=5, intellect=12, attack_name="Cosmic Collision")
        print(f"You Battle {great_wizard.name}!")
        enemy_instance = great_wizard
        Combat.combat(player_instance, enemy_instance)

    @classmethod
    def final_boss(self, player_instance):
        dragon = Enemy(name="Fortranus the Ancient One", health=40, strength=14, intellect=10, attack_name="Dragon Fire")
        print(f"You battle must now battle {dragon.name}!")
        enemy_instance = dragon
        Combat.combat(player_instance, enemy_instance)