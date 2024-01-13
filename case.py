# Issue on line 84 and 99 on gtn.py. In order to return to selection menu,
# the file needs to import the startup.py file that is imported in the __init__.py file. Which is not possible 
# because on startup.py the gtn file is used here by the startup file to boot the game on line 19 which cause circular
# import. Below is the code demonstration
import __init__
from __init__ import redogame
redogame()