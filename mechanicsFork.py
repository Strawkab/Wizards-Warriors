import random #for dice rolls
class Character:        
    def __init__(self, name, str, dex, con, int, wis, cha, weapon, ac, hitdice, lvl):
        self.name = name
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.weapon = weapon
        self.ac = ac
        self.hitdice = hitdice
        self.lvl = lvl
        self.hp = 0
        if self.lvl > 1:
            for i in range(player_lvl - 1):
                self.hp += random.randint(1, self.hitdice) + (self.con - 10) / 2
        else:
            pass
        self.hp += self.hitdice
        self.max_hp = self.hp
        self.wizard = 0
        self.cleric = 0
        self.casts = 4
    def attack(self, target):
        if random.randint(1, 20) + int((self.dex - 10) / 2) > target.ac:
            damage_dealt = 0
            for i in range(self.weapon[0]):
                damage_dealt = random.randint(1, self.weapon[1]) + int((self.str - 10) / 2)
            if damage_dealt < 1:
                damage_dealt = 1
            target.hp -= damage_dealt
            print("%s hit %s for %i damage leaving them with %i hp" % (self.name, target.name, damage_dealt, target.hp))
        else:
            message = random.randint(0, 3)
            if message == 0:
                print("%s missed" % self.name)
            if message == 1:
                print("%s dodged %s's attack" % (target.name, self.name))
            if message == 2:
                print("%s's blow bounced off %s's armor" % (self.name, target.name))
            if message == 3:
                print("%s parried %s's attack" % (target.name, self.name))
    def missile(self, target):
        if self.wizard == 1 and self.casts > 0 and self.int >= 11:
            damage_dealt = random.randint(1, 4) + 1 + random.randint(1, 4) + 1 + random.randint(1, 4) + 1
            target.hp -= damage_dealt
            print("A bolt of magical energy flies out of %s's hand and strikes %s for %i damage, leaving them with %i hp" % (self.name, target.name, damage_dealt, target.hp))
            self.casts -= 1
        else:
            print("%s raises their hand, but their spell fizzles out" % self.name)
            if self.int < 11:
                print("Your intelligence was too low!")
    def heal(self):
        if self.cleric == 1 and self.casts > 0 and self.wis >= 11:
            heal_amount = random.randint(1, 8) + self.lvl
            if self.hp + heal_amount > self.max_hp:
                self.hp = self.max_hp
                print("%s's hand glows for a second, and they heal themself for %i, leaving them with %i hp" % (self.name, heal_amount, self.hp))
                self.casts -= 1
            else:
                self.hp += heal_amount
                print("%s's hand glows for a second, and they heal themself for %i, leaving them with %i hp" % (self.name, heal_amount, self.hp))
                self.casts -= 1
        else:
            print("%s raises their hand, but their spell fizzles out" % self.name)  
        if self.wis < 11:
            print("Your wisdom was too low!")






#stats being rolled
print("what is your name?")
player_name = input('>')
 
stat_pool = [
    random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6), 
    random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6), 
    random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6), 
    random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6), 
    random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6), 
    random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
]
#choosing which stats are being used
print("choose you stats, type in a ? if you need help, otherwise press enter")
if input('>') == '?':
    print("""
Strength determines how hard you can hit something
Dexterity determines how easy it is for you to hit something
Constitution determines how well you can shrug off enemy blows
Intelligence controls how well you can cast spells
Wisdom controls how well you can cast themauturgy
Charisma controls how well you can charm people
Type in your choice from the list by index(starting from 0)
        """)
else:
    pass
print("Which stat will be used for strength?")
print(stat_pool)
player_str = stat_pool.pop(int(input('>')))
print("Which stat will be used for dexterity?")
print(stat_pool)
player_dex = stat_pool.pop(int(input('>')))
print("Which stat will be used for constitution?")
print(stat_pool)
player_con = stat_pool.pop(int(input('>')))
print("Which stat will be used for intelligence?")
print(stat_pool)
player_int = stat_pool.pop(int(input('>')))
print("Which stat will be used for wisdom?")
print(stat_pool)
player_wis = stat_pool.pop(int(input('>')))
print("Which stat will be used for charisma?")
print(stat_pool)
player_cha = stat_pool.pop(int(input('>')))

print("which race do you want to play? (press ? for help)")
if input(">") == "?":
    print("""
Humans are average
Elves are agile, but don't have high defenses
Orcs posses brutish strength, but are mostly "special" and people don't like them
Dwarves are sturdy, but clumsy
Gnomes are sturdy, but weak
        """)
else:
    pass
print("Do you want to play a human, elf, orc, dwarf, or gnome?")
def choose_race():
    global player_str
    global player_dex
    global player_con
    global player_int
    global player_wis
    global player_cha
    chosen_race = input('>').lower()
    if chosen_race == "human":
        pass
    elif chosen_race == "elf":
        player_dex += 2
        player_con -= 2
    elif chosen_race == "orc":
        player_str += 4
        player_int -= 2
        player_wis -= 2
        player_cha -= 2
    elif chosen_race == "dwarf":
        player_dex -= 2
        player_con += 2
    elif chosen_race == "gnome":
        player_str -= 2
        player_con += 2
    else:
        print("I don't understand")
        choose_race()
choose_race()
print("Which class do you want to play? (press ? for help, otherwise press enter)")
if input('>') == '?':
    print("""
Fighters are skilled at physical combat
Rogues use their speed and wits to fight
Wizards are skilled at using magic
Clerics are skilled at using miracles
""")
else:
    pass
print("Do you want to play as a fighter, rogue, wizard, or cleric")
def choose_class():
    global player_weapon
    global player_ac
    global player_hitdice
    global player_wizard
    global player_cleric
    chosen_class = input('>').lower()
    if chosen_class == "fighter":
        player_weapon = [1, 8]
        if int((player_dex - 10) / 2) > 1:
            player_ac = 1
        else:
            player_ac = 10 + 8 + int((player_dex - 10) / 2)
        player_hitdice = 10
        player_wizard = 0
        player_cleric = 0
    elif chosen_class == "rogue":
        player_weapon = [1, 4]
        player_ac = 10 + 2 + int((player_dex - 10) / 2)
        player_hitdice = 6
        player_wizard = 0
        player_cleric = 0
    elif chosen_class == "wizard":
        player_weapon = [1, 4]
        player_ac = 10 + 1 + int((player_dex - 10) / 2)
        player_hitdice = 4
        player_wizard = 1
        player_cleric = 0
    elif chosen_class == "cleric":
        player_weapon = [1, 4]        
        player_ac = 10 + 1 + int((player_dex - 10) / 2)
        player_hitdice = 4
        player_cleric = 1
        player_wizard = 0
    else:
        print("I don't understand")
        choose_class()
choose_class()
player_lvl = 3
Player = Character(player_name, player_str, player_dex, player_con, player_int, player_wis, player_cha, player_weapon, player_ac, player_hitdice, player_lvl)
Player.inv = []
if player_wizard == 1:
    Player.wizard = 1
elif player_cleric == 1:
    Player.cleric = 1
else:
    pass

def combat(Player, enemy):
    Player_initiative = random.randint(1, 20) + Player.dex
    enemy_initiative = random.randint(1, 20) + enemy.dex
    if Player_initiative > enemy_initiative:
        print("%s siezes the initiative" % Player.name)
        while(Player.hp > 0 and enemy.hp > 0):
            player_action = input("What do you want to do? \n>").lower()
            if "attack" in player_action or player_action == 'a':
                Player.attack(enemy)
            elif "missile" in player_action or player_action == 'm':
                Player.missile(enemy)
            elif "heal" in player_action or player_action == 'h':
                Player.heal()
            else:
                print("You waste your turn thinking about what to do")
            enemy.attack(Player)
    elif Player_initiative < enemy_initiative:
        print("%s siezes the initiative" % enemy.name)
        while(Player.hp > 0 and enemy.hp > 0):
            enemy.attack(Player)
            player_action = input("What do you want to do?\n>").lower()
            if "attack" in player_action or player_action == 'a':
                Player.attack(enemy)
            elif "missile" in player_action or player_action == 'm':
                Player.missile(enemy)
            elif "heal" in player_action or player_action == 'h':
                Player.heal()
            else:
                print("You waste your turn thinking about what to do")
    else:   
        print("%s siezes the initiative" % Player.name)
        while(Player.hp > 0 and enemy.hp > 0):
            player_action = input("What do you want to do?\n>").lower()
            if "attack" in player_action or player_action == 'a':
                Player.attack(enemy)
            elif "missile" in player_action or player_action == 'm':
                Player.missile(enemy)
            elif "heal" in player_action or player_action == 'h':
                Player.heal()
            else:
                print("You waste your turn thinking about what to do")
            enemy.attack(Player)
    
    if enemy.hp <= 0:
        print(enemy.death_quote)
    
    if Player.hp <= 0:
        print("You have been defeated")
        exit()
