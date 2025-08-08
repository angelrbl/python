import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def seeCard(self, rank, suit):
        print(f"The drawn card is a {rank} of {suit.lower()}s.")

ranks = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['Diamond', 'Heart', 'Spade', 'Club']

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(Card(rank, suit))

def showDeck():
    for card in deck:
        print(card.rank, card.suit)

def drawRandomCard():
    card = random.randint(0, len(deck) + 1)
    deck[card].seeCard(deck[card].rank, deck[card].suit)

def shuffleDeck():
    for card in deck * 2:
        selCard = random.randint(0, len(deck) - 1)
        saveCard = deck[selCard]
        deck.pop(selCard)
        deck.append(saveCard)

def drawCard():
    card = int(input("Please, input the position of the card you want to draw (1-52): ")) - 1
    deck[card].seeCard(deck[card].rank, deck[card].suit)

drawRandomCard()