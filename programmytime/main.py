import random
import datetime
from level import Level

myname="Unknown"
inventory = []
equiped_item = "Axe"
start_time = datetime.datetime.now()

player_x = 1
player_y = 1

def equip(player_name, hand_item, backpack):
    choice = input(f"{player_name}, would you like to equip an item? ")
    if choice.lower() == "yes":
        choice = int(input("Which item would you like to equip? 0 to Unequip: "))
        if choice == 0:
            if hand_item != "nothing":
                backpack.append(hand_item)
                hand_item = "nothing"
            print("Emptying hand.")
        else:
            if hand_item != "nothing":
                backpack.append(hand_item)
            print(f"Putting {backpack[choice-1]} in hand.")
            hand_item = backpack.pop(choice-1)
    else:
        print("Be that way.")
    return hand_item, backpack

def show_inventory():
    print("You check your backpack and you find the following items in it:")
    print("\tSLOT\t\tITEM")
    count_of_items_in_inventory = len(inventory)
    for x in range(count_of_items_in_inventory):
        print(f"\t{x+1}\t-\t{inventory[x]}")

def request_command():
    global equiped_item
    global inventory
    global myname
    global start_time
    global player_x, player_y
    command = input("Enter a command: ")
    if command.lower() == "show inventory":
        show_inventory()
        equiped_item, inventory = equip(player_name="Fart Breath", hand_item=equiped_item, backpack=inventory)
    elif command.lower() == "equip":
        equiped_item, inventory = equip(player_name=myname, hand_item=equiped_item, backpack=inventory)
    elif command.lower() == "quit":
        quit()
    elif command.lower() == "w":
        player_y -= 1
    elif command.lower() == "a":
        player_x -= 1
    elif command.lower() == "s":
        player_y += 1
    elif command.lower() == "d":
        player_x += 1



print("Hi. Welcome to my amaze game.")
myname = input("Please enter your name: ")

print("Your name is", myname)

print(f"You awaken in a cold cell with a slight headache. You look at your watch and see it's {start_time:%I:%M:%p}. \nYou reach into your pocket and find...")

pocket_items = ["lighter", "cellphone", "condom", "keys", "change", "Thor's Hammer"]

ran1 = random.randrange(0,len(pocket_items))
ran2 = random.randrange(0,len(pocket_items))

while ran2 == ran1:
    ran2 = random.randrange(0,len(pocket_items))

print(f"{pocket_items[ran1]} and {pocket_items[ran2]}")

inventory.append(pocket_items[ran1])
inventory.append(pocket_items[ran2])

level1 = Level(1, 15, 10)
level1.load_level()


while(True):
    level1.draw_screen(player_loc_x=player_x, player_loc_y=player_y)
    print(f"Currently equiped item is {equiped_item}")
    print("Available commands: show inventory, equip, quit, w, a, s, d")
    request_command()
