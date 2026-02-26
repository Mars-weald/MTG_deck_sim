from start import *
import sys

def core_sequence(deck):
    running = True
    mutable = deck.copy()
    library = mutable.copy()
    shuffle(library)
    while running == True:
        step = input("Enter one:\nmark cards\nshuffle\ndraw card\ndraw hand\nexit\n")
        match step:
            case "mark cards":
                pass
            case "shuffle":
                shuffle(library)
                print("Deck shuffled")
            case "draw card":
                draw_card(library)
            case "draw hand":
                hand_size = 7
                x = 0
                while x < hand_size:
                    draw_card(library)
                    x += 1
            case "exit":
                running = False
                sys.exit()

deck = start_sequence()
core_sequence(deck)