from blackjack.deck import Deck
import random
import time

def calculate_total(hand):
    return sum([card.rank if card.name == 'A' else min(card.rank, 10) for card in hand])

def main():

    deck = Deck()
    random.shuffle(deck.cards)

    hand_player = []
    hand_dealer = []

    #Declare player score to avoid error if player doesn't hit
    total_player = 0

    #Give first card to dealer
    card = deck.cards.pop()
    hand_dealer.append(card)
    total_dealer = calculate_total(hand_dealer)

    print(f'Dealer has {card.name} of {card.suit.name}')
    while True:
        read = input('Stand, Hit:\n')

        #More robust if test
        if read.strip().lower() == 'hit':
            card = deck.cards.pop()
            hand_player.append(card)
            total_player = calculate_total(hand_player)

            #if total_player > 21, look for ace with rank 11 and change it to 1
            if total_player > 21:
                for card in hand_player:
                    if card.name == 'A' and card.rank == 11:
                        card.rank = 1
                        total_player = calculate_total(hand_player)
                        break

            #Changed card.rank to card.name
            print(f'Hit with {card.suit.name} {card.name}. Total is {total_player}')
            if total_player > 21:
                print('Bust, dealer won')
                return
        
        #More robst if test
        elif read.strip().lower() == 'stand':
            break
    
    #Dealer's turn

    while True:
        time.sleep(1)
        if total_dealer < 17:
            card = deck.cards.pop()
            hand_dealer.append(card)
            total_dealer = calculate_total(hand_dealer)

            #if total_dealer > 21, look for ace with rank 11 and change it to 1
            if total_dealer > 21:
                for card in hand_dealer:
                    if card.name == 'A' and card.rank == 11:
                        card.rank = 1
                        total_dealer = calculate_total(hand_dealer)
                        break

            #Changed card.rank to card.name
            print(f'Dealer hits it with {card.suit.name} {card.name}. Total is {total_dealer}')

            time.sleep(1)
            if total_dealer > 21:
                print('Dealer busted, you won!')
                break
        
        if total_dealer >= 17:
            print('Dealer stands')
            break
        
    
    time.sleep(1)
    if total_player > total_dealer:
        print('You won!')
    elif total_player < total_dealer:
        print('Dealer won!')
    else:
        print('Tie')

if __name__ == '__main__':
    main()
