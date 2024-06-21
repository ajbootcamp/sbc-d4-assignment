from random import randint #import randint from random module

#Randomly assign choices for player 2 and player 3
p2, p3 = randint(1,2), randint(1,2)

#Get input for player 1
p1 = int(input("Type 1 for Kulob\nType 2 for Hayang: "))

#Print players choices
print("Player 1: Kulob") if p1 == 1 else print("Player 1: Hayang")
print("Player 2: Kulob") if p2 == 1 else print("Player 2: Hayang")
print("Player 3: Kulob") if p3 == 1 else print("Player 3: Hayang")

#Determined the winner from the given condition
if (p1 == 1 and p2 == 2 and p3 == 2) or (p1 == 2 and p2 == 1 and p3 == 1):
    #Print 'Player 1 Win' if the given condition is met
    print("Player 1 Win!")

elif (p1 == 2 and p2 == 1 and p3 == 2) or (p1 == 1 and p2 == 2 and p3 == 1):
    #Print 'Player 2 Win' if the given condition is met
    print("Player 2 Win!")

elif (p1 == 2 and p2 == 2 and p3 == 1) or (p1 == 1 and p2 == 1 and p3 == 2):
    #Print 'Player 3 Win' if the given condition is met
    print("Player 3 Win!")

else:
    #Print 'No ome wins' if none of the given condition are met
    print("No one wins!")