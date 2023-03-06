import random
print("---- \nYou are a young adventurer looking to help your village by slaying a dragon in a nearby castle you have nothing but a sword wits and bravery on you  \n----")
class Character:
    def __init__(self):
        self.name = input("Give your name to make a character: ")
        print("---- \nYour name is", self.name)
        self.strength = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.agility = random.randint(1, 10)

def compareStrength(character, difficulty):
    if character.strength + random.randint(1, 3) >= difficulty:
        return True
    else:
        return False

def compareAgility(character, difficulty):
    if character.agility + random.randint(1, 3) >= difficulty:
        return True
    else:
        return False

def compareIntelligence(character, difficulty):
    if character.intelligence + random.randint(1, 3) >= difficulty:
        return True
    else:
        return False

# Create character
my_character = Character()
print("Strength:", my_character.strength)
print("Agility:", my_character.agility)
print("Intelligence:", my_character.intelligence)

# First encounter
print("---- \nYou set out on a journey and encounter a dwarf on the road who wants to rob you.")
print("1. Fight the dwarf with your sword")
print("2. Run around the dwarf")
print("3. Try to talk the dwarf out of it")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    difficulty = 2
    if compareStrength(my_character, difficulty):
        print("You successfully defeated the dwarf in combat!")
    else:
        print("The dwarf proved to be too strong for you. Game Over")
elif choice == 2:
    difficulty = 4
    if compareAgility(my_character, difficulty):
        print("You managed to run circles around the dwarf and escape.")
    else:
        print("The dwarf caught up with you and robbed you anyway. Game Over")
elif choice == 3:
    difficulty = 6
    if compareIntelligence(my_character, difficulty):
        print("Your silver tongue convinced the dwarf to let you pass.")
        stage="pass"
    else:
        print("The dwarf was not impressed by your words and robbed you anyway. Game Over")
else:
    print("Invalid choice, you broke the game")
#fork in the road TBD

#final boss fight
print("---- \nYou arrive inside the dragons castle and he notices your arrival. Brace yourself!")
DragonHP=50
Dragonfriendly = False
while DragonHP >=0 :
    print("---- \nThe mighty dragon is still alive and angry. He tries to hit you")
    print("1. Take the hit and hit him back with a mighty blow")
    print("2. Dodge his swing and stab him lightly")
    print("3. Try to reason with the Dragon to stop attackign villagers")
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        difficulty = 8
        if compareStrength(my_character, difficulty):
            print("You overpower the dragon with a wide swing and he yells out in pain")
            DragonHP = DragonHP - 10
        else:
            print("The dragon is stronger and crushes you with his swing, Game over")
            break
    elif choice == 2:
        difficulty = 5
        if compareAgility(my_character, difficulty):
            print("You dodge the dragons strike and inflict a tiny cut on him")
            DragonHP = DragonHP - 1
        else:
            print("The dragon catches you and crushes you with his swing. Game Over")
            break
    elif choice == 3:
        difficulty = 10
        if compareIntelligence(my_character, difficulty):
            print("You managed to convince the dragon to not attack villagers ever again")
            Dragonfriendly=True
            break
        else:
            print("The dwarf was not impressed by your words and robbed you anyway. Game Over")
            break
    else:
        print("Invalid choice")
if DragonHP <= 0:
    print("---- \nthe dragon dies and you win, your village can live safely knowing that the dragon wont threaten them again")
elif Dragonfriendly == True:
    print ("---- \nthe dragon is now friendly, he wont bother the villagers again and villagers are happy with you")

