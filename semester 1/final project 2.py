# main.py

import adventures  # Import the adventures module

def main():
    print("\nWelcome to the game library! Choose the adventure you would like to go on.")
    print("1. Forest Adventure")
    print("2. Cave Adventure")
    print("3. Portal Adventure")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        adventures.forest_adventure()  # Call the dungeon adventure
    elif choice == "2":
        adventures.cave_adventure()  # Call the forest adventure
    elif choice == "3":
        adventures.portal_adventure() # Call the portal adventure
    else:
        print("\nInvalid choice. Try again")
        main()

if __name__ == "__main__":
    main()
