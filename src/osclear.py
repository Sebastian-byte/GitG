"""Module to clear the Shell"""

import os
def clear():
    """Check system and clear."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
