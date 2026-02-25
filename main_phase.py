from start import *
import sys

def core_sequence(deck):
    mutable = deck.copy()
    shuffle(mutable)
    step = input("Enter one:\nmark cards\nshuffle\ndraw card\ndraw hand\nexit\n")
    match step:
        case "mark cards":
            pass
        case "shuffle":
            shuffle(mutable)
            print("Deck shuffled")
        case "draw card":
            card = mutable[0]
            del mutable[0]
            print(card.name)
        case "draw hand":
            hand = mutable[0:7]
            del mutable[0:7]
            for card in hand:
                print(card.name)
        case "exit":
            sys.exit()

deck = start_sequence()
core_sequence(deck)