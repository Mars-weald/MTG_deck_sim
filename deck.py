from card import *

def make_deck(decklist):
    lines = decklist.split("\n")
    card_list = []
    for line in lines:
        carrd = line.split(maxsplit=1)
        card_list.append(carrd)
    deck = build_deck(card_list)
    print(deck)
        
def build_deck(card_list):
    library = []
    for card in card_list:
        num = 0
        while num < int(card[0]):
            library.append(Card(card[1]).name)
            num += 1
    return library