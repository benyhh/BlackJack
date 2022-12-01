from blackjack.deck import Deck

def main():

    deck = Deck()
    hand = []
    while True:
        read = input('Stand, Hit:\n')

        #More robust if test
        if read.strip().lower() == 'hit':
            card = deck.cards.pop()
            hand.append(card)
            total = sum([min(card.rank, 10) for card in hand])

            #Changed card.rank to card.name
            print(f'Hit with {card.suit.name} {card.name}. Total is {total}')
            if total > 21:
                print('Bust')
                break
        
        #More robst if test
        elif read.stip().lower() == 'stand':
            break

if __name__ == '__main__':
    main()
