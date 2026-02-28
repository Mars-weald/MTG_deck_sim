from start import *
from marking_cards import *
import sys

def core_sequence(deck):
    running = True
    mutable = deck.copy()
    library = mutable.copy()
    shuffle(library)
    marked_cards = []
    while running == True:
        step = input("\nEnter one:\nmark cards\nshuffle\ndraw card\ndraw hand\nexit\n----------\n")
        match step:
            case "mark cards":
                running = False
                marking = True
                marking_sequence(deck, marked_cards, marking)
            case "shuffle":
                shuffle(library)
                print("Deck shuffled\n----------")
            case "draw card":
                draw_card(library)
                print("----------")
            case "draw hand":
                hand_size = 7
                x = 0
                while x < hand_size:
                    draw_card(library)
                    x += 1
                print("---------")
            case "exit":
                running = False
                sys.exit()

deck = start_sequence()
core_sequence(deck)