class Card:
    def __init__(self, rank, suit, name):
        self.rank = rank
        self.suit = suit
        self.name = name #Added card name

        #Ace should have value 11, unless the total is > 21
        if self.rank == 1:
            self.rank = 11
