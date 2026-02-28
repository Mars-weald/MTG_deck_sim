def marking_sequence(deck, marked_cards, marking):
    while marking == True:
        mark = input("Type VIEW to view the list of marked cards\nType RETURN to return to the main menu\n")
        if mark == "VIEW":
            print("Marked Cards:\n")
            for name in marked_cards:
                print(name)
            print("----------")
        elif mark == "RETURN":
            marking = False
            running = True
        else:
            for thing in deck:
                if thing.name.lower() == mark.lower():
                    if thing.name in marked_cards:
                        continue
                    else:
                        marked_cards.append(thing.name)
