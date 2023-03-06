import random

class Character:
    def __init__(self):
        self.name = input("Give your name to make a character: ")
        print("Your name is", self.name)
        self.strength = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.agility = random.randint(1, 10)

def compareStrength(character, difficulty):
    if character.strength + random.randint(1, 3) >= difficulty:
        return True
    else:
        return False

def compareAgility(character, difficulty):
    if character.Agility + random.randint(1, 3) >= difficulty:
        return True
    else:
        return False

def compareIntelligence(character, difficulty):
    if character.Intelligence + random.randint(1, 3) >= difficulty:
        return True
    else:
        return False

# Create character
my_character = Character()

# First encounter
print("You set out on a journey and encounter a dwarf on the road who wants to rob you.")
print("1. Fight the dwarf with your sword")
print("2. Run around the dwarf")
print("3. Try to talk the dwarf out of it")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    difficulty = 2
    if compareStrength(my_character, difficulty):
        print("You successfully defeated the dwarf in combat!")
    else:
        print("The dwarf proved to be too strong for you.")
elif choice == 2:
    difficulty = 4
    if compareAgility(my_character, difficulty):
        print("You managed to run circles around the dwarf and escape.")
    else:
        print("The dwarf caught up with you and robbed you anyway.")
elif choice == 3:
    difficulty = 6
    if compareIntelligence(my_character, difficulty):
        print("Your silver tongue convinced the dwarf to let you pass.")
    else:
        print("The dwarf was not impressed by your words and robbed you anyway.")
else:
    print("Invalid choice, please enter a number between 1 and 3.")