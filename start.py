import os
from deck import *

def start_sequence():
    chosen_deck = input("Enter name of deck file: ")
    if chosen_deck in os.listdir("./decklists"):
        file = open(f"./decklists/{chosen_deck}")
        working_deck = file.read()
        library_sorted = make_deck(working_deck)
        return library_sorted
    else:
        raise Exception("Deck file not found")