from actors.actor import Actor

#Only for Type Checking/Hinting
from actors.actor_playable import PlayableActor
from actors.actor_enemy import Enemy


class Party:
    def __init__(self, members:list[Actor]) -> None:
        if not isinstance(members, list):
            raise ValueError("The 'members' parameter must be of type list. Received type: {}".format(type(members).__name__))
        for party_member in members:
            if not isinstance(party_member, Actor):
                raise ValueError("The 'party_member' parameter must be of type Actor. Received type: {}".format(type(party_member).__name__))

        self.members = members

    def lose_member(self, member) -> None:
        self.members.remove(member)
    
    def gain_member(self, member) -> None:
        self.members.append(member)

class PlayerParty(Party):
    """
    Stores the progress of the party, and a list/array of member instances 
    """

    def __init__(self, name:str, members:list[PlayableActor]) -> None:
        if not isinstance(name, str):
            raise ValueError("The 'name' parameter must be of type str. Received type: {}".format(type(name).__name__))
        if not isinstance(members, list):
            raise ValueError("The 'members' parameter must be of type list. Received type: {}".format(type(members).__name__))
        for party_member in members:
            if not isinstance(party_member, PlayableActor):
                raise ValueError("The 'party_member' parameter must be of type Actor. Received type: {}".format(type(party_member).__name__))
        
        Party.__init__(self, members=members)
        self.progress = 0
        self.name = name
        self.members = members


class EnemyParty(Party):
    def __init__(self, name:str, members:list[Enemy]) -> None:
        if not isinstance(name, str):
            raise ValueError("The 'name' parameter must be of type str. Received type: {}".format(type(name).__name__))
        if not isinstance(members, list):
            raise ValueError("The 'members' parameter must be of type list. Received type: {}".format(type(members).__name__))
        for party_member in members:
            if not isinstance(party_member, Enemy):
                raise ValueError("The 'party_member' parameter must be of type Actor. Received type: {}".format(type(party_member).__name__))
        
        Party.__init__(self, members=members)
        self.name = name
        self.members = members