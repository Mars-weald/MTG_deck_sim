## _Magic: The Gathering_ Deck Simulator 
A simulator for _Magic: The Gathering_ decks, but can work with any card game, really. Check opening hands and mulligans quickly in your terminal.
You can mark important cards to find their location in your deck quickly. Useful for checking if you would see them in a game, and figuring out how many of those cards you should include.

#### TO START:
Create a file in the 'decklists' folder. Add your cards in the following format:
`{number of cards} {name of card}`
(e.g. `12 Plains`)

Then simply run the `main.sh` script or the `main.py` file in the `src` folder.

You will be prompted to enter the name of the file containing the deck you want to work with. **IMPORTANT:** This is the name of the _file_ containing the decklist, not the name of the deck itself.

#### TO MARK CARDS:
Enter `mark cards` on the main menu, then enter the cards you want to nark, one at a time. Return to the main menu to work with those cards.

_Note: The `reset` command wil return your library to its last point **before** drawing cards._