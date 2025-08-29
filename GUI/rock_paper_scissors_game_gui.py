# rock_paper_scissors_game_gui.py
import random                       
import tkinter as tk

# List of Available Options
Choices=["Rock","Paper","Scissors"] 

#Initial Scores
userScore=0
computerScore=0
tieScore=0
movesPlayed=0
maxMoves=10

def play(userChoice):
     global userScore, computerScore, tieScore, movesPlayed
     
     if movesPlayed>maxMoves:
          return
     
     computerChoice=random.choice(Choices)
     movesPlayed+=1
     movesLabel.config(text=f"Moves Played: {movesPlayed} / {maxMoves}")

     if userChoice==computerChoice:
          result="It is a tie🤝"
          tieScore+=1               

     elif (userChoice=="Rock" and computerChoice=="Scissors") or\
          (userChoice=="Paper" and computerChoice=="Rock") or\
          (userChoice=="Scissors" and computerChoice=="Paper"):
          result="You won this round!🎉"
          userScore+=1           

     else:
          result="You lost this round. Try again!"
          computerScore+=1        

          
     userLabel.config(text=f"You chose: {userChoice}")
     computerLabel.config(text=f"Computer chose: {computerChoice}")
     resultLabel.config(text=result)
     scoreLabel.config(text=f"Score ➤ You: {userScore} | Computer: {computerScore} | Ties: {tieScore}")

     if movesPlayed == maxMoves:
        for btn in gameButtons:
            btn.config(state="disabled")

        # Final Winner
        if userScore > computerScore:
            finalResult = "Congratulations! You won the game🎉!"
        elif computerScore > userScore:
            finalResult = "You lost the game. Better luck next time😞!"
        else:
            finalResult = "It's a draw overall🤝!"
        
        finalResultLabel.config(text=finalResult)

def reset():
    """Reset scores and labels without disabling buttons (clear current game progress)"""
    global userScore, computerScore, tieScore, movesPlayed
    userScore = 0
    computerScore = 0
    tieScore = 0
    movesPlayed = 0
    userLabel.config(text="")
    computerLabel.config(text="")
    resultLabel.config(text="")
    scoreLabel.config(text=f"Score ➤ You: 0 | Computer: 0 | Ties: 0")
    movesLabel.config(text=f"Moves Played: 0 / {maxMoves}")
    finalResultLabel.config(text="")

def restart():
    """Reset everything and enable game buttons for a new game"""
    reset()
    for btn in gameButtons:
        btn.config(state="normal")

root=tk.Tk()                                     
root.title("Rock, Paper, Scissors Game🎮")     
root.geometry("430x400")                     
root.resizable(False, False)
root.config(bg="white") 

# Displaying Heading Label
tk.Label(root,text="Rock✊, Paper🖐, Scissors✌ Game", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

buttonFrame=tk.Frame(root, bg="White")
buttonFrame.pack()

rockBtn = tk.Button(buttonFrame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"), bg="#AED6F1", relief="raised", bd=3)
paperBtn = tk.Button(buttonFrame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"), bg="#F9E79F", relief="raised", bd=3)
scissorsBtn = tk.Button(buttonFrame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"), bg="#F5B7B1", relief="raised", bd=3)

rockBtn.grid(row=0, column=0, padx=10)
paperBtn.grid(row=0, column=1, padx=10)
scissorsBtn.grid(row=0, column=2, padx=10)

gameButtons = [rockBtn, paperBtn, scissorsBtn]

 # Labels to show results and scores
userLabel=tk.Label(root, text="", font=("Arial", 12), bg="white")
userLabel.pack(pady=5)
computerLabel=tk.Label(root, text="", font=("Arial", 12), bg="white")
computerLabel.pack(pady=5)
resultLabel=tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="white")
resultLabel.pack(pady=10)
scoreLabel=tk.Label(root, text="Score ➤ You: 0 | Computer: 0 | Ties: 0", font=("Arial", 12), bg="white")
scoreLabel.pack(pady=5)
finalResultLabel = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="green", bg="white")
finalResultLabel.pack(pady=5)
movesLabel = tk.Label(root, text="Moves Played: 0 / 10", font=("Arial", 12), bg="white")
movesLabel.pack(pady=5)

controlFrame = tk.Frame(root, bg="white")
controlFrame.pack(pady=10)

tk.Button(controlFrame, text="Restart Game", font=("Arial", 12), command=restart).grid(row=0, column=0, padx=20)
tk.Button(controlFrame, text="Reset Scores", font=("Arial", 12), command=reset).grid(row=0, column=1, padx=20)

root.mainloop()