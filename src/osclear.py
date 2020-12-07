"""Module to clear the Shell"""

from sys import platform
import os
def clear():
    """ Check system and clear the Terminal/Console. """
    if platform.startswith("win32"):
        os.system("cls")
    else:
        os.system("clear")
