from start import *
import sys

def core_sequence(deck):
    running = True
    mutable = deck.copy()
    library = mutable.copy()
    shuffle(library)
    marked_cards = []
    while running == True:
        step = input("\nEnter one:\nmark cards\nshuffle\ndraw card\ndraw hand\nreset\nexit\n----------\n")
        match step:
            case "mark cards":
                running = False
                marking = True
                while marking == True:
                    mark = input("Type VIEW to view the list of marked cards\nType RETURN to return to the main menu\nType CLEAR LIST to reset marked cards\n")
                    if mark == "VIEW":
                        print("Marked Cards:\n")
                        for name in marked_cards:
                            print(name)
                        print("----------")
                    elif mark == "RETURN":
                        marking = False
                        for card in deck:
                            if card.name in marked_cards:
                                card.mark()
                        running = True
                    elif mark == "CLEAR LIST":
                        marked_cards = []
                    else:
                        for thing in deck:
                            if thing.name.lower() == mark.lower():
                                if thing.name in marked_cards:
                                    continue
                                else:
                                    marked_cards.append(thing.name)
                                    print(f"{thing.name} marked\n----------\n")

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

            case "reset":
                library = deck.copy()
                shuffle(library)

            case "exit":
                running = False
                sys.exit()

            case _:
                print("ERROR: Invalid command")

deck = start_sequence()
core_sequence(deck)