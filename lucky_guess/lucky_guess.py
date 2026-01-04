import random 
number = [i for i in range(1,11)]
print("Let's play a game!")
print("Lucky guess game!\nYou have 5 tries.")
win = 0
tries=0
while True:
    guess = int(input("Guess a number from 1-10:"))
    while guess not in number:
        guess = int(input("Only enter numbers from 1-10:"))
    r=random.choice(number)
    if r==guess:
        print(f"You won!")
        win +=1
        choice=input("Would you like to play again(yes/no):").lower()
        while choice not in["yes","no"]:
            print("Only choose yes or no!")
            choice=input("Would you like to play again(yes/no):").lower()
        if choice=="no":
            print(f"Game end!\nYou got {win} wins.")
            break
        elif choice == "yes":
            print("Lets play again!")
            tries = 0
    else:
        if guess>r:
            if r==guess-1 or r==guess-2 or r ==guess-3:
                print("You are close!\nYou guessed a little high.")
            else:
                print("Not even close!. Guess a little low")
        else:
            if guess==r-1 or guess==r-2 or guess==r-3:
                print("You are close!\nYou guessed a little low.")
            else:
                print("Not even close!. Guess a little high")
        tries +=1 
    if tries==5:
        print("You ran out of tries!\nBetter luck next time")
        break
    else:
        print(f"Tries used:{tries}")  