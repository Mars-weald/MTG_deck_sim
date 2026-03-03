import os
import sys
from deck import *

def start_sequence():
    while True:
        chosen_deck = input("Type 'EXIT' to quit \nEnter name of deck file: ")
        if chosen_deck in os.listdir("./src/decklists"):
            file = open(f"./src/decklists/{chosen_deck}")
            working_deck = file.read()
            library_sorted = make_deck(working_deck)
            return library_sorted
        elif chosen_deck == 'EXIT':
            sys.exit()
        else:
            print("Deck file not found\n----------\n")