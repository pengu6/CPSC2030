# Request the mileage at the last fill-up from the user
lastfillup = int(input("Input fuel mileage from last fill up: "))
# Request the current mileage from the user
currentmileage = int(input("Input current fuel mileage: "))
# Display the miles traveled to the user
milestravled = currentmileage - lastfillup 
print("Miles travled: " + str(milestravled))

# Request amount of gas added to the tank on this fill-up
gallonsfilled = int(input("How many gallons did you put in your car? "))

# Display the miles per gallon for this fill-up to the user
milespergallon = milestravled / gallonsfilled
print(milespergallon)

print("Welcome! To the smart fella quiz.... Three questions will be asked to help YOU find out what kind of smart fella you are!")


print("what kind of weekened activite would you like to do? ")
print("1 - Sleep")
print("2 - Dance")
print("3- Cook")
print("4- Chores")

activites = int(input())



if activites == 1:
    print("What would be the best place to sleep")
    print("1 - Bed of flowers")
    print("2 - Normal bed")
    print("3 - GFs bed")
    print("4 - The floor")

if activites == 2: 
    print("What kind of dance are you doing?")
    print("1 - Hip hop dances")
    print("2 - Break dance")
    print("3 - Slow dance")
    print("4 - Salsa")

bed = int()
dance = int()

if bed == 1:
    print("Thats a good bed")
if bed == 2:
    print("Thats an OK bed")
if bed == 3:
    print("Thats the best bed!")
if bed == 4:
    print("Thats not a good choice")

if dance == 1:
    print("You got some smooth moves")
if dance == 2:
    print("Break it down buddy!")
if dance == 3:
    print("Love bird <3")
if dance == 4:
    print("Need some chips or queso with that!")