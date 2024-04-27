import random


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(rank)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value


def display_hand(hand, player):
    print(f"{player}'s Hand:")
    for card in hand:
        print(card[0])


def play_blackjack():
    while true:
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        
        print("Dealer's hand:")
        print(dealer_hand[0][0])
        print("\nYour Hand:")
        for card in player_hand:
            print(card[0])
            print("\n")


# Starta spelet
play_blackjack()



