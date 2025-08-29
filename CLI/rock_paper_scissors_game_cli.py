# rock_paper_scissors_game_cli.py
import random                                       # Random Module
Choices=["Rock", "Paper","Scissors"]                # List of Available Options
validChoices={"Rock","Paper","Scissors"}            # Set of Choices
print("Welcome to Rock-Paper-Scissors Game!")       # Welcome Message

# Initial Scores
userScore=0
computerScore=0
tieScore=0

while True:
    userChoice=input("Enter your Choice(Rock/Paper/Scissors) or 'Exit' to quit:").title() 
    if(userChoice=="Exit"):
        print("Game Over")
        print(f"Your Final Score={userScore}, Computer's Final Score={computerScore}, Total Ties={tieScore}")
        print("Thanks for playing")
        break
    if (userChoice not in validChoices):
        print("Invalid Input❌! Please enter Rock, Paper or Scissors.")
        continue
    computerChoice=random.choice(Choices)
    print(f"You chose {userChoice}")
    print(f"Computer chose {computerChoice}")
    if(userChoice==computerChoice):
        print("This is a tie🤝")
        tieScore+=1
    elif(userChoice=="Rock" and computerChoice=="Scissors") or\
        (userChoice=="Paper" and computerChoice=="Rock") or\
        (userChoice=="Scissors" and computerChoice=="Paper"):
        print("Congratulations! You are winner🎉")
        userScore+=1
    else:
        print("You lost the game. Better Luck next time☺")
        computerScore+=1
    print(f"Your Score={userScore}, Computer's Score={computerScore}, ties={tieScore}")