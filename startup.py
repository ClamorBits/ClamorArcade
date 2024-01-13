import tool as tl
import __init__ as game

# Startup
class Startup:
    print(tl.logo)
    tl.write("Welcome to the Arcade! Choose the game you want to play!\n")
    tl.delay(2)
    print("[1] Guess the number!")
    tl.delay(1)
    print("[2] Memory cards")

# Startup
class StartUpProcess:
    def ChoosingStartup():
        gamechoose = input("")
        if gamechoose == "1":
            tl.clean()
            game.gtnclass.gtngame()
    

Startup()
StartUpProcess.ChoosingStartup()