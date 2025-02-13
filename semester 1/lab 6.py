import random as rand

print("What would you like to do? ")
print("1) Guess your number")
print("2) Pick a number for you to guess")
selection = int(input("Enter selection: "))

if selection == 1:
    print("Alright! I'll try to guess your number.") 
    print("Make sure you pick a number between 1 and 31")

    guess = rand.randint(1,31)
    
    
    n = 0
    
    while True:
        
        n += 1
        print(f"My guess is: " + str(guess))
        
        print("How did I do?")
        print("1) My number is higher")
        print("2) My number is lower")
        print("3) That's my number")
        
        response = int(input("Enter selection: "))

        if response == 1:
            guess = guess + 1
        elif response == 2:
            guess = guess - 1
        elif response == 3:
            print(f"Yay! I guessed your number in " + str(n) + " attempts!")
            break
        else:
            print("Please enter a valid option (1, 2, or 3).")

elif selection == 2:
    print("Great! You'll try to guess my number between 1 and 31.")
    number = rand.randint(1,31)
    i = 0
    
    for guess in range(31):
        guess = int(input("What is my number? "))
        i += 1
        if guess > number:
            print("My number is lower")
        elif guess < number: 
            print("My number is higher")
        elif guess == number:
            print("You got it right in " + str(i) + " guesses")
            exit()

