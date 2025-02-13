import sys


def forest_adventure():
    def start_game():
        print("\nWelcome to the Adventure Game!")
        print("You find yourself in a dark forest with paths leading in multiple directions.")
        first_choice()

    def first_choice():
        print("\nWhat would you like to do?")
        print("1. Go north.")
        print("2. Go east.")
        print("3. Go west.")
        
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            wolf_encounter()
        elif choice == "2":
            treasure_room()
        elif choice == "3":
            abandoned_cabin()
        else:
            print("Invalid choice. Try again.")
            first_choice()

    def wolf_encounter():
        print("\nYou walk north and encounter a large, hungry wolf.")
        print("What do you do?")
        print("1. Fight the wolf.")
        print("2. Run back to the starting point.")
        
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("\nYou bravely fight the wolf but unfortunately, you are no match for it. Game Over!")
            play_again()
        elif choice == "2":
            print("\nYou manage to escape and return to the starting point.")
            first_choice()
        else:
            print("Invalid choice. Try again.")
            wolf_encounter()

    def treasure_room():
        print("\nYou head east and find a room filled with gold and jewels!")
        print("Congratulations, you have found the treasure and won the game!")
        play_again()

    def abandoned_cabin():
        print("\nYou walk west and find an abandoned cabin.")
        print("Inside, there's an old map on the table.")
        print("What do you do?")
        print("1. Take the map.")
        print("2. Leave the cabin.")
        
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("\nThe map shows the location of a hidden treasure to the east!")
            print("You decide to follow the map and find the treasure. You win!")
            play_again()
        elif choice == "2":
            print("\nYou leave the cabin and return to the starting point.")
            first_choice()
        else:
            print("Invalid choice. Try again.")
            abandoned_cabin()

    def play_again():
        print("\nWould you like to play again?")
        choice = input("Enter 'yes' or 'no': ").lower()
        if choice == "yes":
            start_game()
        elif choice == "no":
            print("Thanks for playing! Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")
            play_again()

    # Start the game
    start_game()

if __name__ == "__main__":
    forest_adventure()


def cave_adventure():
    def start_game():
        print("\nWelcome to a Cave Adventure!") 
        print("\nYou're solo camping in the forests of alaska and stumble across a giant cave system")
        first_choice()
    
    def first_choice():
        print("\nWhat would you like to do? ")
        print("1. Go into it ")
        print("2. Walk away ")
        print("3. Go home and come back with a friend ")
    
        choice = input("Enter 1, 2 or 3: ")
        if choice == "1":
            encave()
        elif choice == "2":
            bear()
        elif choice == "3":
            friend()
        else:
            print("Invalid choice")
            first_choice()

    def encave():
        print("You enter the cave...After entering you find 2 paths, left and right.  ")
        print("\nWhich one do you choose? ")
        choice = input("\nLeft or Right ")
        if choice == "Left":
            left()
        elif choice == "Right":
            right()
    
    def bear():
        print("\nYou walk away but end up running into a Polar bear! ")
        print("\nWhat are you going to do?")
        print("1. Try to climb a nearby tree")
        print("2. Play dead and hope it leaves")
        print("3. Fight it with your camping knife")

        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            print("\nYou climb the tree, but the bear waits at the bottom. After hours of waiting, you manage to escape.")
            print("Lesson learned: always be prepared for bears in the wild!")
            exit()
        elif choice == "2":
            print("\nYou play dead, and the bear sniffs you before wandering off. That was close!")
            print("You decide to head back to your camp, shaken but alive.")
            exit()
        elif choice == "3":
            print("\nYou try to fight the bear, but... it's a polar bear. It doesn't end well. The end.")
            exit()
        else:
            print("Invalid choice. Try again.")
            bear()

    def friend():
        print("\nYou go home and grab a friend, as you guys enter the cave you find 2 paths. One that leads left and the other leads right.")
        print("\nWhich one do you choose")
        
        choice = input("\nLeft or Right ")
        if choice.lower() == "left":
            left()
        elif choice.lower() == "right":
            right()
        else:
            friend()

    def left():
        print("\nYou take the left path and run into a sleeping Polar Bear!")
        print("\nWhat do you do?")
        print("1. Try to sneak around it")
        print("2. Turn around and run out ")

        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("\nYou carefully sneak around the bear, holding your breath with every step.")
            print("The bear stirs, but you manage to make it past without waking it. Well done!")
            print("You continue deeper into the cave and eventually find an ancient map that leads to hidden treasures elsewhere.")
            print("Your adventure has only just begun!")
            exit()
        elif choice == "2":
            print("\nYou turn around and run out of the cave, but the noise wakes the bear.")
            print("It chases you out, and you barely escape with your life. Maybe caves aren't for you.")
            exit()
        else:
            print("Invalid choice. Try again.")
            left()

    def right():
        print("You find a bunch of skeltons but you see a door at the end of the path")
        print("\nYou keep moving forward but find yourself facing a puzzle.")
        print("\nYou attempt to solve the puzzle but you cant seem to keep your footing becuase you're on a patch of ice!")
        print("\nYou end up catching your footing, solving the puzzle and opening the door to find a massive room full of gold and tresaure!")
        print("\nYou take as much as you can carry and end up living rich and happy till the end of time. The end")
        exit()



    start_game()

if __name__ == "__main__":
    cave_adventure()

def portal_adventure():
    def start_game():
        print("\nWelcome to a portal adventure!")
        print("\nYou're randomly walking on a path and you see a portal spawn.")
        first_choice()

    def first_choice():
        print("\nWhat would you like to do? ")
        print("1. Go into it ")
        print("2. Walk away ")

        choice = input("Enter 1 or 2")
        if choice == "1":
            enterport()
        elif choice == "2":
            bear()
        else:
            print("Invalid choice")
            first_choice()


    def enterport():
        print("\nYou enter the portal. You end up in medieval times.")
        print("Whats the first thing you're doing?")
        print("1) Find a village")
        print("2) Try to leave")

        choice = input("Enter 1 or 2: ")
        if choice == "1":
            village()
        elif choice == "2":
            leave()
        else:
            print("Invalid choice")
            enterport()

    def village():
        print("\nYou stumble upon a village full of very welcoming people!")
        print("Whats the first thing you're doing in the village? ")
        print("1) Take a walk around, checking out the homes and vendors")
        print("2) Purchase gear and weapons and head off to start a solo adventure")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            meal()
        elif choice == "2":
            dragon()
        else:
            print("Invalid choice")
            village()


    def leave():
        print("You are unable to find the portal back and are stuck in medieval times.")
       

    
    def meal():
        print("You end up getting invited into someones home for dinner. While having dinner you guys are telling stories, laughing, having some drinks.")
        print("\nAfter all that you realize that you dont want to go back home so you stay in the village for the rest of your life. The End")
        exit()

    def dragon():
        print("You are walking for hours until you stumble on a sleeping dragon. What do you do? ")
        print("1) Run away")
        print("2) Try to kill it while it sleeps")
    
        choice4 = int(input("Enter your choice: "))

        if choice4 == 1:
            print("You try to run away but the dragon wakes up and roasts you with its fire breath")
            exit()
        elif choice4 == 2:
            print("After seeing skeletons all around the dragon you slowly you make your way up to the dragons head careful not to wake it.")
            print("Once you make it ontop of the dragons head you slowly raise your blade and pierce it through its head. Killing it instantly")
            print("You return to the village to try and sell the dragon remains. Unbeknownst to you that dragon terrorized their village.")
            print("With you killing it it allowed them to live in peace for the rest of time. As a thank you they give you gifts and gold and crown you their new king. The End")
            exit()
        else:
            print("Invalid choice")

    def bear():
        print("You walk past the portal and are killed by a giant bear that jumped out of the trees")
        exit()
    start_game()
if __name__ == "__main__":
    portal_adventure()