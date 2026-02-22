def make_deck(decklist):
    lines = decklist.split("\n")
    for line in lines:
        carrd = line.split(maxsplit=1)
        print(carrd)