from random import randint #import randint from the random module

#Randomly assign for the winning numbers
winning = str(randint(000, 999))

#Get input from the player
player_bet = input("Enter a 3-digit number: ")

#Checks if the players input is 3 digit only
if player_bet.isdigit() and len(player_bet) == 3:
    #Prints 'Your numbers are:' if the given condition above is met
    print(f"Your numbers are: {player_bet}")
else:
    #Print 'Please enter a valid 3-digit number only' if it doesn't met the given condition
    print("Please enter a valid 3-digit number only.")

#Prints the winning numbers
print(f"Winning numbers are: {winning}")

#Check the players' numbers to see if they match the winning numbers.
if player_bet == winning:
    print("Congratulations! You won!")
elif set(player_bet) == set(winning):
    print("Congratulations! You partially won!")
else:
    print("Sorry, You lose!")