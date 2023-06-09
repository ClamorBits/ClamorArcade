# Libraries
import os
import time
from time import sleep
import sys
import ctypes
import random

# Variables 
logo = r"""
/`|  /||\/|/\|)   /||)/` /||\[~  |\/| /|/`|_|||\ |[~
\,|_/-||  |\/|\  /-||\\,/-||/[_  |  |/-|\,| ||| \|[_
"""

GuessTheNumberLogo = r"""
   ___                                    .    _                  __    _                 _                  
 .'   \  ,   .   ___    ____   ____      _/_   /        ___       |\   |  ,   . , _ , _   \ ___    ___  .___ 
 |       |   | .'   `  (      (           |    |,---. .'   `      | \  |  |   | |' `|' `. |/   \ .'   ` /   \
 |    _  |   | |----'  `--.   `--.        |    |'   ` |----'      |  \ |  |   | |   |   | |    ` |----' |   '
  `.___| `._/| `.___, \___.' \___.'       \__/ /    | `.___,      |   \|  `._/| /   '   / `___,' `.___, /                                                                                                   
"""

# Replaces time.sleep()
def delay(seconds):
    time.sleep(seconds)

# Replaces os.system("cls")
def clean():
    os.system("cls")

# Typing Effect
def write(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)