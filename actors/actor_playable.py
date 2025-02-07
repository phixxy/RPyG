import random
from logging.logging import write_log
from actors.actor import Actor
from actors.actor_combatant import Combatant


class Inventory:
    def __init__(self, gold:int, potions:int) -> None:
        if not isinstance(gold, int):
            raise ValueError("The 'gold' parameter must be of type int. Received type: {}".format(type(gold).__name__))
        if not isinstance(potions, int):
            raise ValueError("The 'potions' parameter must be of type int. Received type: {}".format(type(potions).__name__))
        
        self.gold = gold
        self.potions = potions

    def gain_gold(self, amount:int) -> None:
        self.gold += amount

    def spend_gold(self, amount:int) -> bool:
        if self.gold < amount:
            print(f"{self.name} has insufficient gold")
            return False
        else:
            __class__.lose_gold(self, amount)
            return True
    
    def lose_gold(self, amount:int) -> None:
            self.gold -= amount
            if self.gold < 0:
                self.gold = 0
                print(f"{self.name} has no gold remaining")
            write_log(f"Player now has {self.gold} gold")
                
        

    def gain_potion(self, amount:int) -> None:
        self.potions += amount
    
    def lose_potion(self, amount:int) -> None:
        self.potions -= amount

class PlayableActor(Actor, Inventory, Combatant):
    def __init__(self, name: str, specialization: str) -> None:
        if not isinstance(name, str):
            raise ValueError("The 'name' parameter must be of type str. Received type: {}".format(type(name).__name__))
        if not isinstance(specialization, str):
            raise ValueError("The 'specialization' parameter must be of type str. Received type: {}".format(type(specialization).__name__))

        self.name = name
        self.specialization = specialization
                 

        match specialization:
            case "WARRIOR":
                strength = random.randint(5,10)
                intellect = random.randint(1,5)
                agility = random.randint(4,8)
                luck = random.randint(1,10)
            case "MAGE":
                strength = random.randint(1,5)
                intellect = random.randint(5,10)
                agility = random.randint(4,8)
                luck = random.randint(1,10)
            case "ROGUE":
                strength = random.randint(4,8)
                intellect = random.randint(4,8)
                agility = random.randint(5,10)
                luck = random.randint(1,10)
            case _:
                print(f"Error Invalid Specialization {specialization}")
                exit()
        
    ## Init Inherited Classes
        Actor.__init__(self, 
                       name=name,
                       strength=strength, 
                       intellect=intellect, 
                       agility=agility, 
                       luck=luck)

        Inventory.__init__(self, 
                           gold=strength * 25, 
                           potions=int(intellect / 2) 
                           )
        
        Combatant.__init__(self, 
                           health=100 + int((strength + intellect) * 10),
                           attack_name=__class__.__set_attack_name(self),
                           attack_power=__class__.__set_attack_power(self)
                           )
        write_log(f"Player: {self.name} was created with {self.gold} gold and {self.potions} potions")
    

    def use_potion(self) -> None:
        if self.potions != 0:
            print(f"{self.name} drinks a potion")
            self.lose_potion(1)
            self.heal(100 + random.randint(-20,20))
            print(f"{self.name} has {self.potions} remaining")
            print(f"{self.name}'s health is now {self.health}", end="\n\n")
        else:
            print(f"{self.name} has no remaining potions!")

    def __set_attack_power(self) -> int:
        if self.strength > self.intellect:
            self.attack_power = self.strength
        elif self.strength >= 7 and self.intellect >= 7:
            self.attack_power = int(self.strength + self.intellect * .75)
        else:
            self.attack_power = self.intellect

        return self.attack_power * 10

    def __get_skill(self) -> str:
        strength_skill = ""
        intellect_skill = ""
        player_skill = ""

        if self.strength in range(1, 4):
            strength_skill = "weak"
        elif self.strength in range(4, 7):
            strength_skill = "fair"
        elif self.strength in range(7, 10):
            strength_skill = "strong"
        elif self.strength == 10:
            strength_skill = "mighty"

        if self.intellect in range(1, 4):
            intellect_skill = "dull"
        elif self.intellect in range(4, 7):
            intellect_skill = "ordinary"
        elif self.intellect in range(7, 10):
            intellect_skill = "smart"
        elif self.intellect == 10:
            intellect_skill = "brilliant"
                
        player_skill = str(f"{strength_skill}:{intellect_skill}")

        return player_skill
    
    def __set_attack_name(self) -> str:
        player_skill = __class__.__get_skill(self)

        match player_skill:
            case "weak:dull":
                self.attack_name = "Clumsy Punch"
            case "fair:dull":
                self.attack_name = "Axe Chop"
            case "strong:dull":
                self.attack_name = "Warhammer Slam"
            case "mighty:dull":
                self.attack_name = "Greatsword Cleave"

            case "weak:ordinary":
                self.attack_name = "Dagger Slash"
            case "fair:ordinary":
                self.attack_name = "Shortsword Slash"
            case "strong:ordinary":
                self.attack_name = "Longsword Thrust"
            case "mighty:ordinary":
                self.attack_name = "Greatsword Thrust"

            case "weak:smart":
                self.attack_name = "Arcane Bolt"
            case "fair:smart":
                self.attack_name = "Fireball"
            case "strong:smart":
                self.attack_name = "Arcane Longsword Strike"
            case "mighty:smart":
                self.attack_name = "Arcane Greatsword Cleave"

            case "weak:brilliant":
                self.attack_name = "Arcane Lighting"
            case "fair:brilliant":
                self.attack_name = "Great Fireball"
            case "strong:brilliant":
                self.attack_name = "Seismic Hammer Slam"
            case "mighty:brilliant" :
                self.attack_name = "Cosmic Greatsword Cleave"

        return self.attack_name
    
    def __get_attack_name(self) -> str:

        match self.specialization:
            case "WARRIOR":
                if self.intellect >= 7:
                    attack = "Arcane Greatsword Cleave"
                else:
                    attack = "Greatsword Cleave"
                
                #min str: 5
                #max str: 10

                #min int: 1
                #max int: 5 

                #min agl: 4
                #max agl: 8
            case "MAGE":
                if self.strength >= 7:
                    attack = "Arcane Shockwave"
                else:
                    attack = "Arcane Bolt"
                #min str: 1
                #max str: 5

                #min int: 5
                #max int: 10 
                
                #min agl: 4
                #max agl: 8
            case "ROGUE":
                if self.intellect >= 7 and self.strength >= 7:
                    attack = "Cool Attack"
                else:
                    attack = "Precision Dagger Strike"
                #min str: 4
                #max str: 8

                #min int: 4
                #max int: 8 
                
                #min agl: 5
                #max agl: 10
            case _:
                print(f"Error Invalid Specialization {self.specialization}")
                exit()