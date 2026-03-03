from start import *
import sys

def core_sequence(deck):
    running = True
    library = deck.copy()
    shuffle(library)
    mutable = library.copy()
    marked_cards = []
    index = 0
    while running == True:
        step = input("\nEnter one:\nmark cards\nshuffle\ndraw card\ndraw hand\nreset\nview library\nexit\n----------\n")
        match step:
            case "mark cards":
                running = False #change menus from main to marking
                marking = True
                while marking == True:
                    mark = input("Type VIEW to view the list of marked cards\nType RETURN to return to the main menu\nType CLEAR LIST to reset marked cards\nEnter card to be marked: \n")
                    if mark == "VIEW":
                        print("Marked Cards:\n")
                        for name in marked_cards:
                            print(name)
                        print("----------")
                    elif mark == "RETURN":
                        marking = False
                        for card in deck: #cards marked here
                            if card.name in marked_cards:
                                card.mark()
                        running = True
                    elif mark == "CLEAR LIST":
                        marked_cards = []
                        print("Marked cards cleared\n--------\n")
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
                if len(library) == len(deck):
                    mutable = library.copy()
                print("Deck shuffled\n----------")

            case "draw card":
                draw_card(library)
                index += 1
                print("----------")

            case "draw hand":
                hand_size = int(input("Enter hand size: \n"))
                x = 0
                while x < hand_size:
                    draw_card(library)
                    x += 1
                index += hand_size
                print("---------")

            case "reset":
                library = mutable.copy()
                print("Deck reset\n----------\n")

            case "view library":
                for x, card in enumerate(library):
                    if card.is_marked == True:
                        print(f"{x + 1}. | {card.name} |")
                    else:
                        print(f"{x + 1}. {card.name}")
                print("----------")

            case "exit":
                running = False
                sys.exit()

            case _:
                print("ERROR: Invalid command\n----------")