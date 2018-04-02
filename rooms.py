import mechanicsFork
from mechanicsFork import Player
import random

entrance_description = """
Dungeon Entrance:
You are at the entrance of a dungeon, you feel a soft draft coming from
the doorway in front of you.
exits: n
"""

stairwell_description = """
Stairwell:
You are at the top of a stairwell. It is too dark to see what is at
the bottom of the stairs.
exits: d, s
"""

hallway_description = """
Hallway:
You are at the end of a hallway lit up by torches.
All of the doors here appear to be locked locked except for the
door at the end.
exits: n, u
"""

dininghall_description = """
Dining Hall:
Rotten food line all of the tables here.
There is a door to your left and right.
exits: w, e, s
"""

lounge_description = """
Lounge:
You see a bunch of chairs and rotten food here.
This is probably where everyone stayed before they disappeared.
There is a secured door north.
exits: n, e
"""

office_description = """
Warden's office:
The walls are lined with keys to cells.
In the back of the room sits the warden's desk
exits: s
"""

cellhall_description = """
Cell Hall:
Cells line the walls of this hall.
Everyone here has rotted away and all the cells are mostly empty, but you notice a hole in the wall of one of the cells.
The cells here are locked.
exits: n, w
"""

cell_description = """
Cell:
This cell is quite barren except for a bucket and a pillow.
There is a large hole in one of the walls.
exits: w, s
"""

teleporter_description = """
Teleporter:
Blinking lights and switches line all of the walls in this room.
There is an energetic portal north
exits: n, e
"""

lobby_description = """
Lobby:
There is a coffee table in the center of this room, and a T.V. playing monty python.
To your left you see a tarp covering an entrance,
and to your right you see thick foliage.
There is a door with 2 keycard slots in front of you.
exits: n, e, s, w
"""

construction_description = """
Construction Area:
You see a bunch of bare rebar laying around.
It looks like a building in the process of being built.
exits: e
"""

jungle_description = """
Jungle:
It is hard to see with all the foliage here.
Almost every surface of the floor is covered in punji traps,
and there are trees everywere.
exits: w
"""

finalroom_description = """
The End:
You manage to stand up even though there is no floor here.
It appears as if everything here is made of galaxies.
"""
Rat = mechanicsFork.Character("Ravio", 2, 15, 10, 2, 12, 2, [1, 4], 14, 4, 1)
Rat.hp = 1
Rat.death_quote = "The goblin screeches as it perishes"
rat_alive = 1
dininghall_potion = 1
print(entrance_description)
Warden = mechanicsFork.Character("Atrienus", 13, 11, 12, 10, 9, 8, [1, 4], 16, 8, 1)
Warden.hp = 6
Warden.death_quote = "The warden says, \"And finally, I may rest\" as he dies"
warden_alive = 1
Skeleton = mechanicsFork.Character("The skeleton", 13, 11, 12, 10, 9, 8, [1, 4], 16, 8, 1)
Skeleton.hp = 6
Skeleton.death_quote = "The skeleton collapses into a pile of bones"
skeleton_alive = 1
Toni = mechanicsFork.Character("Toni Kong", 17, 11, 12, 8, 7, 6, [2, 4], 13, 8, 2)
Toni.hp = 10
Toni.death_quote = 'Toni Kong says, "The zone wasn\'t enough to save me" as he falls of the girder.'
toni_alive = 1
Caleb = mechanicsFork.Character("Caleb", 13, 13, 10, 10, 9, 8, [1, 8], 15, 8, 2)
Caleb.hp = 8
Caleb.death_quote = "Caleb says, \" I have all these punji traps, but I never had a trap gf\" as he dies"
caleb_alive = 1
lobby_potions_taken = 0
Master = mechanicsFork.Character("GM", 15, 15, 15, 15, 15, 15, [2, 5], 16, 10, 3)
Master.death_quote = "Fool! You think this world can exist without me!?"
def entrance():
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(entrance_description)
        entrance()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        entrance()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        entrance()
    elif player_action == 'n' or player_action == "north":
        print(stairwell_description)
        stairwell()
    else:
        print("I don't understand")
        entrance()
        
def stairwell():
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(stairwell_description)
        stairwell()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        stairwell()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        stairwell()         
    elif player_action == 'd' or player_action == "down":
        print(hallway_description)
        hallway()
    elif player_action == 's' or player_action == "south":
        print(entrance_description)
        entrance()
    else:
        print("I don't understand")
        stairwell()

def hallway():
    global rat_alive
    if rat_alive == 1:
        print("Ravio the goblin shouts and attacks you")
        mechanicsFork.combat(Player, Rat)
        rat_alive = 0
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(hallway_description)
        hallway()
    elif player_action == 'i' or player_action == 'inventory':
        print(Player.inv)
        hallway()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        hallway()
    elif player_action == 'n' or player_action == "north":
        print(dininghall_description)
        dininghall()
    elif player_action == 'u' or player_action == "up":
        print(stairwell_description)
        stairwell()
    else:
        print("I don't understand")
        hallway()

def dininghall():
    global dininghall_potion
    if dininghall_potion == 1:
        print("There is a health potion here.")
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(dininghall_description)
        dininghall()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        dininghall()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        dininghall()
    elif player_action == 'w' or player_action == "west":
       print(lounge_description)
       lounge()
    elif player_action == 'e' or player_action == "east":
        print(cellhall_description)
        cellhall()
    elif player_action == 's' or player_action == "south":
        print(hallway_description)
        hallway()
    elif "get" in player_action and "potion" in player_action and dininghall_potion == 1:
        print("You get the health potion")
        Player.inv.append("health potion")
        dininghall_potion = 0
        dininghall()
    else:
        print("I don't understand")
        dininghall()

def lounge():
    global warden_alive
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(lounge_description)
        lounge()
    if player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        lounge()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        lounge()
    elif player_action == 'n' or player_action == "north":
        print(office_description)
        if warden_alive == 0:
            print("There is a cell key here")
        office()
    elif player_action == 'e' or player_action == "east":
        print(dininghall_description)
        dininghall()
    else:
        print("I don't understand")
        lounge()

def office():
    global warden_alive
    if warden_alive == 1:
        print("You see Atrienus the Warden. He is carrying keys all over his body, and he wields a giant key as a weapon.")
        mechanicsFork.combat(Player, Warden)
        warden_alive = 0
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(office_description)
        if warden_alive == 0:
            print("There is a cell key here")
        office()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        office()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        office()
    elif "get" in player_action and "key" in player_action and warden_alive == 0:
        print("You get the key")
        Player.inv.append("cell key")
        warden_alive = 2
        office()
    elif player_action == 's' or player_action == "south":
        print(lounge_description)
        lounge()
    else:
        print("I don't understand")
        office()

def cellhall():
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(cellhall_description)
        cellhall()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        cellhall()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        cellhall()
    elif player_action == 'n' or player_action == "north":
        if "cell key" in Player.inv:
            print(cell_description)
            cell()
        else:
            print("That cell is locked")
            cellhall()
    elif player_action == 'w' or "west":
        print(dininghall_description)
        dininghall()
    else:
        print("I don't understand")
        cellhall()

def cell():
    global skeleton_alive
    if skeleton_alive == 1:
        print("You are ambushed by a skeleton!")
        mechanicsFork.combat(Player, Skeleton)
        skeleton_alive = 0
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(cell_description)
        cell()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        cell()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        cell()
    elif player_action == 'w' or player_action == "west":
        print(teleporter_description)
        teleporter()
    elif player_action == 's' or player_action == "south":
        print(cellhall_description)
        cellhall()
    else:
        print("I don't understand")
        cell()

def teleporter():
    global lobby_potions_taken
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(teleporter_description)
        teleporter()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        teleporter()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        teleporter()
    elif player_action == 'n' or player_action == "north":
        print(lobby_description)
        if lobby_potions_taken == 0:
            print("There are three potions here")
        lobby()
    elif player_action == 'e' or player_action == "east":
        print(cell_description)
        cell()
    else:
        print("I don't understand")
        teleporter()
        
def lobby():
    global toni_alive
    global caleb_alive
    global lobby_potions_taken
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(lobby_description)
        if lobby_potions_taken == 0:
            print("There are three health potion here")
        lobby()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        lobby()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        lobby()
    elif "get" in player_action and "potions" in player_action and lobby_potions_taken == 0:
        for i in range(3):
            Player.inv.append("health potion")
        print("You get the three potions")
        lobby_potions_taken = 1
        lobby()
    elif player_action == 'w' or player_action == "west":
        print(construction_description)
        if toni_alive == 0:
            print("There is a green keycard here")
        construction()
    elif player_action == 'e' or player_action == "east":
        print(jungle_description)
        if caleb_alive == 0:
            print("There is a blue keycard here")
        jungle()
    elif player_action == 'n' or player_action == "north":
        if "green keycard" in Player.inv and "blue keycard" in Player.inv:
            finalroom()
        else:
            print("That door is locked")
            lobby()
    else:
        print("I don't understand")
        lobby()

def construction():
    global toni_alive
    if toni_alive == 1:
        print("You see Toni Kong start to beat his chest and throw basketballs")
        mechanicsFork.combat(Player, Toni)
        toni_alive = 0
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(construction_description)
        if toni_alive == 0:
            print("There is a green keycard here")
        construction()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        construction()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        construction()
    elif "get" in player_action and "keycard" in player_action and toni_alive == 0:
        print("You get the keycard")
        Player.inv.append("green keycard")
        toni_alive = 2
        construction()
    elif player_action == 'e' or player_action == "east":
        print(lobby_description)
        lobby()
    else:
        print("I don't understand")
        construction()

def jungle():
    global caleb_alive
    if caleb_alive == 1:
        print("Caleb jumps out of a tree and screams, \"TAN CONG!!\"")
        mechanicsFork.combat(Player, Caleb)
        caleb_alive = 0
    player_action = input('>').lower()
    if player_action == 'l' or player_action == "look":
        print(jungle_description)
        if caleb_alive == 0:
            print("There is a blue keycard here")
        jungle()
    elif player_action == 'i' or player_action == "inventory":
        print(Player.inv)
        jungle()
    elif "drink" in player_action and "potion" in player_action and "health potion" in Player.inv:
        heal_amount = random.randint(1, 8) + 1
        if Player.hp + heal_amount > Player.max_hp:
            Player.hp = Player.max_hp
        else:
            Player.hp += heal_amount
        print("%s was healed for %i, leaving them with %i hp" % (Player.name, heal_amount, Player.hp))
        Player.inv.remove("health potion")
        jungle()
    elif "get" in player_action and "keycard" in player_action and caleb_alive == 0:
        print("You get the blue keycard")
        Player.inv.append("blue keycard")
        caleb_alive = 2
        jungle()
    elif player_action == 'w' or player_action == "west":
        print(lobby_description)
        lobby()
    else:
        print("I don't understand")
        jungle()

def finalroom():
    print(finalroom_description)
    print("The game master says, \"Fool! You dare enter my domain\"")
    mechanicsFork.combat(Player, Master)
    print("As the game master dies, this world slowly starts to fade away")
    print("Thank you for playing Wizards & Warriors")
entrance()
    
