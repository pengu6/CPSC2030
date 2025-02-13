
print("You're randomly walking on a path and you see a portal spawn. Do you go through it?")
print("1) Yes")
print("2) No")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("You enter the portal. You end up in medieval times""\n")
    print("Whats the first thing you're doing?")
    print("1) Find a village")
    print("2) Try to leave")
    
    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        print("You stumble upon a village full of very welcoming people!""\n")
        print("Whats the first thing you're doing in the village? ")
        print("1) Take a walk around, checking out the homes and vendors")
        print("2) Purchase gear and weapons and take off and go searching for a dragon to slay")
    elif choice2 == 2:
        print("You are unable to find the portal back and are stuck in medieval times.")
        exit()
    else:
        print("Invalid choice.")

    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        print("You end up going into someones home and having a great meal and realize you want to spend the rest of your life in this village")
        exit()
    elif choice3 == 2: 
        print("You are walking for hours until you stumble on a sleeping dragon. What do you do? ")
        print("1) Run away")
        print("2) Try to kill it while it sleeps")
    else:
        print("Invalid choice.")

    choice4 = int(input("Enter your choice: "))

    if choice4 == 1:
        print("You try to run away but the dragon wakes up and roasts you with its fire breath")
        exit()
    elif choice4 == 2:
        print("You slowly get on top of the dragons head and pierce your sword through its brain, killing it instantly""\n")
        print("You go back to the village and they make you their king. The End")
        exit()
    else:
        print("Invalid choice")

elif choice == 2:
    print("You walk past the portal and are killed by a giant bear that jumped out of the trees")
    exit()
else:
    print("Invalid choice")
    exit()
