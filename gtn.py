import tool as tl
import __init__ as stp
from __init__ import redogame

tl.ucl()
print("Welcome to the number game!")
tl.delay(2)
tl.write("I will pick a number from the range you picked, and you'll try to guess it!")
tl.delay(2)
tl.ucl()
class gtnclass:
    global repeat
    repeat = 1
    def gtngame():
        tl.write("Now, please pick a number range for me\n")
        tl.delay(1)
        nrcheck = True
        while nrcheck == True:
            numansw = input("Number range (Minimum 10) : ")
            numrange = int(numansw)
            if numrange >= 10:
                tl.ucl()
                nrcheck = False
            if numrange < 10:
                tl.write("Uh oh! You need to pick a number 10 or above!")
                tl.delay(3)
                tl.ucl()
                tl.write("Now, pick a number again, but this time, 10 or above\n")
        
        tl.write("Now pick how many number of tries allowed before the game ends!\n")
        trcheck = True
        while trcheck == True:
            transw = input("Number of tries (Maximum 10) : ")
            transint = int(transw)
            if transint <= 10:
                tl.ucl()
                trcheck = False
            if transint > 10:
                tl.write("Uh oh! You need to pick a number 10 or below!\n")
                tl.delay(1)
                tl.write("I can't make this any more easier!")
                tl.delay(3)
                tl.ucl()
                tl.write("Now, pick a number again, but this time, 10 or below\n")
        
        
        tl.write(f"Alright! I will pick a number between 1 to {numrange}\nand you will have {transint} tries before losing the game.")
        tl.delay(3)
        tl.ucl()
        tl.write("The game will start in...\n")
        tl.delay(1)
        ctdwn = 3
        while ctdwn > 0:
            tl.write(f"{ctdwn}...\n")
            tl.delay(1)
            ctdwn = ctdwn - 1
        tl.ucl()
        thenum = tl.random.randint(1, numrange)
        while transint > 0:
            if transint == 0:
                tl.write(f"Whoops! You ran out of number of tries! My number was {thenum}.\nBetter luck next time!")
                tl.delay(3)
                tl.ucl()
                break
            print(f"{thenum}\nNumber of tries left : {transint}")
            guess = input("Your guess : ")
            guess = int(guess)
            if guess == thenum:
                tl.ucl()
                tl.write(f"Congratulations, you picked my number, which is {thenum}!\n")
                tl.delay(3)
                tl.write("Do you wanna play again?\n")
                rescon = input("(y/n) : ")
                if rescon == "y":
                    tl.ucl()
                    print("Restarting game...")
                    tl.delay(5)
                    tl.ucl()
                    break
                if rescon == "n":
                    tl.ucl()
                    print("Quitting...")
                    tl.delay(5)
                    redogame()
                    break
            if guess > thenum:
                print("The number is lower than that!")
                tl.delay(2)
                transint = transint - 1
                tl.ucl()
            if guess < thenum:
                print("The number is higher than that!")
                tl.delay(2)
                transint = transint - 1
                tl.ucl()
    while repeat == 1:
        gtngame()
        if repeat == 0:
            redogame()
