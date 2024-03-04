# EXERCISE 4 TASK 1

# Note: 1) Further slight updates have been made to this final exercise to format output.
#       2) During final testing I noticed that, for player action selections, hitting enter without input crashed
#          the game. Implemented try-except from Python OOP Lecture 4 to get around this. Updated for final version of game.            

############################################################################################################################################

import random
import time

############################################################################################################################################

# CREATURE CLASS DEFINITION

class Creature:
    '''Basic creature class.'''
    
    def __init__(self, name, maxHP = 10):
        self.name = name
        self.maxHP = maxHP
        self.hp = self.maxHP            
        self.abilities = {"attack" : 1, "defense" : 5, "speed" : 5}
    
    def __str__(self):
        return f"\nName: {self.name}, Current HP: {self.hp}, Max HP: {self.maxHP}, Abilities: {self.abilities}\n"
    
    def setHP(self, value):
        self.hp = value
    
    def setMaxHP(self, value):
        self.maxHP = value
        
    def setAbilities(self, key, value):
            self.abilities[key] = value
    
    def check_life(self):
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} fainted ...")
            return self.hp                      
       
        else:
            return self.hp                      
        
    def attack(self, target):
       self.roll = random.randint(1,20)
       
       if self.roll > (target.abilities["defense"] + target.abilities["speed"]):
           self.damage = self.abilities["attack"] + random.randint(1,4)
           target.hp -= (self.damage)
           print(f"\n{self.name} attacks {target.name}!")
           print(f"Attack hits for {self.damage} damage!")
           print(f"{target.name}'s HP: {target.check_life()}")
        
       else:
           print(f"\n{self.name} attacks {target.name}!")
           print(f"Attack missed...")
           
    def auto_select(self, target_list):
        targets_in_play = [target for target in target_list if target.hp > 0]       # Reference: W3 Schools List Comprehension : https://www.w3schools.com/python/python_lists_comprehension.asp
        
        if len(targets_in_play) > 0:
            return random.choice(targets_in_play)
        
        else:
            return None
    
    def turn(self, round_num, target_list):
        #print("\nRound: ", round_num)
        self.selected_target = self.auto_select(target_list)
        
        if self.selected_target != None:
            time.sleep(1.5)
            self.attack(self.selected_target)
        
        elif self.selected_target == None:
            time.sleep(1.5)
            print(f"\nNo targets left for {self.name}!\n")
     
############################################################################################################################################   
    
# GOBLIN CLASS DEFINITION
     
class Goblin(Creature):
    '''Goblin creature class that inherits from Creature.'''
    
    def __init__(self, name):
        Creature.__init__(self, name, maxHP = 15)
        self.abilities = {"attack" : 3, "defense" : 6, "speed" : 6}   
        
############################################################################################################################################          

# ORC CLASS DEFINITION

class Orc(Creature):
    '''Orc creature class that inherits from Creature. '''
    
    def __init__(self, name):
        Creature.__init__(self, name, maxHP = 50)
        self.abilities = {"attack" : 5, "defense" : 8, "speed" : 3}
        self.rage = False
    
    def __str__(self):
        return Creature.__str__(self) + f"Rage: {self.rage}\n"
    
    def turn(self, round_num, target_list):
    
        self.selected_target = self.auto_select(target_list)
    
        if self.selected_target != None:
            if round_num % 4 == 0:
                time.sleep(1.5)
                self.heavy_attack(self.selected_target)
            else:
                time.sleep(1.5)
                self.attack(self.selected_target)

        elif self.selected_target == None:
            time.sleep(0.5)
            print(f"\nNo targets left for {self.name}!\n")
    
    def heavy_attack(self, target):
        if self.rage == False:                          # If not in rage, modify values to put in rage, then attack.
            self.abilities["attack"] += 5
            self.abilities["defense"] -= 3
            self.rage = True
            print(f"\n{self.name} is in RAGE!\n")
            Creature.attack(self, target)
            
        else:
            Creature.attack(self, target)               # If already in rage, just attack.
            
    def attack(self, target):
        if self.rage == True:                           # If in rage, reset values to default for Orc, then attack.
            
            self.abilities["attack"] = 5
            self.abilities["defense"] = 8
            self.rage = False
            print(f"\n{self.name} cooled down!")
            Creature.attack(self, target) 
        
        else:
            Creature.attack(self, target)               # If not in rage, just attack. 
            
############################################################################################################################################       

# WARRIOR CLASS DEFINIION

class Warrior(Creature):
    '''Warrior creature class that inherits from Creature.'''
    
    def __init__(self, name):
        Creature.__init__(self, name, maxHP = 50)
        self.abilities = {"attack" : 5, "defense" : 10, "speed" : 4}
        self.shield = False
        
    def __str__(self):
        return Creature.__str__(self) + f"Shield: {self.shield}\n"
        
    def shield_up(self):
        if self.shield == False:
            self.abilities["attack"] -= 4
            self.abilities["defense"] += 4
            self.shield = True
            print(f"\n{self.name} raised SHIELD!\n")
    
    def shield_down(self):
        if self.shield == True:
            self.abilities["attack"] = 5
            self.abilities["defense"] = 10
            self.shield = False
            print(f"\n{self.name} lowered shield!\n")
    
    def turn(self, round_num, target_list):
        
        self.selected_target = self.auto_select(target_list)
        
        if self.selected_target != None:
            if round_num % 4 == 1:
                time.sleep(1.5)
                Creature.attack(self, self.selected_target)
                self.shield_up()
            
            elif (round_num % 4 == 2) or (round_num % 4 == 3):
                time.sleep(1.5)
                Creature.attack(self, self.selected_target)
            
            elif round_num % 4 == 0:
                time.sleep(1.5)
                self.shield_down()
                Creature.attack(self, self.selected_target)
            
        elif self.selected_target == None:
            time.sleep(1.5)
            print(f"\nNo targets left for {self.name}!\n")
        
############################################################################################################################################

# ARCHER CLASS DEFINITION

class Archer(Creature):
    
    def __init__(self, name):
        Creature.__init__(self, name, maxHP = 30)
        self.abilities = {"attack" : 7, "defense" : 9, "speed" : 8}
        self.powershot = False
        
    def __str__(self):
        return Creature.__str__(self) + f"Power Shot: {self.powershot}\n"
    
    def power_shot(self, target):
        self.roll1 = random.randint(1,20)
        self.roll2 = random.randint(1,20)
        self.roll = max(self.roll1, self.roll2)
       
        if self.abilities["speed"] > target.abilities["speed"]:
           self.roll += (self.abilities["speed"] - target.abilities["speed"])
        
        if self.powershot == False:
            self.abilities["attack"] += 3
            self.abilities["defense"] -= 3
            self.powershot = True
            print(f"\n{self.name} using POWER SHOT!")
            
        if self.roll > (target.abilities["defense"] + target.abilities["speed"]):
           self.damage = self.abilities["attack"] + random.randint(1,8)
           target.hp -= (self.damage)
           print(f"\n{self.name} attacks {target.name}!")
           print(f"Attack hits for {self.damage} damage!")
           print(f"{target.name}'s HP: {target.check_life()}")
        
        else:
           print(f"\n{self.name} attacks {target.name}!")
           print("Attack missed...")
    
    def attack(self, target):
        if self.powershot == True:                           
            
            self.abilities["attack"] = 7
            self.abilities["defense"] = 9
            self.powershot = False
            print(f"\n{self.name} stopped using Power Shot!")
            Creature.attack(self, target) 
        
        else:
            Creature.attack(self, target)
    
    def auto_select(self, target_list):
        
        targets_in_play = [target for target in target_list if target.hp > 0]
        
        if len(targets_in_play) > 0:
            target_min_hp =  min(targets_in_play, key = lambda x: x.hp)
            return target_min_hp
        
        else:
            return None
        
    
    def turn(self, round_num, target_list):
        
        self.selected_target = self.auto_select(target_list)
        
        if self.selected_target != None:
            if round_num % 4 == 1:
                time.sleep(1.5)
                self.attack(self.selected_target)
            
            else:
                time.sleep(1.5)
                self.power_shot(self.selected_target)
            
        elif self.selected_target == None:
            time.sleep(1.5)
            print(f"\nNo targets left for {self.name}!\n")
        
############################################################################################################################################    
   
# FIGHTER CLASS DEFINITION

class Fighter(Creature):
    
    def __init__(self, name):
        Creature.__init__(self, name, maxHP = 50)
        self.abilities = {"attack" : 5, "defense" : 8, "speed" : 5}
        
    def auto_select(self, target_list):
        
        targets_in_play = [target for target in target_list if target.hp > 0]
        
        if len(targets_in_play) > 0:
            target_max_hp =  max(targets_in_play, key = lambda x: x.hp)
            return target_max_hp
        
        else:
            return None
    
    def turn(self, round_num, target_list):
        
        self.selected_target = self.auto_select(target_list)
        self.default_attack = 5
        self.reduced_attack = self.default_attack - 3  
        
        if self.selected_target != None:
            
            print(f"\n{self.name} uses FLURRY attack!")
            
            for attack in range(1,4):
                time.sleep(1.5)
                
                if attack > 1:
                    self.abilities["attack"] = self.reduced_attack
                
                Creature.attack(self, self.selected_target)
                
                if self.selected_target.check_life() <= 0:
                    self.selected_target = self.auto_select(target_list)
            
            self.abilities["attack"] = self.default_attack
                    
            
        elif self.selected_target == None:
            time.sleep(1.5)
            print(f"\nNo targets left for {self.name}!\n")

############################################################################################################################################  
       
# ORC GENERAL CLASS DEFINITION
   
class OrcGeneral(Warrior, Orc):
    
    def __init__(self, name):
        Warrior.__init__(self, name)
        Orc.__init__(self, name)        # Placed second to set abilities equal to that of Orc parent class.
        self.maxHP = 80
        self.hp = self.maxHP
        
    def __str__(self):
        return Creature.__str__(self) + f"Shield: {self.shield}, Rage: {self.rage}\n"

    def turn(self, round_num, target_list):
        
        self.selected_target = self.auto_select(target_list)
        
        if self.selected_target != None:
            
            if round_num % 4 == 1:
                self.attack(self.selected_target)
                self.shield_up()
                
            elif round_num % 4 == 2:
                self.attack(self.selected_target)
            
            elif round_num % 4 == 3:
                self.shield_down()
                self.attack(self.selected_target)
                
            elif round_num % 4 == 0: 
                self.heavy_attack(self.selected_target)
                
        elif self.selected_target == None:
            time.sleep(1.5)
            print(f"\nNo targets left for {self.name}!\n")    

############################################################################################################################################ 

# GOBLIN KING CLASS DEFINITION

class GoblinKing(Archer, Goblin):
    
    def __init__(self, name):
        Archer.__init__(self, name)
        Goblin.__init__(self, name)
        self.maxHP = 50
        self.hp = self.maxHP
      
# No further definition necessary as __str__ inherited from Archer as is turn().

############################################################################################################################################

# BOSS CLASS DEFINITION

class Boss(Orc):
    def __init__(self, name):
        Orc.__init__(self, name)
        self.maxHP = 200
        self.hp = self.maxHP
        self.abilities = {"attack" : 5, "defense" : 8, "speed" : 5}
        self.selectmode = "weak"
        self.boss_lock = 0      # Added to prevent Balrog being readded to battle. Patch for Battle start() method. 
        
    def __str__(self):
        return Orc.__str__(self) + f"Select Mode: {self.selectmode}"

    def auto_select(self, target_list):
        
        targets_in_play = [target for target in target_list if target.hp > 0]
        
        if len(targets_in_play) > 0:
            
            if self.selectmode == "strong":
                target_max_hp =  max(targets_in_play, key = lambda x: x.hp)
                return target_max_hp
            
            elif self.selectmode == "weak":
                target_min_hp =  min(targets_in_play, key = lambda x: x.hp)
                return target_min_hp
            
            elif self.selectmode == "random":
                target_max_hp =  max(targets_in_play, key = lambda x: x.hp)
                target_min_hp =  min(targets_in_play, key = lambda x: x.hp)
                targets = [target_max_hp, target_min_hp]
                return random.choice(targets)
                      
        else:
            return None
    
    def turn(self, round_num, target_list):
        
        self.default_attack = 5
        self.reduced_attack = self.default_attack - 3  
        
        targets_in_play = [target for target in target_list if target.hp > 0]
        
        if len(targets_in_play) > 0:
            
            if round_num % 4 == 1:
                
                self.selectmode = "weak"
                self.selected_target = self.auto_select(targets_in_play)
                
                print(f"\n{self.name} selected WEAKEST target!")
                
                for attack in range(1,4):
                    time.sleep(1.5)
                    
                    if attack > 1:
                        self.abilities["attack"] = self.reduced_attack
                    
                    Creature.attack(self, self.selected_target)
                    
                    if self.selected_target.check_life() <= 0:
                        self.selectmode = "random"
                        self.selected_target = self.auto_select(targets_in_play)
                        print(f"\n{self.name} selected RANDOM target!")
                
                self.abilities["attack"] = self.default_attack
                    
            else:
                self.selectmode = "strong"
                self.selected_target = self.auto_select(targets_in_play)
                print(f"\n{self.name} selected STRONGEST target!")
                self.heavy_attack(self.selected_target)
                                
        elif len(targets_in_play) == 0:
            time.sleep(1.5)
            print(f"\nNo targets left for {self.name}!\n")
        
############################################################################################################################################     

# WIZARD CLASS DEFINITION

class Wizard(Creature):
    
    def __init__(self, name):
        Creature.__init__(self, name, maxHP = 20)
        self.abilities = {"attack" : 3, "defense" : 5, "speed" : 5, "arcana" : 10}
        self.max_mana = 100
        self.mana = self.max_mana
        self.quit = 0
        
    def __str__(self):
        return Creature.__str__(self) + f"Mana: {self.mana}"
    
    def attack(self, target):
        
        self.roll = random.randint(1,20)
       
        if target == None:
            print("\nNo targets left for {self.name}.")
            return None
           
        elif self.roll > (target.abilities["defense"] + target.abilities["speed"]):
           self.damage = self.abilities["attack"] + random.randint(1,4)
           target.hp -= (self.damage)
           print(f"\n{self.name} attacks {target.name}!")
           print(f"Attack hits for {self.damage} damage!")
           print(f"{target.name}'s HP: {target.check_life()}")
           self.mana = min(self.max_mana, self.mana + 20)
           print(f"{self.name}'s Mana +20!\n")
           if self.mana == self.max_mana:
               print(f"{self.name}'s mana is full!")
           else:
               print(f"{self.name}'s Mana: ", self.mana)
        
        elif self.roll < (target.abilities["defense"] + target.abilities["speed"]):
            print(f"\n{self.name} attacks {target.name}!")
            print("Attack missed...")
        
    def recharge(self):
        
        self.mana = min(self.max_mana, self.mana + 30)
        print(f"\n{self.name} used Recharge!")
        print(f"{self.name}'s Mana +20!\n")
        if self.mana == self.max_mana:
            print(f"{self.name}'s mana is full!")
        else:
            print(f"{self.name}'s Mana: ", self.mana)
        
    def firebolt(self, target):
        
        self.roll = random.randint(1,20) + (self.abilities["arcana"]//2)
       
        if self.roll > (target.abilities["defense"] + target.abilities["speed"]):
           self.damage = random.randint(1, self.abilities["arcana"])
           target.hp -= (self.damage)
           print(f"\n{self.name} cast Firebolt on {target.name}!\n")
           print(f"Attack hits for {self.damage} damage!")
           print(f"{target.name}'s HP: {target.check_life()}")
           self.mana = min(self.max_mana, self.mana + 10)
           print(f"\n{self.name}'s Mana +10!\n")
           if self.mana == self.max_mana:
               print(f"\n{self.name}'s mana is full!")
           else:
               print(f"\n{self.name}'s Mana: ", self.mana)
        
        else:
           print(f"\n{self.name} cast Firebolt on {target.name}!\n")
           print(f"Attack missed...")
    
    def heal(self, target):

        if self.mana >= 20:
            target.hp += (random.randint(0,8) + (self.abilities["arcana"]//2))
            target.hp = min(target.maxHP, target.hp)
            self.mana -= 20
            print(f"\n{self.name} cast heal on {target.name}!\n")
            print(f"{self.name}'s Mana -20!\n")
            if self.mana == 0:
               print(f"\n{self.name}'s mana depleted!\n")
            else:
               print(f"\n{self.name}'s Mana: ", self.mana)    
       
        else:
            print('\nNot enough Mana!\n')
    
    def mass_heal(self, allies):
        
        if self.mana >= 30:
            
            # Assumption made that the random heal value applies individually to each ally.
            print(f"\n{self.name} cast Mass Heal on party!\n")
            for ally in allies:
                random_heal = random.randint(1,10) + self.abilities["arcana"]
                ally.hp += random_heal
                ally.hp = min(ally.maxHP, ally.hp)
                print(f"{self.name} healed {ally.name} for +{random_heal}!")
            self.mana -= 30
            print(f"\n{self.name}'s Mana -30!\n")
            if self.mana == 0:
               print(f"\n{self.name}'s mana depleted!")
            else:
               print(f"\n{self.name}'s Mana: ", self.mana)
            
        else:
            print('\nNot enough Mana!\n')
    
    def firestorm(self, enemies):
        
        targets_in_play = [target for target in enemies if target.hp > 0]
        
        if self.mana >= 50:
            
            self.firestorm_damage = random.randint(5,20) + self.abilities["arcana"]
            self.firestorm_roll = random.randint(1, 20) + self.abilities["speed"]
            
            if self.firestorm_roll >= self.abilities["arcana"]:
                self.firestorm_damage //= 2
                print(f"\n{self.name} cast Firestorm for HALF DAMAGE!\n")
            
            else:
                
                print(f"\n{self.name} cast Firestorm for FULL DAMAGE!\n")  
            
            for target in targets_in_play:
                target.hp -= self.firestorm_damage
                print(f"Firestorm deals {self.firestorm_damage} damage to {target.name}!")
                print(f"{target.name}'s HP: {target.check_life()}")
            
            self.mana -= 50
            
            print(f"\n{self.name}'s Mana -50!\n")
            
            if self.mana == 0:
               print(f"\n{self.name}'s mana depleted!")
            else:
               print(f"\n{self.name}'s Mana: ", self.mana)
               
        else:
            print('\nNot enough Mana!')
    
    def select_target(self, target_list):
        
        targets_in_play = [target for target in target_list if target.hp > 0]
        
        if len(targets_in_play) > 0:
            print()
            for target in targets_in_play:
                print(f"{targets_in_play.index(target) + 1}: {target.name}, HP :{target.hp}/{target.maxHP}")
                
            while True:
                try:
                    self.choice = int(input('\nEnter choice: '))
                    
                    if not self.choice:
                        
                        print("\nInvalid choice! Please try again!\n")
                        continue

                    if (self.choice >= 1 and self.choice <= len(targets_in_play)):
                        break
                    
                    elif (self.choice < 1 or self.choice > len(targets_in_play)):
                        print("\nInvalid choice! Please try again!\n")
                        continue
                        
                except ValueError:
                    print("\nInvalid choice! Please try again!\n")
                    
            return targets_in_play[self.choice - 1]
        
    def select_heal_target(self, heal_target_list):
        
        for target in heal_target_list:
            print(f"{heal_target_list.index(target)+1}: {target.name}, HP: {target.hp}/{target.maxHP}")
        
        while True:
            try:
                self.choice = int(input('\nEnter choice: '))
                
                if not self.choice:
                    
                    print("\nInvalid choice! Please try again!\n")
                    continue

                if (self.choice >= 1 and self.choice <= len(heal_target_list)):
                    break
                
                elif (self.choice < 1 or self.choice > len(heal_target_list)):
                    print("\nInvalid choice! Please try again!\n")
                    continue
                
            except ValueError:
                print("\nInvalid choice! Please try again!\n")
        
        return heal_target_list[self.choice - 1]   
    
    def player_turn(self, attack_target_list, heal_target_list):
        
        self.full_heal_list = heal_target_list + [self]    
        print('\n#####################')
        print('     PLAYER MENU     ')
        print('#####################\n')
        
        print('\nPLAYER STATUS:\n')
        print(f"Name:\t\t{self.name}")
        print(f"HP:\t\t{self.hp}/{self.maxHP}")
        print(f'Mana"\t\t{self.mana}/{self.max_mana}')
        
        print('\nALLIES:\n')
        for ally in heal_target_list:
                print(f"{ally.name}\t\tHP: {ally.hp}/{ally.maxHP}")
        print(f"{self.name}\t\tHP: {self.hp}/{self.maxHP}")
                
        print('\nSELECT ACTION:\n')
        
        print('1: Attack')
        print('2: Firebolt')
        print('3: Firestorm')
        print('4: Heal')
        print('5: Mass Heal')
        print('6: Recharge')
        print('\nENTER 0 TO QUIT')
        
        print('\nEnter a number from 1-6.')  
        #while self.action not in [0, 1, 2, 3, 4, 5, 6]:
        #    print('\nInvalid input. Enter number from 1-6.')
        #    self.action  = input(int('Enter choice: '))
        
        while True:
            try:
                self.action = int(input('\nEnter choice: '))
                
                #if not self.action:
                    
                    #print("\nInvalid choice! Please try again!\n")
                    #continue

                if self.action in [0, 1, 2, 3, 4, 5, 6]:
                    break
                
                elif self.action not in [0, 1, 2, 3, 4, 5, 6]:
                    print("\nInvalid choice! Please try again!\n")
                    continue
                    
            except ValueError:
                print("\nInvalid choice! Please try again!\n")
        
        if self.action == 1 or self.action == 2:
            self.attack_target = self.select_target(attack_target_list)
            
            if self.action == 1:
                time.sleep(1.5)
                self.attack(self.attack_target)
                
            elif self.action == 2:
                time.sleep(1.5)
                self.firebolt(self.attack_target)

            
        elif self.action == 3:
            time.sleep(1.5)
            self.firestorm(attack_target_list)
        
        elif self.action == 4:
            time.sleep(1.5)
            self.heal_target = self.select_heal_target(self.full_heal_list)
            self.heal(self.heal_target)
        
        elif self.action == 5:
            time.sleep(1.5)
            self.mass_heal(self.full_heal_list)
        
        elif self.action == 6:
            time.sleep(1.5)
            self.recharge()
        
        elif self.action == 0:
            self.quit = 1
                
############################################################################################################################################

# BATTLE CLASS DEFINITION

class Battle:
    
    def __init__(self):
        
        self.player = Wizard("Gandalf")
        self.enemies = [GoblinKing("Goblin King"), OrcGeneral("Orc General"), Goblin("Goblin"), Orc("Orc")]
        self.allies = [Fighter("Boromir"), Archer("Legolas"), Warrior("Aragorn"), Creature("Frodo")]
        self.boss = Boss("Balrog")

        
    def start(self):
        
        print("\n#############################################\n")
        print("THE BATTLE FOR MIDDLE EARTH BEGINS! :-(\n")
        time.sleep(2.0)
        print("\n#############################################\n")
            
        for round_num in range(1, 50):
            
            # Evaluate active enemies and allies before round begins to show who is still in play.
            
            self.active_allies = [ally for ally in self.allies if ally.hp > 0]
            self.active_enemies = [enemy for enemy in self.enemies if enemy.hp > 0]
            
            self.all_characters = self.active_enemies + self.active_allies
            
            self.all_characters.sort(key = lambda x: x.abilities["speed"], reverse = True)
            
            
            print("\n#################\nROUND NUMBER: ", round_num, "\n#################\n")
            print("\nALLIES IN PLAY: \n")
    
            for ally in self.active_allies:
                if ally.hp > 0:
                    print(f"{ally.name}\t\tHP: {ally.hp}/{ally.maxHP}")
    
            print('\nENEMIES IN PLAY: \n')
    
            for enemy in self.active_enemies:
                
                # Included this to align HP tabs in output.
                # Probably a better way to do it but it's just a quick fix!
                
                if enemy.hp > 0 and len(enemy.name) <= 6:
                    print(f"{enemy.name}\t\tHP: {enemy.hp}/{enemy.maxHP}")
                else:
                    print(f"{enemy.name}\tHP: {enemy.hp}/{enemy.maxHP}")
            
            time.sleep(2.5)
            print(f"\n------------------START!-------------------\n")
           
            for i in range(0, len(self.all_characters)):
                if self.all_characters[i] in self.allies:
                    
                    self.all_characters[i].turn(round_num, self.active_enemies)
                    
                    # There is a possibility that all remaining enemies can be eliminated in a round. Therefore, self.active_enemies list 
                    # will be rebuilt after each characters turn to remove defeated enemies and also to facilitate triggering addition of 
                    # Boss mid-round. If self.active_enemies drops to one, Boss is added to self.enemies and self.active_enemies is constructed
                    # again before leaving the current iteration completes to make it selectable to the next ally to take their turn. 
                    
                    self.active_enemies = [enemy for enemy in self.enemies if enemy.hp > 0]
                    
                    if len(self.active_enemies) <= 1 and self.boss.boss_lock == 0:
                        self.boss.boss_lock = 1
                        self.enemies += [self.boss]
                        self.active_enemies = [enemy for enemy in self.enemies if enemy.hp > 0]
                        
                        time.sleep(2.5)
                        
                        print('\n####################################\n')
                        print(f"{self.boss.name} JOINED THE BATTLE!")
                        print('\n####################################\n')
                        
                        time.sleep(2.5)
                    
                    # Boss HP more than double all other enemies. Assume Boss fainting as win condition for allies.
                    if self.boss.hp == 0:
                        break  
                    
                    
                elif self.all_characters[i] in self.enemies:
                    
                    self.all_characters[i].turn(round_num, self.active_allies)
                    
                    self.active_allies = [ally for ally in self.allies if ally.hp > 0]
                    
                    # Fainting of all allies is win condition for enemies.
                    if len(self.active_allies) == 0:
                        break
                        
                        
            # Boss HP more than double all other enemies. Assume Boss fainting as win condition for allies.
            
            self.player.player_turn(self.enemies, self.allies)

            if self.player.quit == 1:
                print('\nQUITTING.....')
                break
            
            if self.boss.hp == 0:
                print("\nYOU DEFEATED THE BOSS!\n\nALLIES WON!\n")
                break
            
            # Fainting of all allies is win condition for enemies.
            if len(self.active_allies) == 0:
                print("\nYOU HAVE BEEN DEFEATED!\n\nENEMIES WON!\n")
                break
            
            print(f"\n-------------ROUND {round_num} FINISHED!-------------\n")
            
            print(f'\n\n\nGET READY FOR ROUND {round_num + 1}!\n\n\n')
            time.sleep(4)
        

############################################################################################################################################

# BATTLE SCRIPT
            
battle = Battle()
battle.start()

print("GAME OVER!\n")

############################################################################################################################################
            
            
            

        

        
        
        
        
        
        
        
        
        