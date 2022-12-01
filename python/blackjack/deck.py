from collections import deque

from blackjack.suit import Suit
from blackjack.card import Card

class Deck:
    def __init__(self):

        self.cards = deque()


        for suit in Suit:
            for i in range(1, 14):
                self.cards.append(Card(rank=i, suit=suit, name=self.name(i)))

    def name(self, num):
        name = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        if num in name:
            return name[num]
        else:
            return num 
