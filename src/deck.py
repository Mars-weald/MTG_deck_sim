from card import *
import random

def make_deck(decklist):
    lines = decklist.split("\n")
    card_list = []
    for line in lines:
        carrd = line.split(maxsplit=1)
        card_list.append(carrd)
    deck = build_deck(card_list)
    return deck
        
def build_deck(card_list):
    library = []
    for card in card_list:
        num = 0
        while num < int(card[0]):
            library.append(Card(card[1]))
            num += 1
    return library

def shuffle(deck):
    random.shuffle(deck)
    return deck

def draw_card(library):
    if len(library) == 0:
        print("No cards left\n")
        return
    card = library[0]
    del library[0]
    if card.is_marked == True:
        print(f"| {card.name} |")
    elif card.is_marked == False:
        print(card.name)