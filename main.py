
#Imports
import random
import os
from os import system, name
import time
from time import sleep
import json
import sys

#Defining
def get_variables(file_path):
    """Gets all the variables from the given JSON file.
    Args:
        file_path: The path to the JSON file.
    Returns:
        A dictionary of variables.
    """
    with open(file_path, 'r') as f:
      data = f.readlines()
    return data
def load_save(file_path):
  """Loads variables from a JSON file and assigns them to corresponding variables in the current scope.
  Args:
      file_path: The path to the JSON file.
  """
  with open(file_path, 'r') as f:
    data = json.load(f)
  # Assign loaded values to corresponding variables in current scope
  globals().update(data)

def clear():
  if name == 'nt':
    _ = system('cls')
  
  else:
    _ = system('clear')

def userturn():
  print("+|Actions|+")
  print("Attack")
  print("Defend")
  print("Run")
  actionB = input("What do you do? ")
  if actionB == "Attack" or actionB == "attack":
    enemyhp = enemyhp - (atk + wpnatk)
    spd = spd - 1
  elif actionB == "Defend" or actionB == "defend":
    _def = maxdef + 1
    spd = spd - 1
  elif actionB == "Run" or actionB == "run":
    fightnum = 0
    menu = 0
    print("You Ran Away")

def battlecheck():
  if hp <= 0:
    print("You Died!")
    menu = 0
    fightnum = 0
    hp = 1
    spd = maxspd
    atk = maxatk
    _def = maxdef
    exp = exp - 3
  elif enemyhp <= 0:
    fightnum = 0
    menu = 0
    print("You Win!")
    exp = exp + ((enemyhp + 2) * 5)
    spd = maxspd
    atk = maxatk
    _def = maxdef
    gold = (gold + (1 * luck)) + (wealth * 2)
    itemrng = random.randint(1, 10)
    dorng = True

def wpnswitch():
  if not wpn == "None":
    if wpn == "Slime Sword":
      wpnatk = wpnatk - 1
    elif wpn == "Basic Dagger":
      wpnatk = wpnatk - 1
      eqspd = eqspd - 1

def armorswitch():
  if not armor == "None":
    if armor == "Leather Armor":
      eqdef = eqdef - 2
    elif armor == "Rotted Sheild":
      eqdef = eqdef - 1

def accswitch():
  if not accessory == "None":
    if accessory == "Soggy Boots":
      eqspd = eqspd - 1

#Starup Variables:
username = 0
passkey = 0
exp = 0
level = 1
atk = 1
_def = 0
spd = 1
hp = 10
maxhp = 10
maxspd = 1
maxatk = 1
maxdef = 0
wpnatk = 0
eqdef = 0
eqspd = 0
wpn = "None"
wpndesc = ""
armor = "None"
armrdesc = ""
accessory = "None"
accdesc = ""
gold = 0
#Extra Stats
lifesteal = 0
luck = 1
wealth = 0
exhp = 0
#Main Code
actionStart = "No"
Y = "Y"
N = "N"
clear()
actionStart = input("Have you played before? Y  N ")

if actionStart == "Y":
  print("Warning, this does not work yet, it is in Progress.")
  actionFileUser = input("Username: ")
  actionFilePass = input("Passkey: ")
  if actionFileUser == "savetest" and actionFilePass == "devtool":
    with open("dev_f.json", "r") as f:
      data = json.load(f) 
      globals().update(data)  # Update global variables directly from the dictionary
      print("How You Doin' Today?")
      print("Logging In SaveTester...")
      load_save("dev_f.json")
      
  else:
    with open("save_f.json", "r") as f:
      for line in f:
        username, passkey, exp, level, atk, _def, spd, hp, maxhp, maxspd, maxatk, maxdef, wpnatk, eqdef, eqspd, wpn, wpndesc, armor, armrdesc, accessory, accdesc, gold, lifesteal, luck, wealth, exhp = line.strip().split(",")
        if actionFileUser == username and ActionFilePass == password:
          print("Login Successful:")
          load_save("save_f.json")
    


else:
	username = input("What is your name? ")
	passkey = input("Passkey? ")
	#Setup Game
	exp = 0
	level = 1
	atk = 1
	_def = 0
	spd = 1
	hp = 10
	maxhp = 10
	maxspd = 1
	maxatk = 1
	maxdef = 0
	wpnatk = 0
	eqdef = 0
	eqspd = 0
	wpn = "None"
	wpndesc = ""
	armor = "None"
	armrdesc = ""
	accessory = "None"
	accdesc = ""
	gold = 0
	#Extra Stats
	lifesteal = 0
	luck = 1
	wealth = 0
	exhp = 0
player = username
#Inventory
inventory = list()
#Areas
area = list()
area.extend( ["Grassland"] )
area.extend( ["Graveyard"] )
area.extend( ["Dungeon"] )
exploreA = 0
dorng = False
def logo():                                                         
  print("      ,------.         ,--.                     ,-----.  ,---.   ")
  print("      |  .-.  \  ,---. |  |,--.  ,--.,---.     '  .-.  '/  .-'   ")
  print("      |  |  \  :| .-. :|  | \  `'  /| .-. :    |  | |  ||  `-,   ")
  print("      |  '--'  /\   --.|  |  \    / \   --.    '  '-'  '|  .-'   ")
  print("      `-------'  `----'`--'   `--'   `----'     `-----' `--'     ")
  print("       ,------.                                                  ")
  print(",-----. |  .-.  \ ,--.--. ,---.  ,--,--.,--,--,--. ,---. ,-----. ")
  print("'-----' |  |  \  :|  .--'| .-. :' ,-.  ||        |(  .-' '-----' ")
  print(",----.  |  '--'  /|  |   \   --.\ '-'  ||  |  |  |.-'  `) ,----. ")
  print("'----'  `-------' `--'    `----' `--`--'`--`--`--'`----'  '----' ")

print("----------------------------------------")
print("WARNING: THIS DOES NOT (CURRENTLY) SAVE")
print("----------------------------------------")
menu = 0
_gameOn = 0
itemget  = 0
menuselected = 0
nextlvl = 100
#Game Starts Here VVV
while 1:
  
  while _gameOn == 1:
    if not menuselected == 1:
      clear()
  #Leveling Up
    if exp >= nextlvl:
      print("{+}--------------------------------------{+}")
      print("Level Up")
      exp = exp - nextlvl
      level = level + 1
      hp = hp + 5
      maxhp = maxhp + 5
      nextlvl = nextlvl * 1.5
      print("ATK | DEF | SPD ")
      actionL = input("Choose a Stat To Improve: ")
      if actionL == "ATK" or actionL == "atk" or actionL == "Attack" or actionL == "attack":
        maxatk = maxatk + 1
        atk = maxatk
      elif actionL == "DEF" or actionL == "def" or actionL == "Defense" or actionL == "defense":
        maxdef = maxdef+1
        _def = maxdef
      elif actionL == "SPD" or actionL == "spd" or actionL == "Speed" or actionL == "speed":
        maxspd = maxspd + 1
        spd = maxspd
    elif menu == 0:
      logo()
      if itemget == 1:
        print("---------------------")
        print("You Obtained an Item!")
      print("-----Menu-----")
      print("Explore")
      print("Train")
      print("Rest")
      print("--------------")
      print("Inventory")
      print("Equipment")
      print("Stats")
      print("+-+-+-+-+-+-+-+")
      print("Save Game")
      print("Quit")
      print("~~--==--~~--==--~~")
      print("")
      actionM = input("What would you like to do? ")
      itemget = 0

  #Resting

    if actionM == "Rest" or actionM == "rest":
      clear()
      hp = maxhp + random.randint(0, 1)
      print("You recovered to ", maxhp, " hp!")
      menuselected = 1

    elif actionM == "Quit" or actionM == "quit":
      clear()
      sys.exit()
        

  #Inventory (List)
    elif actionM == "Inventory" or actionM == "inventory":
      clear()
      print("Inventory:")
      print("-----------------")
      print(inventory)
      print("Gold: ", gold)
      actionI = input("What would you like to do? (Equip Item) (Sell Item) (Menu): ")
      if actionI == "Menu" or actionI == "menu":
        menu = 0

      #Base Stuff
      elif actionI == "Sell Slime Sword":
        if 'Slime Sword' in inventory:
          gold = gold + 1
          inventory.remove('Slime Sword')
      elif actionI == "Sell Rotted Shield":
        if 'Rotted Shield' in inventory:
          gold = gold + 1
          inventory.remove('Rotted Shield')
      elif actionI == "Sell Soggy Boots":
        if 'Soggy Boots' in inventory:
          gold = gold + 1
          inventory.remove('Soggy Boots')
      elif actionI == "Sell Basic Dagger":
        if 'Basic Dagger' in inventory:
          gold = gold + 5
          inventory.remove('Basic Dagger')
      elif actionI == "Sell Leather Armor":
        if 'Leather Armor' in inventory:
          gold = gold + 10
          inventory.remove('Leather Armor')
      elif actionI == "Equip Slime Sword":
        if 'Slime Sword' in inventory:
          inventory.remove('Slime Sword')
          wpndesc = "Gives +1 Atk"
          wpnswitch()
          wpn = "Slime Sword"
          wpnatk = wpnatk + 1
          print("Slime Sword Equipped")
      elif actionI == "Equip Rotted Shield":
        if 'Rotted Shield' in inventory:
          inventory.remove('Rotted Shield')
          armor = "Rotted Shield"
          armrdesc = "Gives +1 Def"
          armorswitch()
          eqdef = eqdef + 1
          print("Rotted Shield Equipped")
      elif actionI == "Equip Soggy Boots":
        if 'Soggy Boots' in inventory:
          inventory.remove('Soggy Boots')
          accswitch()
          accessory = "Soggy Boots"
          accdesc = "Gives +1 Spd"
          eqspd = eqspd + 1
          print("Soggy Boots Equipped")
      elif actionI == "Equip Basic Dagger":
        if 'Basic Dagger' in inventory:
          inventory.remove('Basic Dagger')
          wpnswitch()
          wpn = "Basic Dagger"
          wpndesc = "Gives +1 Atk and +1 Spd"
          wpnatk = wpnatk + 1
          eqspd = eqspd + 1
      elif actionI == "Equip Leather Armor":
        if 'Leather Armor' in inventory:
          inventory.remove('Leather Armor')
          armorswitch()
          armor = "Leather Armor"
          eqdef = eqdef + 2
          menuselected = 1
      #Grassland items
      elif actionI == "Sell Wolf Pelt":
        if 'Wolf Pelt' in inventory:
          gold = gold + 3
          inventory.remove('Wolf Pelt')
      elif actionI == "Sell Wolf Fang":
        if 'Wolf Fang' in inventory:
          gold = gold + 4
          inventory.remove('Wolf Fang')
      elif actionI == "Sell Rusty Knife":
        if 'Rusty Knife' in inventory:
          gold = gold + 3
          inventory.remove('Rusty Knife')
      elif actionI == "Sell Golem Core":
        if 'Golem Core' in inventory:
          gold = gold + 5
          inventory.remove('Golem Core')
      elif actionI == "Sell Slime Greatsword":
        if 'Slime Greatsword' in inventory:
          gold = gold + 6
          inventory.remove('Slime Greatsword')
      elif actionI == "Sell Slime Core":
        if 'SlimeCore' in inventory:
          gold = gold + 4
          inventory.remove('Slime Core')
  #Saving  
    elif actionM == "Save Game" or actionM == "save game":

      clear()
      with open("save_f.json", "w") as f:
        # Write the variables to the file
        f.write("{\n")
        f.write(f'  "username" : "{username}",\n' )
        f.write(f'  "passkey" : "{passkey}",\n' )
        f.write(f'  "exp" : {exp},\n')
        f.write(f'  "level" : {level},\n')
        f.write(f'  "atk" : {atk},\n')
        f.write(f'  "_def" : {_def},\n')
        f.write(f'  "spd" : {spd},\n')
        f.write(f'  "hp" : {hp},\n')
        f.write(f'  "maxhp" : {maxhp},\n')
        f.write(f'  "maxspd" : {maxspd},\n')
        f.write(f'  "maxatk" : {maxatk},\n')
        f.write(f'  "maxdef" : {maxdef},\n')
        f.write(f'  "wpnatk" : {wpnatk},\n')
        f.write(f'  "eqdef" : {eqdef},\n')
        f.write(f'  "eqspd" : {eqspd},\n')
        f.write(f'  "wpn" : "{wpn}",\n')
        f.write(f'  "wpndesc" : "{wpndesc}",\n' )
        f.write(f'  "armor" : "{armor}",\n' )
        f.write(f'  "armrdesc" : "{armrdesc}",\n' )
        f.write(f'  "accessory" : "{accessory}",\n' )
        f.write(f'  "accdesc" : "{accdesc}",\n' )
        f.write(f'  "gold" : {gold},\n')
        f.write(f'  "lifesteal" : {lifesteal},\n')
        f.write(f'  "wealth" : {wealth},\n')
        f.write(f'  "luck" : {luck},\n')
        f.write(f'  "exhp" : {exhp},\n')
        f.write("}")
      
      print("Game Saved!")



  #Equipment
    elif actionM == "Equipment" or actionM == "equipment":
      clear()
      print("Equipment:")
      print("--------------------")
      print("Weapon: ", wpn)
      print(wpndesc)
      print("Armor: ", armor)
      print(armrdesc)
      print("Accessory: ", accessory)
      print(accdesc)
      menuselected = 1
  #Stats
    elif actionM == "Stats" or actionM == "stats":
      clear()
      print("+------------Stats------------+")
      print("Name: ", username)
      print("ATK: ", atk, "+", wpnatk)
      print("DEF: ", _def, "+", eqdef)
      print("SPD: ", spd, "+", eqspd)
      print("MAXHP: ", maxhp)
      print("+---------------+")
      print("EXP: ", exp)
      nxtlvl = (nextlvl - exp)
      print("EXP to Next LVL: ", nxtlvl)
      print("Level: ", level)
      menuselected = 1
  #Training
    elif actionM == "Train" or actionM == "train":
      clear()
      menu = 1
      enemyhp = 1
      print("[---]Battle[---]")
      fightnum = 1
      if fightnum == 1:
        enemyhp = 5
      while fightnum == 1:
        battlecheck()
        #rng stuff:
        if dorng == True:
          if itemrng == 2:
            inventory.extend( ["Slime Sword"] )
            print("You got Slime Sword!")
            itemget = 1
          elif itemrng == 5:
            inventory.extend( ["Rotted Shield"] )
            print("You got Rotted Shield!")
            itemget = 1
          elif itemrng == 7:
            inventory.extend( ["Soggy Boots"] )
            print("You got Soggy Boots!")
            itemget = 1
          dorng = False
        #fightin'
        elif fightnum == 1:
          print("Slime")
          enemyatk = 1
          enemydef = 0
          enemyspd = 0
          print("HP: ", enemyhp)
          print("+-", username, "-+")
          print("HP: ", hp)
          if enemyspd >= spd + eqspd:
            clear()
            print("Slime attacks for ", (enemyatk - (_def + eqdef)), "dmg")
            enemydmg = 0
            enemydmg = enemyatk - (_def + eqdef)
            hp = hp - enemydmg
            spd = maxspd
            _def = maxdef
          else:
            userturn()
  #Exploration
    elif actionM == "Explore" or actionM == "explore":
      clear()
      menu = 2
      print(area)
      inputE = input("Where would you like to go? ")
      if inputE == "Grassland":
        exploreA = 1
      elif inputE == "Graveyard":
        exploreA = 2
      elif inputE == "Dungeon":
        exploreA = 3
      while exploreA == 1:
          fightnum = random.randint(1, 3)
          print("Fight")
          print("Menu")
          print("Shop")
          inputGrass = input("What would you like to do? ")
          if inputGrass == "Shop" or inputGrass == "shop":
            print('Dravic: "Welcome to the shop!"')
            print("=+--Items--+=")
            print("Basic Dagger")
            print("- Gives +1 Atk and +1 Spd.")
            print("- 10 GP")
            print("Leather Armor")
            print("- Gives +2 Def")
            print("- 20 GP")
            inputGrassS = input("What would you like to do? (Buy [Item]) (Back) ")
            if inputGrassS == "Buy Basic Dagger" and gold >= 10:
              print("Basic Dagger Bought")
              gold = gold - 10
              inventory.extend( ["Basic Dagger"] )
            elif inputGrassS == "Buy Leather Armor" and gold >= 20:
              print("Leather Armor Bought")
              gold = gold - 20
              inventory.extend( ["Leather Armor"] )
          elif inputGrass == "Menu" or inputGrass == "menu":
            menu = 0
            exploreA = 0
          elif inputGrass == "Fight" or inputGrass == "fight":
            fightnum = random.randint(2, 4)
            if fightnum == 2:
              enemyhp = 10
            while fightnum == 2:
              battlecheck()
              #rng stuff:
              if dorng == True:
                if itemrng == 1:
                  inventory.extend( ["Wolf Pelt"] )
                  print("You got A Wolf Pelt!")
                  itemget = 1
                elif itemrng == 8:
                  inventory.extend( ["Wolf Fang"] )
                  print("You got A Wolf Fang!")
                  itemget = 1
                dorng = False
                #fightin'
              elif fightnum == 2:
                print("Wolf")
                enemyatk = 2
                enemydef = 0
                enemyspd = 1
                print("HP: ", enemyhp)
                print("+-", username, "-+")
                print("HP: ", hp)
                if enemyspd >= spd + eqspd:
                  clear()
                  print("Wolf attacks for ", (enemyatk - (_def + eqdef)), "dmg")
                  enemydmg = 0
                  enemydmg = enemyatk - (_def + eqdef)
                  hp = hp - enemydmg
                  spd = maxspd
                  _def = maxdef
                    
                else:
                  userturn()
            if fightnum == 3:
              enemyhp = 3
            while fightnum == 3:
              battlecheck()
              #rng stuff:
              if dorng == True:
                if itemrng == 3:
                  inventory.extend( ["Rusty Knife"] )
                  print("You got A Rusty Knife!")
                  itemget = 1
                elif itemrng == 9:
                  inventory.extend( ["Golem Core"] )
                  print("You got A Golem Core!")
                  itemget = 1
                dorng = False
              #fightin'
              elif fightnum == 3:
                print("Golem")
                enemyatk = 6
                enemydef = 1
                enemyspd = 0
                print("HP: ", enemyhp)
                print("+-", username, "-+")
                print("HP: ", hp)
                if enemyspd >= spd + eqspd:
                  clear()
                  print("Golem attacks for ", enemyatk, "dmg")
                  enemydmg = 0
                  enemydmg = enemyatk
                  hp = hp - enemydmg
                  spd = maxspd
                  _def = maxdef
                else:
                  userturn()
            if fightnum == 4:
              enemyhp = 10
            while fightnum == 4:
              battlecheck()
              #rng stuff:
              if dorng == True:
                if itemrng == 7:
                  inventory.extend( ["Slime Greatsword"] )
                  print("You got Slime Greatsword!")
                  itemget = 1
                elif itemrng == 4:
                  inventory.extend( ["Slime Core"] )
                  print("You got A Slime Core!")
                  itemget = 1
                dorng = False
                #fightin'
              elif fightnum == 4:
                print("Big Slime")
                enemyatk = 1
                enemydef = 1
                enemyspd = 1
                print("HP: ", enemyhp)
                print("+-", username, "-+")
                print("HP: ", hp)
                if enemyspd >= spd + eqspd:
                  clear()
                  print("The Big Slime attacks for ", (enemyatk - (_def + eqdef)), "dmg")
                  enemydmg = 0
                  enemydmg = enemyatk - (_def + eqdef)
                  hp = hp - enemydmg
                  spd = maxspd
                  _def = maxdef

                else:
                  userturn()

  #Fighting God (Unfinished)
    elif actionM == "fight god":
        if not wpnatk >= 5318008:
          print("}---------{+}--------{")
          print("You Shouldn't Do That.")
          print("}---------{+}--------{")
        elif not level >= 9112001:
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -o- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("You may have the attack power, but you would not survive a single swing.")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -o- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif izakused == "yes":
          print("--===--")
          print("Really?")
          print("--===--")
        else:
          print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
          print("So, You Really did it? You got the book, and are now Level 9112001. However, the lazy dev of this has not yet implemented me, check back later. My Apologies...")
          print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

  _gameOn = 1