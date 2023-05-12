import random
import tool as tl

# Startup
class Startup:
    print(tl.logo)
    tl.write("Welcome to the Arcade! Choose the game you want to play!\n")
    tl.delay(2)
    print("[1] Guess the number!")
    tl.delay(1)
    print("[2] Memory cards")

# GuessTheNumber Sequence
class GuessTheNumberClass:
    # Self Variables
    def __init__(self):
        self.pickednumber = 0
        self.attemptsint = 0
        self.hints = 0
    
    # Game process
    def play(self):
        print(tl.GuessTheNumberLogo)
        tl.delay(2)
        tl.write("Welcome to the Guess the Number game! In this game, I will pick a number between 1, until the number you choose (Minimum 10), and you are given attempt to guess the number by how many times you choose to (Maximum 10)\n")
        tl.delay(2)
        tl.write("But, I may give you hints for 3 times, and I will also respond 'Higher' if the number is lower than my pick, and 'Lower' for vice versa\n\n")
        tl.delay(2)
        input("ENTER to continue...")
        tl.clean()
        tl.write("Alright, choose a number that I will pick from 1 to that number (Minimum 10): ")
        endnumber = input("")
        endint = int(endnumber)
        self.pickednumber = int(str(random.randint(1, endint)))
        tl.clean()
        tl.write("Now pick the number of attempts you can make (Maximum 10): ")
        attempts = input("")
        self.attemptsint = int(attempts)
        self.hints = 3

        while True:
            tl.clean()
            print(f"Attempts left : {self.attemptsint}")
            print(f"Hints left : {self.hints}")  
            # Checks if there are attempts left
            if self.attemptsint > 0:
                answerboxed = input(f"\n\nAnswer (1-{endint}): ")
                answerbox = int(answerboxed)
                # Correct answer
                if answerbox == self.pickednumber:
                    tl.clean()
                    tl.write(f"That's CORRECT! My number was {self.pickednumber}\n")
                    tl.delay(1)
                    tl.write(f"You guessed right with {self.attemptsint} attempts left and {self.hints} hints left.\n\n")
                    break
                # Too high
                elif answerbox > self.pickednumber:
                    tl.write("\nLower! Guess again")
                    tl.delay(1)
                    self.attemptsint -= 1
                # Too low
                else:
                    tl.write("\nHigher! Guess again")
                    tl.delay(1)
                    self.attemptsint -= 1
            # No attempts left
            else:
                tl.clean()
                tl.write("Whoops! You have no attempt left.\n")
                break
        
        tl.write("Do you want to play again? (Y/N) ")
        GTNReplayBox = input("")
        tl.clean()
        if GTNReplayBox.lower() == "y":
            self.play()
        else:
            tl.write("Returning to menu...")
            tl.delay(4)
            tl.clean()
            Startup()

gtn = GuessTheNumberClass()

# Startup
class StartUpProcess:
    def ChoosingStartup(self):
        gamechoose = input("")
        if gamechoose == "1":
            tl.clean()
            gtn.play()
    

Startup()
StartUpProcess()