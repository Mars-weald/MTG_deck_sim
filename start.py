import os
import deck

def start_sequence():
    chosen_deck = input("Enter name of deck file: ")
    if chosen_deck in os.listdir("./decklists"):
        file = open(f"./decklists/{chosen_deck}")
        working_deck = file.read()
        make_deck(working_deck)
    else:
        raise Exception("Deck file not found")

start_sequence()